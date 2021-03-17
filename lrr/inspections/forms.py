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
                    'class': 'form-control',
                },
            ),
            "directions": DirectionsWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "digital_complexes": DigitalComplexesWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            # 'digital_resource': forms.MultipleChoiceField(
            #     attrs={
            #         'class': 'form-control',
            #         'required': 'false'
            #     }
            # ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'required': 'false'
                }
            ),
            'expert': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
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
            #         'required': 'false'
            #     }
            # ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
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
            #         'required': 'false'
            #     }
            # ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'required': 'false'
                }
            ),
            'subjects': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            'directions': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            'digital_complexes': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            'expert': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            'date_end': forms.DateInput(
                attrs={
                    'class': 'datepicker form-control',
                    'required': 'true'
                },
                format='%d/%m/%Y'
            ),
            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            )
        }
        exclude = ['status', 'date']


class CheckListCreateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "type",
            "expert",
        ]
        exclude = ["expertise", "date", "protocol", "status"]


class ExpertiseRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "type",
            "expert",
            "date",
            "protocol",
            "status",
            "expertise"
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Question
        fields = [
            "title",
            "checklist",
            "type",
            "choices"
        ]


class CheckListQestionForm(forms.ModelForm):
    class Meta:
        model = inspections_models.CheckListQestion
        fields = '__all__'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Answer
        fields = "__all__"
