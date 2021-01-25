from django import forms

from lrr.inspections import models as inspections_models
from lrr.repository import models as repository_models
from lrr.complexes import models as complexes_models
from lrr.users.models import Expert


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
                }
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
                }
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
            'date_end': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }
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
        model = inspections_models.CheckList
        fields = [
            "type",
            "expert",
        ]
        exclude = ["expertise", "date", "protocol", "status"]


class CheckListUpdateForm(forms.ModelForm):
    class Meta:
        model = inspections_models.CheckList
        fields = [
            "type",
            "expert",
            "date",
            "protocol",
            "status"
        ]
        exclude = ["expertise", ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Question
        fields = [
            "title",
            "checklist",
            "answer",
        ]
