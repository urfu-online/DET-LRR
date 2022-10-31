import logging
import uuid
from copy import deepcopy

from django import forms
from django.conf import settings
from django.urls import reverse
from django_select2 import forms as s2forms

from lrr.inspections import models as inspections_models
from lrr.users.models import Expert
from lrr.utils import slugify
from .models import Indicator, ExpertiseRequest, Category, OpinionIndicator, ExpertiseOpinion
from .signals import survey_completed
from .widgets import ImageSelectWidget

logger = logging.getLogger(__name__)


class DirectionsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class SubjectsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class DigitalComplexesWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "keywords__icontains",
        "format__icontains"
    ]
    max_results = 50


class ExpertiseRequestCreateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "type",
            "subjects",
            "directions",
            "digital_complexes",
            "expert",
            "file",
            "remarks",
        ]
        widgets = {
            "subjects": SubjectsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "directions": DirectionsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "digital_complexes": DigitalComplexesWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            # 'digital_resource': forms.MultipleChoiceField(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',

                }
            ),
            'expert': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }
            ),
            # 'date_end': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required': 'true'
            #     }
            # ),
            # 'remarks': forms.Textarea(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }
        exclude = ['status', 'date', "digital_resource", ]


class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            # "digital_resource",
            # "subjects",
            # "directions",
            # "digital_complexes",
            # "expert",
            "status_text",
            "file",
            "remarks",
            "date_end"
        ]
        widgets = {
            # 'digital_resource': forms.MultipleChoiceField(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',

                }
            ),
            # 'subjects': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #
            #     },
            # ),
            # 'directions': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            # 'digital_complexes': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            # 'expert': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            'date_end': forms.DateTimeInput(

                format="%d/%m/%Y %H:%M",
                attrs={
                    'class': 'datetimepicker form-control',
                    'required': 'true',
                    'placeholder': "DD/MM/YYYY HH:MM"

                }
            ),
            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',

                }
            ),
            'status_text': forms.Textarea(
                attrs={
                    'class': 'form-control',

                }
            ),
            # 'type': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # )
        }
        exclude = ['status', 'date']


class ExpertiseTypeWidget(s2forms.Select2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class ExpertWidget(s2forms.Select2Widget):
    search_fields = [
        "person__first_name__icontains",
        "person__middle_name__icontains",
        "person__last_name__icontains",
        "subdivision__icontains",
    ]
    max_results = 50


class ExpertiseOpinionCreateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseOpinion
        fields = [
            "expertise_type",
            "expert",
        ]
        exclude = ["expertise_request", "date", "protocol", "status"],
        widgets = {
            'expertise_type': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            'expert': ExpertWidget(
                attrs={
                    'class': 'form-control',

                }
            ),
        }


class ExpertiseOpinionUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseOpinion
        fields = [
            "expert",
            "date",
            "protocol",
            "status",
            "expertise_request",
            "expertise_type"
        ]
        widgets = {
            'expertise_type': forms.Select(
                attrs={
                    'class': 'form-select',

                }
            )
        }


class IndicatorWidget(s2forms.Select2Widget):
    search_fields = ["category__title"]
    max_results = 5


class ExpertiseOpinionForm(forms.ModelForm):
    FIELDS = {
        Indicator.TEXT: forms.CharField,
        Indicator.SHORT_TEXT: forms.CharField,
        Indicator.SELECT_MULTIPLE: forms.MultipleChoiceField,
        Indicator.INTEGER: forms.IntegerField,
        Indicator.FLOAT: forms.FloatField,
        Indicator.DATE: forms.DateField,
    }

    WIDGETS = {
        Indicator.TEXT: forms.Textarea,
        Indicator.SHORT_TEXT: forms.TextInput,
        Indicator.RADIO: forms.RadioSelect,
        Indicator.SELECT: forms.Select,
        Indicator.SELECT_IMAGE: ImageSelectWidget,
        Indicator.SELECT_MULTIPLE: forms.CheckboxSelectMultiple,
    }

    class Meta:
        model = ExpertiseOpinion
        fields = ()

    def __init__(self, *args, **kwargs):
        """ Expects expertise_type object to be passed in initially """
        self.expertise_type = kwargs.pop("expertise_type")
        self.expert = kwargs.pop("expert")
        self.expertise_request = kwargs.pop("expertise_request")
        try:
            self.step = int(kwargs.pop("step"))
        except KeyError:
            self.step = None
        super(ExpertiseOpinionForm, self).__init__(*args, **kwargs)
        self.uuid = uuid.uuid4().hex

        self.categories = self.expertise_type.non_empty_categories()
        self.qs_with_no_cat = self.expertise_type.indicators.filter(category__isnull=True).order_by("order", "id")

        # if self.expertise_type.display_method == ExpertiseType.BY_CATEGORY:
        self.steps_count = len(self.categories) + (1 if self.qs_with_no_cat else 0)
        # else:
        #     self.steps_count = len(self.expertise_type.indicators.all())
        # will contain prefetched data to avoid multiple db calls
        self.response = False
        self.opinion_indicators = False

        self.add_indicators(kwargs.get("data"))

        self._get_preexisting_response()

        if self.response is not None:
            for name in self.fields.keys():
                self.fields[name].values = None

        # if not self.expertise_type.editable_answers and self.response is not None:
        #     for name in self.fields.keys():
        #         self.fields[name].widget.attrs["disabled"] = True
        for name in self.fields.keys():
            self.fields[name].widget.attrs["class"] = "form-control"

    def add_indicators(self, data):
        # add a field for each expertise_type indicator, corresponding to the indicator
        # type as appropriate.

        # if self.expertise_type.display_method == ExpertiseType.BY_CATEGORY and self.step is not None:
        #     if self.step == len(self.categories):
        #         qs_for_step = self.expertise_type.indicators.filter(category__isnull=True).order_by("order", "id")
        #     else:
        #         qs_for_step = self.expertise_type.indicators.filter(category=self.categories[self.step])
        #
        #     for indicator qs_for_step:
        #         self.add_indicator(indicator, data)
        # else:

        disciplines = self.expertise_request.subjects.all()
        per_discipline_indicator_count = self.expertise_type.indicators.filter(per_discipline=True).count()

        for i, indicator in enumerate(self.expertise_type.indicators.all()):
            # not_to_keep = i != self.step and self.step is not None
            # if self.expertise_type.display_method == ExpertiseType.BY_QUESTION and not_to_keep:
            #     continue
            if indicator.is_group_indicator():
                for discipline in disciplines:
                    if not Indicator.objects.filter(parent=indicator, discipline=discipline).exists():
                        subquestion = deepcopy(indicator)
                        subquestion.pk = None
                        subquestion.per_discipline = False
                        subquestion.discipline = discipline
                        subquestion.parent = indicator
                        subquestion.save()
                        self.add_indicator(subquestion, data)
            else:
                self.add_indicator(indicator, data)

    def current_categories(self):
        # if self.expertise_type.display_method == ExpertiseType.BY_CATEGORY:
        if self.step is not None and self.step < len(self.categories):
            return [self.categories[self.step]]
        return [Category(title="Без категории")]
        # else:
        #     extras = []
        #     if self.qs_with_no_cat:
        #         extras = [Category(title="Без категории", description="")]

        # return self.categories + extras

    def _get_preexisting_response(self):
        """Recover a pre-existing response in database.

        The user must be logged. Will store the response retrieved in an attribute
        to avoid multiple db calls.

        :rtype: Response or None
        """
        if self.response:
            return self.response

        if not self.expert.get_user().is_authenticated:
            self.response = None
        else:
            # expert = Expert.get_expert(self.user)
            try:
                self.response = ExpertiseOpinion.objects.prefetch_related("expert", "expertise_type", "expertise_request").filter(
                    expert=self.expert, expertise_type=self.expertise_type, expertise_request=self.expertise_request
                ).latest()
            except ExpertiseRequest.DoesNotExist:
                logger.debug(f"No saved response for {self.expertise_type} for expert {self.expert}")
                self.response = None
        return self.response

    def _get_preexisting_opinion_indicators(self):
        """Recover pre-existing opinion_indicators in database.

        The user must be logged. A Response containing the Answer must exist.
        Will create an attribute containing the opinion_indicators retrieved to avoid multiple
        db calls.

        :rtype: dict of Answer or None
        """
        if self.opinion_indicators:
            return self.opinion_indicators

        request = self._get_preexisting_response()
        if request is None:
            self.opinion_indicators = None
        try:
            opinion_indicators = OpinionIndicator.objects.filter(request=request).prefetch_related("indicator")
            self.opinion_indicators = {opinion_indicator.indicator.id: opinion_indicator for opinion_indicator in opinion_indicators.all()}
        except OpinionIndicator.DoesNotExist:
            self.opinion_indicators = None

        return self.opinion_indicators

    def _get_preexisting_opinion_indicator(self, indicator):
        """Recover a pre-existing opinion_indicator in database.

        The user must be logged. A Response containing the Answer must exist.

        :param Indicator indicator: The indicator we want to recover in the
        response.
        :rtype: Answer or None"""
        opinion_indicators = self._get_preexisting_opinion_indicators()
        return opinion_indicators.get(indicator.id, None)

    def get_indicator_initial(self, indicator, data):
        """Get the initial value that we should use in the Form

        :param Indicator indicator: The indicator
        :param dict data: Value from a POST request.
        :rtype: String or None"""
        initial = None
        opinion_indicator = self._get_preexisting_opinion_indicator(indicator)
        if opinion_indicator:
            # Initialize the field with values from the database if any
            if indicator.type == Indicator.SELECT_MULTIPLE:
                initial = []
                if opinion_indicator.body == "[]":
                    pass
                elif "[" in opinion_indicator.body and "]" in opinion_indicator.body:
                    initial = []
                    unformated_choices = opinion_indicator.body[1:-1].strip()
                    for unformated_choice in unformated_choices.split(settings.CHOICES_SEPARATOR):
                        choice = unformated_choice.split("'")[1]
                        initial.append(slugify(choice))
                else:
                    # Only one element
                    initial.append(slugify(opinion_indicator.body))
            else:
                initial = opinion_indicator.body
        if data:
            # Initialize the field field from a POST request, if any.
            # Replace values from the database
            initial = data.get("indicator_%d" % indicator.pk)
        return initial

    def get_indicator_widget(self, indicator):
        """Return the widget we should use for indicator.

        :param Indicator indicator: The indicator
        :rtype: django.forms.widget or None"""
        try:
            return self.WIDGETS[indicator.type]
        except KeyError:
            return None

    @staticmethod
    def get_indicator_choices(indicator):
        """Return the choices we should use for indicator.

        :param Indicator indicator: The indicator
        :rtype: List of String or None"""
        qchoices = None
        if indicator.type not in [Indicator.TEXT, Indicator.SHORT_TEXT, Indicator.INTEGER, Indicator.FLOAT, Indicator.DATE]:
            qchoices = indicator.get_choices()
            # add an empty option at the top so that the user has to explicitly
            # select one of the options
            if indicator.type in [Indicator.SELECT, Indicator.SELECT_IMAGE]:
                qchoices = tuple([("", "-------------")]) + qchoices
        return qchoices

    def get_indicator_field(self, indicator, **kwargs):
        """Return the field we should use in our form.

        :param Indicator indicator: The indicator
        :param **kwargs: A dict of parameter properly initialized in
            add_indicator.
        :rtype: django.forms.fields"""
        # logging.debug("Args passed to field %s", kwargs)
        try:
            return self.FIELDS[indicator.type](**kwargs)
        except KeyError:
            return forms.ChoiceField(**kwargs)

    def add_indicator(self, indicator, data):
        """Add indicator to the form.

        :param Indicator indicator: The indicator to add.
        :param dict data: The pre-existing values from a post request."""
        kwargs = {"label": indicator.text}  # , "required": indicator.required
        initial = self.get_indicator_initial(indicator, data)
        if initial:
            kwargs["initial"] = initial
        choices = self.get_indicator_choices(indicator)
        if choices:
            kwargs["choices"] = choices
        widget = self.get_indicator_widget(indicator)
        if widget:
            kwargs["widget"] = widget
        field = self.get_indicator_field(indicator, **kwargs)
        field.widget.attrs["category"] = indicator.category.title if indicator.category else ""

        if indicator.type == Indicator.DATE:
            field.widget.attrs["class"] = "date"
        # logging.debug("Field for %s : %s", indicator, field.__dict__)
        self.fields["indicator_%d" % indicator.pk] = field

    def has_next_step(self):
        if not self.expertise_type.is_all_in_one_page():
            if self.step < self.steps_count - 1:
                return True
        return False

    def next_step_url(self):
        if self.has_next_step():
            context = {"id": self.expertise_type.id, "step": self.step + 1}
            return reverse("expertise_type:expertise_type-detail-step", kwargs=context)

    def current_step_url(self):
        return reverse("expertise_type:expertise_type-detail-step", kwargs={"id": self.expertise_type.id, "step": self.step})

    @staticmethod
    def save_status(opinion_indicator, indicator, expertise_type):
        if expertise_type.is_methodic():
            pass
        if expertise_type.is_content():
            pass
        if expertise_type.is_tech():
            pass

    def save(self, commit=True):
        response = self._get_preexisting_response()

        # TODO check opinion_indicator and set status.
        response = super(ExpertiseOpinionForm, self).save(commit=False)
        response.expertise_type = self.expertise_type
        response.expertise_opinion = self.expertise_opinion
        response.id = self.uuid
        if self.user.is_authenticated:
            response.expert = Expert.get_expert(self.user)
        response.save()
        # response "raw" data as dict (for signal)
        data = {"expertise_type": response.expertise_type.id, "id": response.id, "responses": []}
        # create an opinion_indicator object for each indicator and associate it with this
        # response.
        for field_name, field_value in list(self.cleaned_data.items()):
            if field_name.startswith("indicator_"):
                # warning: this way of extracting the id is very fragile and
                # entirely dependent on the way the indicator_id is encoded in
                # the field name in the __init__ method of this form class.
                q_id = int(field_name.split("_")[1])
                indicator = Indicator.objects.get(pk=q_id)
                opinion_indicator = self._get_preexisting_opinion_indicator(indicator)
                if opinion_indicator is None:
                    opinion_indicator = OpinionIndicator(indicator=indicator)
                if indicator.type == Indicator.SELECT_IMAGE:
                    value, img_src = field_value.split(":", 1)
                    # TODO Handling of SELECT IMAGE
                    logger.debug("Indicator.SELECT_IMAGE not implemented, please use : %s and %s", value, img_src)
                indicator.body = field_value
                data["responses"].append((opinion_indicator.indicator.id, opinion_indicator.body))
                logger.debug("Creating opinion_indicator for indicator %d of type %s : %s", q_id, opinion_indicator.indicator.type, field_value)
                indicator.expertise_opinion = response
                self.save_status(opinion_indicator, indicator, self.expertise_type)
                opinion_indicator.save()
        survey_completed.send(sender=ExpertiseRequest, instance=response, data=data)
        return response
