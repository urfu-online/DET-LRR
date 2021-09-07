from django import forms
from easy_select2.widgets import Select2Multiple, Select2

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
            'directions': Select2Multiple,
            'expert': Select2Multiple,
            'digital_complexes': Select2Multiple,
            'subjects': Select2Multiple,
            'digital_resource': Select2,
            'owner': Select2,
            'status': Select2,
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'date'})
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

        widgets = {
            'expert': Select2,
            'type': Select2,
            'expertise': Select2,
            'status': Select2,
            'survey': Select2,
            'date': forms.DateTimeInput(attrs={'type': 'date'})
        }
