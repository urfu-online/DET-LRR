# -*- coding: utf-8 -*-
import logging
from _collections import OrderedDict
from datetime import timedelta

import auto_prefetch
from addict import Dict
from django.conf import settings
from django.contrib.postgres.fields import IntegerRangeField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.models.fields import ArrayField

from lrr.complexes import models as complex_model
from lrr.repository import models as repository_model
from lrr.repository.models import DigitalResource
from lrr.users.models import Person, Expert

logger = logging.getLogger(__name__)

CHOICES_HELP_TEXT = (
    """Поле выбора используется только в том случае, если тип вопроса
если тип вопроса - "радио", "выбор" или
'select multiple' - список разделенных запятыми
варианты этого вопроса ."""
)

EXPERTISE_TYPES = {
    'methodical': 'Методическая экспертиза',
    'contental': 'Содержательная экспертиза',
    'technical': 'Техническая экспертиза'
}


def validate_choices(choices):
    """  Verifies that there is at least two choices in choices
    :param String choices: The string representing the user choices.
    """
    values = choices.split(settings.CHOICES_SEPARATOR)
    empty = 0
    for value in values:
        if value.replace(' ', '') == '':
            empty += 1
    if len(values) < 2 + empty:
        msg = 'Для выбранного поля требуется связанный список вариантов.'
        msg += ' Варианты должны содержать более одного элемента.'
        raise ValidationError(msg)


def in_duration_day():
    return now() + timedelta(days=settings.DEFAULT_SURVEY_PUBLISHING_DURATION)


class ExpertiseType(auto_prefetch.Model):
    title = models.CharField(_('Name'), max_length=400)
    description = models.TextField(_('Description'), null=True, blank=True)

    template = models.CharField(_('Template'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'вид экспертизы'
        verbose_name_plural = 'виды экспертизы'

    def __str__(self):
        return self.title

    @property
    def safe_name(self):
        return self.title.replace(' ', '_').encode('utf-8').decode('ISO-8859-1')

    def latest_answer_date(self):
        """Return the latest answer date.

        Return None is there is no response."""
        min_ = None
        for response in self.responses.all():
            if min_ is None or min_ < response.updated:
                min_ = response.updated
        return min_

    def get_absolute_url(self):
        return reverse('survey:survey-detail', kwargs={'id': self.pk})

    def non_empty_categories(self):
        return [x for x in list(self.categories.order_by('order', 'id')) if x.questions.count() > 0]

    def get_expertise_opinions(self, expert, expertise_type, request):
        return self.expertiseopinion_set.filter(Q(expert=expert) & Q(expertise_type=expertise_type) & Q(request=request))

    def is_methodic(self):
        if 'методическая' in self.title.lower():
            return True
        else:
            return False

    def is_content(self):
        if 'содержательная' in self.title.lower():
            return True
        else:
            return False

    def is_tech(self):
        if 'техническая' in self.title.lower():
            return True
        else:
            return False


class Category(auto_prefetch.Model):
    title = models.CharField('Название', max_length=400)
    expertise_type = auto_prefetch.ForeignKey(ExpertiseType, on_delete=models.CASCADE, verbose_name='Вид экспертизы', related_name='categories',
                                              null=True, blank=True)
    order = models.IntegerField('Порядок отображения', blank=True, null=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title

    def slugify(self):
        return slugify(str(self), allow_unicode=True)


class SortOpinionIndicator:
    CARDINAL = 'cardinal'
    ALPHANUMERIC = 'alphanumeric'


class Indicator(auto_prefetch.Model):
    """
    ex-Question
    """
    TEXT = 'text'
    SHORT_TEXT = 'short-text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_IMAGE = 'select_image'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'
    FLOAT = 'float'
    DATE = 'date'

    INDICATOR_TYPES = (
        (TEXT, _('text (multiple line)')),
        (SHORT_TEXT, _('short text (one line)')),
        (RADIO, _('radio')),
        (SELECT, _('select')),
        (SELECT_MULTIPLE, _('Select Multiple')),
        (SELECT_IMAGE, _('Select Image')),
        (INTEGER, _('integer')),
        (FLOAT, _('float')),
        (DATE, _('date')),
    )

    text = models.TextField('Наименование показателя', null=True)
    order = models.IntegerField('Порядок отображения', default=0)
    category = auto_prefetch.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True, related_name='indicators'
    )
    expertise_type = auto_prefetch.ForeignKey(ExpertiseType, on_delete=models.CASCADE, verbose_name='Вид экспертизы', related_name='indicators', null=True)
    type = models.CharField(_('Type'), max_length=200, choices=INDICATOR_TYPES, default=TEXT)
    per_discipline = models.BooleanField('Для каждой дисциплины', default=False)
    discipline = models.ForeignKey('repository.Subject', verbose_name='Дисциплина', blank=True, null=True, on_delete=models.SET_NULL)
    choices = models.TextField(_('Choices'), blank=True, null=True, help_text=CHOICES_HELP_TEXT)
    parent = models.ForeignKey('self', related_name='referrals', null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'показатель'
        verbose_name_plural = 'показатели'
        ordering = ('expertise_type', 'order')

    def save(self, *args, **kwargs):
        if self.type in [Indicator.RADIO, Indicator.SELECT, Indicator.SELECT_MULTIPLE]:
            validate_choices(self.choices)
        super(Indicator, self).save(*args, **kwargs)

    def get_clean_choices(self):
        """ Return split and stripped list of choices with no null values. """
        if self.choices is None:
            return []
        choices_list = []
        for choice in self.choices.split(settings.CHOICES_SEPARATOR):
            choice = choice.strip()
            if choice:
                choices_list.append(choice)
        return choices_list

    @property
    def opinion_indicators_as_text(self):
        """Return opinion_indicators as a list of text.

        :rtype: List"""
        opinion_indicators_as_text = []
        for answer in self.opinion_indicators.all():
            for value in answer.values:
                opinion_indicators_as_text.append(value)
        return opinion_indicators_as_text

    def is_group_indicator(self):
        if self.per_discipline and not (self.discipline or self.parent):
            logger.debug(f"is_group_indicator {self.text}: {self.per_discipline} and {not (self.discipline or self.parent)}")
            return True
        return False

    @staticmethod
    def standardize(value, group_by_letter_case=None, group_by_slugify=None):
        """ Standardize a value in order to group by slugify or letter case """
        if group_by_slugify:
            value = slugify(value)
        if group_by_letter_case:
            value = value.lower()
        return value

    @staticmethod
    def standardize_list(string_list, group_by_letter_case=None, group_by_slugify=None):
        """ Return a list of standardized string from a csv string.."""
        return [Indicator.standardize(strng, group_by_letter_case, group_by_slugify) for strng in string_list]

    def opinion_indicators_cardinality(
        self,
        min_cardinality=None,
        group_together=None,
        group_by_letter_case=None,
        group_by_slugify=None,
        filter=None,
        other_indicator=None,
    ):
        """Return a dictionary with opinion_indicators as key and cardinality (int or
            dict) as value

        :param int min_cardinality: The minimum of answer we need to take it
            into account.
        :param dict group_together: A dictionary of value we need to group
            together. The key (a string) is a placeholder for the list of value
            it represent (A list of string)
        :param boolean group_by_letter_case: If true we will group 'Aa' with
            'aa and 'aA'. You can use group_together as a placeholder if you
            want everything to be named 'Aa' and not 'aa'.
        :param boolean group_by_slugify: If true we will group 'Aé b' with
            'ae-b' and 'aè-B'. You can use group_together as a placeholder if
            you want everything to be named 'Aé B' and not 'ae-b'.
        :param list filter: We will exclude every string in this list.
        :param Question other_indicator: Instead of returning the number of
            person that answered the key as value, we will give the cardinality
            for another answer taking only the user that answered the key into
            account.
        :rtype: Dict"""
        if min_cardinality is None:
            min_cardinality = 0
        if group_together is None:
            group_together = {}
        if filter is None:
            filter = []
            standardized_filter = []
        else:
            standardized_filter = Indicator.standardize_list(filter, group_by_letter_case, group_by_slugify)
        if other_indicator is not None:
            if not isinstance(other_indicator, Indicator):
                msg = "Indicator.answer_cardinality expect a 'Indicator' for "
                msg += "the 'other_indicator' parameter and got"
                msg += " '{}' (a '{}')".format(other_indicator, other_indicator.__class__.__name__)
                raise TypeError(msg)
        return self.__opinion_indicators_cardinality(
            min_cardinality,
            group_together,
            group_by_letter_case,
            group_by_slugify,
            filter,
            standardized_filter,
            other_indicator,
        )

    def __opinion_indicators_cardinality(
        self,
        min_cardinality,
        group_together,
        group_by_letter_case,
        group_by_slugify,
        filter,
        standardized_filter,
        other_indicator,
    ):
        """Return an ordered dict but the insertion order is the order of
        the related manager (ie question.opinion_indicators).

        If you want something sorted use sorted_opinion_indicators_cardinality with a set
        sort_answer parameter."""
        cardinality = OrderedDict()
        for answer in self.opinion_indicators.all():
            for value in answer.values:
                value = self.__get_cardinality_value(value, group_by_letter_case, group_by_slugify, group_together)
                if value not in filter and value not in standardized_filter:
                    if other_indicator is None:
                        self._cardinality_plus_n(cardinality, value, 1)
                    else:
                        self.__add_user_cardinality(
                            cardinality,
                            answer.response.user,
                            value,
                            other_indicator,
                            group_by_letter_case,
                            group_by_slugify,
                            group_together,
                            filter,
                            standardized_filter,
                        )
        cardinality = self.filter_by_min_cardinality(cardinality, min_cardinality)
        if other_indicator is not None:
            self.__handle_other_indicator_cardinality(
                cardinality,
                filter,
                group_by_letter_case,
                group_by_slugify,
                group_together,
                other_indicator,
                standardized_filter,
            )
        return cardinality

    def filter_by_min_cardinality(self, cardinality, min_cardinality):
        if min_cardinality != 0:
            temp = {}
            for value in cardinality:
                if cardinality[value] < min_cardinality:
                    self._cardinality_plus_n(temp, "Other", cardinality[value])
                else:
                    temp[value] = cardinality[value]
            cardinality = temp
        return cardinality

    def __handle_other_indicator_cardinality(
        self,
        cardinality,
        filter,
        group_by_letter_case,
        group_by_slugify,
        group_together,
        other_indicator,
        standardized_filter,
    ):
        """Treating the value for Other question that were not answered in this question"""
        for indicator in other_indicator.opinion_indicators.all():
            for value in indicator.values:
                value = self.__get_cardinality_value(value, group_by_letter_case, group_by_slugify, group_together)
                if value not in filter + standardized_filter:
                    if indicator.response.user is None:
                        self._cardinality_plus_answer(cardinality, _(settings.USER_DID_NOT_ANSWER), value)

    def sorted_opinion_indicators_cardinality(
        self,
        min_cardinality=None,
        group_together=None,
        group_by_letter_case=None,
        group_by_slugify=None,
        filter=None,
        sort_answer=None,
        other_indicator=None,
    ):
        """Mostly to have reliable tests, but marginally nicer too...

        The ordering is reversed for same cardinality value so we have aa
        before zz."""
        cardinality = self.opinion_indicators_cardinality(
            min_cardinality, group_together, group_by_letter_case, group_by_slugify, filter, other_indicator
        )
        # We handle SortOpinionIndicator without enum because using "type" as a variable
        # name break the enum module and we want to use type in
        # answer_cardinality for simplicity
        possibles_values = [SortOpinionIndicator.ALPHANUMERIC, SortOpinionIndicator.CARDINAL, None]
        undefined = sort_answer is None
        user_defined = isinstance(sort_answer, dict)
        valid = user_defined or sort_answer in possibles_values
        if not valid:
            msg = "Unrecognized option '%s' for 'sort_answer': " % sort_answer
            msg += "use nothing, a dict (answer: rank),"
            for option in possibles_values:
                msg += " '{}', or".format(option)
            msg = msg[:-4]
            msg += ". We used the default cardinal sorting."
            logger.warning(msg)
        if undefined or not valid:
            sort_answer = SortOpinionIndicator.CARDINAL
        sorted_cardinality = None
        if user_defined:
            sorted_cardinality = sorted(list(cardinality.items()), key=lambda x: sort_answer.get(x[0], 0))
        elif sort_answer == SortOpinionIndicator.ALPHANUMERIC:
            sorted_cardinality = sorted(cardinality.items())
        elif sort_answer == SortOpinionIndicator.CARDINAL:
            if other_indicator is None:
                sorted_cardinality = sorted(list(cardinality.items()), key=lambda x: (-x[1], x[0]))
            else:
                # There is a dict instead of an int
                sorted_cardinality = sorted(list(cardinality.items()), key=lambda x: (-sum(x[1].values()), x[0]))
        return OrderedDict(sorted_cardinality)

    def _cardinality_plus_answer(self, cardinality, value, other_indicator_value):
        """The user answered 'value' to our question and
        'other_indicator_value' to the other question."""
        if cardinality.get(value) is None:
            cardinality[value] = {other_indicator_value: 1}
        elif isinstance(cardinality[value], int):
            # Previous answer did not had an answer to other question
            cardinality[value] = {_(settings.USER_DID_NOT_ANSWER): cardinality[value], other_indicator_value: 1}
        else:
            if cardinality[value].get(other_indicator_value) is None:
                cardinality[value][other_indicator_value] = 1
            else:
                cardinality[value][other_indicator_value] += 1

    def _cardinality_plus_n(self, cardinality, value, n):
        """We don't know what is the answer to other question but the
        user answered 'value'."""
        if cardinality.get(value) is None:
            cardinality[value] = n
        else:
            cardinality[value] += n

    def __get_cardinality_value(self, value, group_by_letter_case, group_by_slugify, group_together):
        """ Return the value we should use for cardinality. """
        value = Indicator.standardize(value, group_by_letter_case, group_by_slugify)
        for key, values in list(group_together.items()):
            grouped_values = Indicator.standardize_list(values, group_by_letter_case, group_by_slugify)
            if value in grouped_values:
                value = key
        return value

    def __add_user_cardinality(
        self,
        cardinality,
        user,
        value,
        other_indicator,
        group_by_letter_case,
        group_by_slugify,
        group_together,
        filter,
        standardized_filter,
    ):
        found_answer = False
        for other_opinion_indicator in other_indicator.opinion_indicators.all():
            if user is None:
                break
            if other_opinion_indicator.expertise_opinion.expert.person.user == user:
                # We suppose there is only a response per user
                # Why would you want this info if it is
                # possible to answer multiple time ?
                found_answer = True
                break
        if found_answer:
            values = other_opinion_indicator.values
        else:
            values = [_(settings.USER_DID_NOT_ANSWER)]
        for other_value in values:
            other_value = self.__get_cardinality_value(
                other_value, group_by_letter_case, group_by_slugify, group_together
            )
            if other_value not in filter + standardized_filter:
                self._cardinality_plus_answer(cardinality, value, other_value)

    def get_choices(self):
        """
        Parse the choices field and return a tuple formatted appropriately
        for the 'choices' argument of a form widget.
        """
        choices_list = []
        for choice in self.get_clean_choices():
            choices_list.append((slugify(choice, allow_unicode=True), choice))
        choices_tuple = tuple(choices_list)
        return choices_tuple

    def __str__(self):
        msg = "Показатель '{}' ".format(self.text)
        # if self.required:
        #     msg += "(*) "
        msg += "{}".format(self.get_clean_choices())
        return msg


class OpinionIndicator(repository_model.BaseModel):
    """
    Answer
    """
    indicator = auto_prefetch.ForeignKey(Indicator, on_delete=models.CASCADE, verbose_name='Показатель', related_name='opinion_indicators')
    expertise_opinion = auto_prefetch.ForeignKey('inspections.ExpertiseOpinion', on_delete=models.CASCADE, verbose_name='Экспертное заключение', related_name='opinion_indicators')
    created = models.DateTimeField(_('Creation date'), auto_now_add=True)
    updated = models.DateTimeField(_('Update date'), auto_now=True)
    body = models.TextField(_('Content'), blank=True, null=True)
    discipline = auto_prefetch.ForeignKey('repository.Subject', verbose_name='Дисциплина', on_delete=models.SET_NULL, null=True, blank=True)

    # @computed(models.JSONField(), depends=[['self', ['body']]])
    # def indicator(self):
    #     return next(indicator for indicator in indicators if indicator['title'] == self.question.text)

    def __init__(self, *args, **kwargs):
        try:
            indicator = Indicator.objects.get(pk=kwargs['indicator_id'])
        except KeyError:
            indicator = kwargs.get('indicator')
        body = kwargs.get('body')
        if indicator and body:
            self.check_opinion_indicator_body(indicator, body)
        super(OpinionIndicator, self).__init__(*args, **kwargs)

    @property
    def category(self):
        return self.indicator.category

    @property
    def values(self):
        if self.body is None:
            return [None]
        if len(self.body) < 3 or self.body[0:3] != "[u'":
            return [self.body]
        # We do not use eval for security reason but it could work with :
        # eval(self.body)
        # It would permit to inject code into answer though.
        values = []
        raw_values = self.body.split("', u'")
        nb_values = len(raw_values)
        for i, value in enumerate(raw_values):
            if i == 0:
                value = value[3:]
            if i + 1 == nb_values:
                value = value[:-2]
            values.append(value)
        return values

    def check_opinion_indicator_body(self, indicator, body):
        if indicator.type in [Indicator.RADIO, Indicator.SELECT, Indicator.SELECT_MULTIPLE]:
            choices = indicator.get_clean_choices()
            if body:
                if body[0] == "[":
                    opinions = []
                    for i, part in enumerate(body.split("'")):
                        if i % 2 == 1:
                            opinions.append(part)
                else:
                    opinions = [body]
            for opinion in opinions:
                if opinion not in choices:
                    msg = "Impossible opinion '{}'".format(body)
                    msg += " should be in {} ".format(choices)
                    raise ValidationError(msg)

    class Meta:
        verbose_name = 'показатель заключения'
        verbose_name_plural = 'показатели заключения'

    def __str__(self):
        return "{} to '{}' : '{}'".format(self.__class__.__name__, self.indicator, self.body)


class Request(repository_model.BaseModel):
    """
    Заявка на проведение экспертизы, ex-Expertise
    """
    # status
    NO_INIT = 'NO_INIT'
    SUB_APP = 'SUB_APP'
    ON_EXPERTISE = 'ON_EXPERTISE'
    ON_REVISION = 'ON_REVISION'
    ASSIGNED_STATUS = 'ASSIGNED_STATUS'
    NOT_ASSIGNED_STATUS = 'NOT_ASSIGNED_STATUS'

    STATUS_CHOICES = [
        (SUB_APP, 'подана заявка'),
        (ON_EXPERTISE, 'на экспертизе'),
        (ON_REVISION, 'на доработку'),
        (ASSIGNED_STATUS, 'присвоен статус'),
        (NOT_ASSIGNED_STATUS, 'не присвоен статус'),
    ]

    # type
    FULL = 'FULL'
    COMPLIANCE_DISCIPLINE = 'COMPLIANCE_DISCIPLINE'

    TYPE_EXPERTISE = [
        (FULL, 'Полная'),
        (COMPLIANCE_DISCIPLINE, 'На соответствие дисциплине'),
    ]

    # quality_category
    INNER = 'INNER'
    OUTER = 'OUTER'
    OUTSIDE = 'OUTSIDE'

    QUALITY_CATEGORIES = [
        (INNER, 'внутренний'),
        (OUTER, 'внешний'),
        (OUTSIDE, 'сторонний'),
    ]

    # interactive_category
    NOT_INTERACTIVE = 'NOT_INTERACTIVE'
    WITH_TEACHER_SUPPORT = 'WITH_TEACHER_SUPPORT'
    AUTO = 'AUTO'

    INTERACTIVE_CATEGORIES = [
        (NOT_INTERACTIVE, 'не интерактивный'),
        (WITH_TEACHER_SUPPORT, 'с поддержкой преподавателя'),
        (AUTO, 'автоматизированный'),
    ]

    digital_resource = auto_prefetch.ForeignKey(repository_model.DigitalResource, verbose_name="Паспорт ЭОР",
                                                on_delete=models.CASCADE)
    date = models.DateTimeField('Дата заявки', blank=True, null=True)
    subjects = models.ManyToManyField('repository.Subject', verbose_name='Дисциплина(ы)', blank=True)
    directions = models.ManyToManyField('repository.Direction', verbose_name='Направление подготовки', blank=True)
    digital_complexes = models.ManyToManyField('complexes.DigitalComplex', verbose_name='ЭУМК', blank=True)
    expert = models.ManyToManyField('users.Expert', verbose_name='Назначенные эксперты', blank=True)
    date_end = models.DateTimeField('Срок действия статуса экспертизы', blank=True, null=True)
    file = models.FileField(
        verbose_name='№ протокола комиссии по ресурсному обеспечению модулей и ЭО методического совета',
        upload_to='upload/files', null=True, blank=True)
    remarks = models.TextField('Замечания и рекомендации комиссии', blank=True)
    status = models.CharField('Состояние заявки', max_length=30, choices=STATUS_CHOICES,
                              default=NOT_ASSIGNED_STATUS)
    status_text = models.TextField('Статус', blank=True, null=True)
    type = models.CharField('Тип экспертизы', max_length=30, choices=TYPE_EXPERTISE, blank=True, null=True)

    # TODO: возможно нужны
    quality_category = models.CharField('Категория качества', max_length=30, choices=QUALITY_CATEGORIES, blank=True)
    interactive_category = models.CharField('Категория интерактивности', max_length=30, choices=INTERACTIVE_CATEGORIES,
                                            blank=True)
    owner = auto_prefetch.ForeignKey('users.Person', on_delete=models.PROTECT, related_name='owner_expertise',
                                     verbose_name='Инициатор', blank=True, null=True)

    @classmethod
    def get_count_request_assigned_status(cls):
        return cls.objects.filter(status='ASSIGNED_STATUS').count()

    @classmethod
    def get_request_assigned_status_assigned(cls, subjects_tags):
        objs = cls.objects.filter(status='ASSIGNED_STATUS', digital_resource__subjects_tags=subjects_tags)
        return objs

    @classmethod
    def get_request_assigned_status(cls):
        objs = cls.objects.filter(Q(status='ASSIGNED_STATUS') | Q(status='NOT_ASSIGNED_STATUS'), )
        return objs

    @classmethod
    def get_request_not_assigned_status(cls):
        objs = cls.objects.exclude(Q(status='ASSIGNED_STATUS') | Q(status='NOT_ASSIGNED_STATUS'), )
        return objs

    @classmethod
    def get_count_request_on_expertise(cls):
        return cls.objects.filter(status='ON_EXPERTISE').count()

    @classmethod
    def get_digital_resource_status(cls, digital_resource):
        return cls.objects.filter(digital_resource=digital_resource)

    @classmethod
    def get_expertise_mthd(cls, digital_resource):
        return cls.objects.filter(digital_resource=digital_resource)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return f"{self.get_status_display()} {self.digital_resource.title} {self.date} {self.owner}"

    def get_absolute_url(self):
        return reverse('inspections:inspections_Request_detail', args=(self.pk,))

    def get_absolute_url_digital_resource(self):
        return reverse('repository:repository_DigitalResource_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('inspections:inspections_Request_update', args=(self.pk,))

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        elif self.date is not None:
            self.date = None
        super(Request, self).save(*args, **kwargs)

    # choose type checklist
    # def get_checklists(self, type):
    #     return ExpertiseOpinion.objects.filter(expertise=self.pk, type=type)
    def get_expertise_opinion(self):
        return self.expertiseopinion_set.all()

    def get_expertise_opinions_ids(self):
        return self.expertiseopinion_set.all().values_list("pk")

    def get_temporary_status(self):
        return self.temporarystatus_set.all()

    def get_responses(self):
        responses = OpinionIndicator.objects.filter(expertise_opinion__in=self.get_expertise_opinions_ids()).order_by(
            'expertise_type', '-created').distinct('expertise_type')
        return responses

    def get_typed_responses(self):
        responses = self.get_responses()
        resp = dict()

        for resp_type in EXPERTISE_TYPES.keys():
            locals()[resp_type] = responses.filter(expertise_type__title=EXPERTISE_TYPES[resp_type])
            if locals()[resp_type].exists():
                locals()[resp_type] = locals()[resp_type].latest()
                resp[resp_type] = locals()[resp_type]
            else:
                resp[resp_type] = None
        return resp

    def get_checklists_self(self):
        return ExpertiseOpinion.objects.filter(request=self.pk)

    def get_expertise(self):
        expertise_pk = self.request.path.split('/')[5]
        expertise = Request.objects.get(pk=expertise_pk)
        return expertise

    def check_empty_queryset(self, type):
        if type == 'directions':
            queryset = repository_model.Direction.objects.all()
        elif type == 'subjects':
            queryset = repository_model.Subject.objects.all()
        elif type == 'digital_complexes':
            queryset = complex_model.DigitalComplex.objects.all()
        else:
            queryset = None

        if not queryset:
            return None
        else:
            return queryset

    def get_digital_resource(self, digital_resource_pk):
        return DigitalResource.objects.get(pk=digital_resource_pk)


class ExpertiseOpinion(repository_model.BaseModel):
    """
    Экспертное заключение, ex-Response
    """
    # status
    START = 'START'
    IN_PROCESS = 'IN_PROCESS'
    END = 'END'

    STATUS_CHOICES = [
        (START, 'Начата'),
        (IN_PROCESS, 'В процессе'),
        (END, 'Завершена')

    ]

    expert = auto_prefetch.ForeignKey('users.Expert', verbose_name='Эксперт', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата проведения экспертизы', blank=True, null=True)
    protocol = models.CharField('№ Протокола учебно-методического совета института', max_length=424, null=True,
                                blank=True)
    request = auto_prefetch.ForeignKey('inspections.Request', verbose_name='Заявка', on_delete=models.CASCADE, blank=True)
    status = models.CharField('Состояние', max_length=30, choices=STATUS_CHOICES, default=START, blank=True)

    expertise_type = auto_prefetch.ForeignKey(ExpertiseType, on_delete=models.PROTECT, verbose_name='Вид экспертизы', related_name='responses', null=True)

    class Meta:
        verbose_name = 'экспертное заключение'
        verbose_name_plural = 'экспертные заключения'

    def __str__(self):
        return f'{self.request} {self.status} {self.expertise_type}'

    def get_absolute_url(self):
        return reverse('inspections:inspections_ExpertiseOpinion_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('inspections:inspections_ExpertiseOpinion_update', args=(self.pk,))

    @classmethod
    def get_close_my_checklist(cls, user):
        objs = cls.objects.filter(Q(status='END') & Q(expert__person__user=user), )
        return objs

    @classmethod
    def get_my_checklist(cls, user):
        objs = cls.objects.filter(Q(status='IN_PROCESS') & Q(expert__person__user=user), )
        return objs

    @classmethod
    def get_active_my_checklist(cls):
        objs = cls.objects.exclude(
            # (Q(status='IN_PROCESS') | Q(status='START')) &
            # Q(status=cls.START) | Q(status=cls.END) |
            Q(expertise__status=Request.ASSIGNED_STATUS) | Q(expertise__status=Request.NOT_ASSIGNED_STATUS)
        )
        return objs

    @classmethod
    def get_checklists(cls, expertise):
        return cls.objects.filter(expertise=expertise)

    def get_request(self, request):
        try:
            return ExpertiseOpinion.objects.get(request=request).request
        except:
            return Request.objects.none()

    def get_dig_res(self, expertise):
        try:
            expertise = ExpertiseOpinion.objects.get(expertise=expertise).expertise
            dig_res = expertise.digital_resource
        except:
            dig_res = None
        return dig_res


# class Indicator(auto_prefetch.Model):
#     title = models.CharField(max_length=1024, db_index=True, unique=True)
#     group = auto_prefetch.ForeignKey("inspections.IndicatorGroup", on_delete=models.CASCADE)
#     values = ArrayField(
#         models.CharField(max_length=32, blank=True, null=True),
#         blank=True, null=True)
#     json_values = models.JSONField(blank=True, null=True)
#
#     num_values = IntegerRangeField(blank=True, null=True)
#     survey = models.ForeignKey("survey.Survey", null=True, on_delete=models.SET_NULL)
#     per_discipline = models.BooleanField("Для каждой дисциплины", default=False)
#     question = auto_prefetch.ForeignKey("survey.Question", null=True, blank=True, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "показатель"
#         verbose_name_plural = "показатели"
#         # ordering = ["order"]
#
#     def __str__(self):
#         return self.title
#
#     def bind_question(self):
#         qs = Question.objects.filter(text=self.title, survey=self.survey)
#         if qs.exists():
#             self.question = qs.first()
#             self.save()
#
#     def prefill_json_values(self, force=False):
#         if self.question and (not self.json_values or force):
#             l = list()
#             for i, v in enumerate(reversed(self.question.get_clean_choices())):
#                 l.append({
#                     "title": v,
#                     "value": i
#                 })
#                 self.json_values = l
#                 self.save()
#
#     def dict(self):
#         d = Dict(model_to_dict(self))
#         d.question = Dict(model_to_dict(Question.objects.get(pk=d.question)))
#         return d
#
#     def get_value(self, title):
#         if self.question.per_discipline and not self.question.discipline:
#             return None
#         if self.question.type == "integer":
#             return int(title)
#         if not self.json_values:
#             return None
#         for pair in self.json_values:
#             if pair.get('title', None) == title:
#                 return pair.get('value', None)
#         return None


class StatusRequirement(auto_prefetch.Model):
    indicator = auto_prefetch.ForeignKey('inspections.Indicator', verbose_name='Показатель', on_delete=models.CASCADE)
    allowed_values = ArrayField(models.CharField(max_length=32, blank=True, null=True),
                                verbose_name='Допустимые значения', blank=True, null=True)
    allowed_num_values = IntegerRangeField(verbose_name='Диапазон допустимых числовых значений', blank=True,
                                           null=True)  # null - нет, 0 - любое
    exclude_values = ArrayField(models.CharField(max_length=32, blank=True, null=True),
                                verbose_name='Исключаемые значения', blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name='Используется')
    status = auto_prefetch.ForeignKey('Status', on_delete=models.CASCADE, related_name='requirements')

    def __str__(self):
        return self.indicator.category.title

    def is_ok(self, value):
        if not value:
            return False

        values_is_ok, range_is_ok, not_exclude = False, False, False
        if self.allowed_values:
            values_is_ok = value in self.allowed_values
        else:
            values_is_ok = True
        if self.allowed_num_values:
            range_is_ok = self.allowed_num_values.lower <= value <= self.allowed_num_values.upper
        else:
            range_is_ok = True
        if self.exclude_values:
            not_exclude = value not in self.exclude_values
        else:
            not_exclude = True

        return all([values_is_ok, range_is_ok, not_exclude])


class Status(models.Model):
    GROUPS = (
        ('qual', 'Категория качества контента ЭОР'),
        ('struct', 'Соответствие структуры и содержания ЭОР требованиям конкретных дисциплин ОП'),
        ('tech', 'Технологические возможности и сценарии функционирования ЭОР')
    )
    title = models.CharField('Наименование', max_length=1024, db_index=True)
    group = models.CharField('Группа', max_length=6, choices=GROUPS, default='qual')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        reqs = StatusRequirement.objects.filter(status=self).order_by('id')
        empty_indicators = Indicator.objects.exclude(statusrequirement__in=reqs)

        for indicator in empty_indicators:
            StatusRequirement.objects.create(
                status=self,
                indicator=indicator
            )


class TemporaryStatus(models.Model):
    request = models.ForeignKey('Request', verbose_name='Заявка', null=True, blank=True,
                                on_delete=models.CASCADE)
    name = models.TextField('Тело статуса', blank=True, null=True)
    date = models.DateTimeField('Дата выставления статуса', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.date.strftime('%d.%m.%Y')})"

    class Meta:
        verbose_name = 'временный статус'
        verbose_name_plural = 'временные статусы'

    @classmethod
    def get_temporary_status(cls, request):
        if request:
            return cls.objects.filter(request=request)
        return None


class AcceptableIndicatorValue(repository_model.BaseModel):
    """
    Код показателя
    o Значение показателя
    o КУРС_ЭОР
    o Внеш_Внутр
    o Авт_Неинтер_Преп
    o Полн_Част
    o Рейтинг

    ENTITY_TYPES = (
        ("course", "курс"),
        ("eor", "ЭОР")
    )
    LOCATION_TYPES = (
        ("external", "внешний"),
        ("internal", "внутренний")
    )
    INTERACTION_TYPES = (
        ('automated', 'Автоматизированный'),
        ('non-interactive', 'Не интерактивный'),
        ('teacher', 'С участием преподавателя')
    )
    COMPLIANCE_LEVELS = (
        ('full', 'Полностью соответствует содержанию и результатам обучения дисциплины'),
        ('partly', 'Частично соответствует содержанию и результатам обучения дисциплины')
    )
    """

    indicator = auto_prefetch.ForeignKey('inspections.Indicator', verbose_name='Показатель', on_delete=models.CASCADE)
    value = models.CharField('Значение показателя', max_length=256, null=True, blank=True)
    entity = models.PositiveSmallIntegerField('КУРС_ЭОР', null=True, blank=True)
    location = models.PositiveSmallIntegerField('Внеш_Внутр', null=True, blank=True)
    interaction = models.PositiveSmallIntegerField('Тип интерактивности (Автоматизированный/Не интерактивный/С участием преподавателя)', null=True, blank=True)
    compliance = models.PositiveSmallIntegerField('Соответствие содержанию дисциплины (Полностью/Частично)', null=True, blank=True)
    per_discipline = models.BooleanField('Для каждой дисциплины', default=False)
    rating = models.DecimalField('Рейтинг', decimal_places=3, max_digits=4, null=True, blank=True)

    class Meta:
        verbose_name = 'допустимое значение показателя'
        verbose_name_plural = 'допустимые значения показателя'


class SummaryIndicator(repository_model.BaseModel):
    """
    Код заявки
    Код показателя
    КУРС_ЭОРo
    Внеш_Внутр
    Авт_Неинтер_Преп
    Полн_Част
    Дисциплина
    Образовательная программа
    Рейтинг
    Имеются противоречия
    """
    request = auto_prefetch.ForeignKey('inspections.Request', verbose_name='Заявка', on_delete=models.PROTECT)
    indicator = auto_prefetch.ForeignKey('inspections.Indicator', verbose_name='Показатель', on_delete=models.CASCADE)
    entity = models.PositiveSmallIntegerField('КУРС_ЭОР', null=True, blank=True)
    location = models.PositiveSmallIntegerField('Внеш_Внутр', null=True, blank=True)
    interaction = models.PositiveSmallIntegerField('Тип интерактивности (Автоматизированный/Не интерактивный/С участием преподавателя)', null=True, blank=True)
    compliance = models.PositiveSmallIntegerField('Соответствие содержанию дисциплины (Полностью/Частично)', null=True, blank=True)
    per_discipline = models.BooleanField('Для каждой дисциплины', default=False)
    rating = models.DecimalField('Рейтинг', decimal_places=3, max_digits=4, null=True, blank=True)
    have_conflicts = models.BooleanField('Имеются противоречия', default=False)

    class Meta:
        verbose_name = 'сводный показатель'
        verbose_name_plural = 'сводные показатели'
