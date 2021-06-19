from django import forms

from lrr.complexes import grid_models
from lrr.complexes import models as complex_models


class ContainerAdminForm(forms.ModelForm):
    class Meta:
        model = grid_models.Container
        fields = "__all__"


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
            "thematic_plan",
            "form_control"
        ]


class AssignmentAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = complex_models.AssignmentAcademicGroup
        fields = "__all__"


class ThemeForm(forms.ModelForm):
    class Meta:
        model = grid_models.Theme
        fields = [
            "title",
            "content",
        ]


#
# class CellForm(forms.ModelForm):
#     class Meta:
#         model = grid_models.Cell
#         fields = '__all__'


class ContainerForm(forms.ModelForm):
    class Meta:
        model = grid_models.Container
        fields = [
            "type",
        ]


class ComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComponentComplex
        fields = "__all__"


class ThemeAdminForm(forms.ModelForm):
    class Meta:
        model = grid_models.Theme
        fields = "__all__"

# class CellAdminForm(forms.ModelForm):
#     class Meta:
#         model = grid_models.Cell
#
#         fields = "__all__"
