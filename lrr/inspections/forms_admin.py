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
        ]


class CheckListAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.CheckList
        fields = [
            "expertise",
            "type",
            "expert",
            "date",
            "protocol",
        ]


class QestionAdminForm(forms.ModelForm):
    class Meta:
        model = inspection_models.Question
        fields = "__all__"
