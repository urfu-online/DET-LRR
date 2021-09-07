from django import forms
from easy_select2 import apply_select2
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
        widgets = {
            'directions': apply_select2(forms.SelectMultiple),
            'expert': apply_select2(forms.SelectMultiple),
            'digital_complexes': apply_select2(forms.SelectMultiple),
            'subjects': apply_select2(forms.SelectMultiple),
            'digital_resource': apply_select2(forms.Select),
            'owner': apply_select2(forms.Select),
            'status': apply_select2(forms.Select),
        }


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
