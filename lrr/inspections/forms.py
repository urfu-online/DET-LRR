from django import forms
from django_select2 import forms as s2forms

from lrr.inspections import models as inspections_models


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


class ExpertiseCreateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Expertise
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


class ExpertiseUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Expertise
        fields = [
            "digital_resource",
            "subjects",
            "directions",
            "digital_complexes",
            "expert",
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
            'subjects': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                },
            ),
            'directions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }
            ),
            'digital_complexes': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }
            ),
            'expert': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',

                }
            ),
            'date_end': forms.DateTimeInput(
                attrs={
                    'class': 'datetimepicker form-control',
                    'required': 'true'
                },
                format='%d/%m/%Y %H:%M'
            ),
            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',

                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            )
        }
        exclude = ['status', 'date']


class SurveyWidget(s2forms.Select2Widget):
    search_fields = [
        "name__icontains",
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


class ExpertiseRequestCreateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "survey",
            "expert",
        ]
        exclude = ["expertise", "date", "protocol", "status", "type"],
        widgets = {
            'survey': forms.Select(
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


class ExpertiseRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "type",
            "expert",
            "date",
            "protocol",
            "status",
            "expertise",
            "survey"
        ]
        widgets = {
            'survey': forms.Select(
                attrs={
                    'class': 'form-select',

                }
            )
        }


class IndicatorWidget(s2forms.Select2Widget):
    search_fields = ["group__title"]
    max_results = 5
