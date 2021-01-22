from django import forms

from lrr.inspections import models as inspections_models
from lrr.repository import models as repository_models
from lrr.complexes import models as complexes_models
from lrr.users.models import Expert


class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Expertise
        fields = '__all__'
        # fields = [
        #     "digital_resource",
        #     "date",
        #     "subjects",
        #     "directions",
        #     "digital_complexes",
        #     "expert",
        #     "date_end",
        #     "file",
        #     "remarks",
        #     "status",np
        # ]
        widgets = {
            # 'digital_resource': forms.MultipleChoiceField(
            #     attrs={
            #         'class': 'form-control',
            #         'required': 'false'
            #     }
            # ),
            'date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }
            ),
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'required': 'false'
                }
            ),
            'subjects': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
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
                    'required': 'true'
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
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
        }


class CheckListForm(forms.ModelForm):
    class Meta:
        model = inspections_models.CheckList
        fields = [
            "expertise",
            "type",
            "expert",
            "date",
            "protocol",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Question
        fields = [
            "title",
            "checklist",
            "answer",
        ]
