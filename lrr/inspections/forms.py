from django import forms

from lrr.inspections import models as inspections_models


class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = inspections_models.Expertise
        fields = [
            "digital_resource",
            "date",
            "subjects",
            "directions",
            "digital_complexes",
            "expert",
            "date_end",
            "file",
            "remarks",
            "status",
        ]
        widgets = {
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
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
