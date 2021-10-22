# -*- coding: utf-8 -*-
import logging

import auto_prefetch
from addict import Dict
from django.conf import settings
from django.contrib.postgres.fields import IntegerRangeField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.forms.models import model_to_dict
from django.urls import reverse
from django.utils import timezone
from django_better_admin_arrayfield.models.fields import ArrayField

from lrr.complexes import models as complex_model
from lrr.repository import models as repository_model
from lrr.repository.models import DigitalResource
from lrr.survey.models.question import Question
from lrr.survey.models.response import Response as SurveyResponse
from lrr.users.models import Person, Expert

logger = logging.getLogger(__name__)

CHOICES_HELP_TEXT = (
    """Поле выбора используется только в том случае, если тип вопроса
если тип вопроса - "радио", "выбор" или
'select multiple' - список разделенных запятыми
варианты этого вопроса ."""
)

EXPERTISE_TYPES = {
    "methodical": "Методическая экспертиза",
    "contental": "Содержательная экспертиза",
    "technical": "Техническая экспертиза"
}


def validate_choices(choices):
    """  Verifies that there is at least two choices in choices
    :param String choices: The string representing the user choices.
    """
    values = choices.split(settings.CHOICES_SEPARATOR)
    empty = 0
    for value in values:
        if value.replace(" ", "") == "":
            empty += 1
    if len(values) < 2 + empty:
        msg = "The selected field requires an associated list of choices."
        msg += " Choices must contain more than one item."
        raise ValidationError(msg)


class Expertise(repository_model.BaseModel):
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
    date = models.DateTimeField("Дата заявки", blank=True, null=True)
    subjects = models.ManyToManyField("repository.Subject", verbose_name="Дисциплина(ы)", blank=True)
    directions = models.ManyToManyField("repository.Direction", verbose_name="Направление подготовки", blank=True)
    digital_complexes = models.ManyToManyField("complexes.DigitalComplex", verbose_name="ЭУМК", blank=True)
    expert = models.ManyToManyField("users.Expert", verbose_name="Назначенные эксперты", blank=True)
    date_end = models.DateTimeField("Срок действия статуса экспертизы", blank=True, null=True)
    file = models.FileField(
        verbose_name="№ протокола комиссии по ресурсному обеспечению модулей и ЭО методического совета",
        upload_to="upload/files", null=True, blank=True)
    remarks = models.TextField("Замечания и рекомендации комиссии", blank=True)
    status = models.CharField("Состояние экспертизы", max_length=30, choices=STATUS_CHOICES,
                              default=NOT_ASSIGNED_STATUS)
    type = models.CharField("Тип экспертизы", max_length=30, choices=TYPE_EXPERTISE, blank=True, null=True)

    # TODO: возможно нужны
    quality_category = models.CharField("Категория качества", max_length=30, choices=QUALITY_CATEGORIES, blank=True)
    interactive_category = models.CharField("Категория интерактивности", max_length=30, choices=INTERACTIVE_CATEGORIES,
                                            blank=True)
    owner = auto_prefetch.ForeignKey("users.Person", on_delete=models.PROTECT, related_name="owner_expertise",
                                     verbose_name="Инициатор", blank=True, null=True)

    @classmethod
    def get_count_expertise_assigned_status(cls):
        return cls.objects.filter(status='ASSIGNED_STATUS').count()

    @classmethod
    def get_expertise_assigned_status_assigned(cls, subjects_tags):
        try:
            objs = cls.objects.filter(status='ASSIGNED_STATUS', digital_resource__subjects_tags=subjects_tags)
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_expertise_assigned_status(cls):
        try:
            objs = cls.objects.filter(Q(status='ASSIGNED_STATUS') | Q(status='NOT_ASSIGNED_STATUS'), )
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_expertise_not_assigned_status(cls):
        try:
            objs = cls.objects.exclude(Q(status='ASSIGNED_STATUS') | Q(status='NOT_ASSIGNED_STATUS'), )
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_count_expertise_on_expertise(cls):
        return cls.objects.filter(status='ON_EXPERTISE').count()

    @classmethod
    def get_digital_resource_status(cls, digital_resource):
        return cls.objects.filter(digital_resource=digital_resource)

    @classmethod
    def get_expertise_mthd(cls, digital_resource):
        try:
            cls.objects.filter(digital_resource=digital_resource)
        except:
            return cls.objects.none()

    class Meta:
        verbose_name = "экспертиза"
        verbose_name_plural = "экспертизы"

    def __str__(self):
        return f"{self.get_status_display()} {self.digital_resource.title} {self.date} {self.owner}"

    def get_absolute_url(self):
        return reverse("inspections:inspections_Expertise_detail", args=(self.pk,))

    def get_absolute_url_digital_resource(self):
        return reverse("repository:repository_DigitalResource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("inspections:inspections_Expertise_update", args=(self.pk,))

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        elif self.date is not None:
            self.date = None
        super(Expertise, self).save(*args, **kwargs)

    # choose type checklist
    # def get_checklists(self, type):
    #     return ExpertiseRequest.objects.filter(expertise=self.pk, type=type)
    def get_expertise_request(self):
        return self.expertiserequest_set.all()

    def get_expertise_requests_ids(self):
        return self.expertiserequest_set.all().values_list("pk")

    def get_temporary_status(self):
        return self.temporarystatus_set.all()

    def get_responses(self):
        responses = SurveyResponse.objects.filter(expertise_request__in=self.get_expertise_requests_ids()).order_by(
            "survey", "-created").distinct("survey")
        return responses

    def get_typed_responses(self):
        responses = self.get_responses()
        resp = dict()

        for resp_type in EXPERTISE_TYPES.keys():
            locals()[resp_type] = responses.filter(survey__name=EXPERTISE_TYPES[resp_type])
            if locals()[resp_type].exists():
                locals()[resp_type] = locals()[resp_type].latest()
                resp[resp_type] = locals()[resp_type]
            else:
                resp[resp_type] = None
        return resp

    def get_checklists_self(self):
        return ExpertiseRequest.objects.filter(expertise=self.pk)

    def get_expertise(self):
        expertise_pk = self.request.path.split('/')[5]
        expertise = Expertise.objects.get(pk=expertise_pk)
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

    @staticmethod
    def get_digital_resource(digital_resource_pk):
        return DigitalResource.objects.get(pk=digital_resource_pk)


class ExpertiseRequest(repository_model.BaseModel):
    # type
    METHODICAL = 'METHODICAL'
    CONTENT = 'CONTENT'
    TECH = 'TECH'
    NO_TYPE = 'NO_TYPE'

    TYPE_CHOICES = [
        (METHODICAL, 'Методическая'),
        (CONTENT, 'Содержательная'),
        (TECH, 'Техническая'),
        (NO_TYPE, 'Отсутствует тип экспертизы')

    ]

    # status
    START = 'START'
    IN_PROCESS = 'IN_PROCESS'
    END = 'END'

    STATUS_CHOICES = [
        (START, 'В процессе'),
        (IN_PROCESS, 'В процессе'),
        (END, 'Завершена')

    ]

    type = models.CharField("Тип заявки", max_length=30, choices=TYPE_CHOICES, default=NO_TYPE, null=True,
                            blank=True)
    expert = auto_prefetch.ForeignKey("users.Expert", verbose_name="Эксперт", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField("Дата проведения экспертизы", blank=True, null=True)
    protocol = models.CharField("№ Протокола учебно-методического совета института", max_length=424, null=True,
                                blank=True)
    expertise = auto_prefetch.ForeignKey("inspections.Expertise", verbose_name="Экспертиза", on_delete=models.CASCADE, blank=True)
    status = models.CharField("Состояние", max_length=30, choices=STATUS_CHOICES, default=START, blank=True)
    survey = auto_prefetch.ForeignKey('survey.Survey', verbose_name="Опросник", on_delete=models.PROTECT, blank=True,
                                      null=True)

    class Meta:
        verbose_name = "эаявка"
        verbose_name_plural = "эаявка"

    def __str__(self):
        return f"{self.expertise} {self.status} {self.survey}"

    def get_absolute_url(self):
        return reverse("inspections:inspections_ExpertiseRequest_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("inspections:inspections_ExpertiseRequest_update", args=(self.pk,))

    @classmethod
    def get_close_my_checklist(cls, user):
        try:
            objs = cls.objects.filter(Q(status='END') & Q(expert__person__user=user), )
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_my_checklist(cls, user):
        try:
            objs = cls.objects.filter(Q(status='IN_PROCESS') & Q(expert__person__user=user), )
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_active_my_checklist(cls):
        try:
            objs = cls.objects.exclude(Q(status='IN_PROCESS') & Q(status='START'))
        except:
            objs = cls.objects.all()
        return objs

    @classmethod
    def get_checklists(cls, expertise):
        return cls.objects.filter(expertise=expertise)

    def get_expertise(self, expertise):
        try:
            return ExpertiseRequest.objects.get(expertise=expertise).expertise
        except:
            return None

    def get_dig_res(self, expertise):
        try:
            expertise = ExpertiseRequest.objects.get(expertise=expertise).expertise
            dig_res = expertise.digital_resource
        except:
            dig_res = None
        return dig_res


class IndicatorGroup(models.Model):
    GROUPS = (
        ("0", "Кадровый состав авторского коллектива (Соблюдение квалификационных требований)"),
        ("1", "Полнота заполнения полей паспорта ресурса"),
        ("2", "Редакционно-издательская обработка"),
        ("3", "Соблюдение требований в области защиты авторских прав"),
        ("4", "Соответствие требованиям к оценочным материалам"),
        ("5", "Состав применяемых технологий"),
        ("6", "Управление учебной деятельностью"),
        ("7", "Соблюдение требований в области защиты авторских прав"),
        ("8", "Соответствие требованиям к оценочным материалам"),
        ("9", "Соответствие содержанию дисциплины ОП"),
        ("10", "Соответствие требованиям к контенту"),
        ("11", "Дизайн-эргономические и технические характеристики используемых средств обучения"),
        ("12", "Доступ к ресурсу"),
        ("13", "Соответствие требованиям к структуре ресурса")
    )
    title = models.CharField(max_length=1024, choices=GROUPS, default="0", unique=True)

    class Meta:
        verbose_name = "группа показателей"
        verbose_name_plural = "группы показателей"

    def __str__(self):
        return self.get_title_display()


class Indicator(auto_prefetch.Model):
    title = models.CharField(max_length=1024, db_index=True, unique=True)
    group = auto_prefetch.ForeignKey("inspections.IndicatorGroup", on_delete=models.CASCADE)
    values = ArrayField(
        models.CharField(max_length=32, blank=True, null=True),
        blank=True, null=True)
    json_values = models.JSONField(blank=True, null=True)

    num_values = IntegerRangeField(blank=True, null=True)
    survey = models.ForeignKey("survey.Survey", null=True, on_delete=models.SET_NULL)
    per_discipline = models.BooleanField("Для каждой дисциплины", default=False)
    question = auto_prefetch.ForeignKey("survey.Question", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "показатель"
        verbose_name_plural = "показатели"
        # ordering = ["order"]

    def __str__(self):
        return self.title

    def bind_question(self):
        qs = Question.objects.filter(text=self.title, survey=self.survey)
        if qs.exists():
            self.question = qs.first()
            self.save()

    def prefill_json_values(self, force=False):
        if self.question and (not self.json_values or force):
            l = list()
            for i, v in enumerate(reversed(self.question.get_clean_choices())):
                l.append({
                    "title": v,
                    "value": i
                })
                self.json_values = l
                self.save()

    def dict(self):
        d = Dict(model_to_dict(self))
        d.question = Dict(model_to_dict(Question.objects.get(pk=d.question)))
        return d

    def get_value(self, title):
        if self.question.per_discipline and not self.question.discipline:
            return None
        if self.question.type == "integer":
            return int(title)
        if not self.json_values:
            return None
        for pair in self.json_values:
            if pair.get('title', None) == title:
                return pair.get('value', None)
        return None


class StatusRequirement(auto_prefetch.Model):
    indicator = auto_prefetch.ForeignKey("inspections.Indicator", verbose_name="Показатель", on_delete=models.CASCADE)
    allowed_values = ArrayField(models.CharField(max_length=32, blank=True, null=True),
                                verbose_name="Допустимые значения", blank=True, null=True)
    allowed_num_values = IntegerRangeField(verbose_name="Диапазон допустимых числовых значений", blank=True,
                                           null=True)  # null - нет, 0 - любое
    exclude_values = ArrayField(models.CharField(max_length=32, blank=True, null=True),
                                verbose_name="Исключаемые значения", blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name="Используется")
    status = auto_prefetch.ForeignKey("Status", on_delete=models.CASCADE, related_name="requirements")

    def __str__(self):
        return self.indicator.group.get_title_display()

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
        ("qual", "Категория качества контента ЭОР"),
        ("struct", "Соответствие структуры и содержания ЭОР требованиям конкретных дисциплин ОП"),
        ("tech", "Технологические возможности и сценарии функционирования ЭОР")
    )
    title = models.CharField("Наименование", max_length=1024, db_index=True)
    group = models.CharField("Группа", max_length=6, choices=GROUPS, default="qual")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        reqs = StatusRequirement.objects.filter(status=self).order_by("id")
        empty_indicators = Indicator.objects.exclude(statusrequirement__in=reqs)

        for indicator in empty_indicators:
            StatusRequirement.objects.create(
                status=self,
                indicator=indicator
            )


class TemporaryStatus(models.Model):
    expertise = models.ForeignKey("Expertise", verbose_name="Экспертиза", null=True, blank=True,
                                  on_delete=models.CASCADE)
    name = models.TextField("Тело статуса", blank=True, null=True)
    date = models.DateTimeField("Дата выставления статуса", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.date.strftime('%d.%m.%Y')})"

    class Meta:
        verbose_name = "временный статус"
        verbose_name_plural = "временные статусы"

    @classmethod
    def get_temporary_status(cls, expertise):
        if expertise:
            return cls.objects.filter(expertise=expertise)
        return None
