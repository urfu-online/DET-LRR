from django import forms

from lrr.complexes import models as complex_models


class DigitalComplexAdminForm(forms.ModelForm):
    class Meta:
        model = complex_models.DigitalComplex
        fields = [
            "keywords",
            "description",
            "language",
            "format",
            "subjects",
            "directions",
            "competences",
            "results_edu",
            "digital_resources",
        ]


class CellAdminForm(forms.ModelForm):
    class Meta:
        model = complex_models.Cell
        fields = "__all__"


class ComplexSpaceCellAdminForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexSpaceCell
        fields = "__all__"


class AssignmentAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = complex_models.AssignmentAcademicGroup
        fields = "__all__"
