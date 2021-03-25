from django import forms

from lrr.inspections import models as inspection_models


class ExpertiseAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.Expertise
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
            "owner",
        ]


class ExpertiseRequestAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.ExpertiseRequest
        fields = [
            "expertise",
            "type",
            "expert",
            "status",
            "date",
            "protocol",
            "survey"
        ]


class CheckListQestionAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.CheckListQestion
        fields = '__all__'


class QestionAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.Question
        fields = "__all__"


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.Answer
        fields = "__all__"
