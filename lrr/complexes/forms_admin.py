from django import forms

from lrr.complexes import models


class DigitalComplexAdminForm(forms.ModelForm):
    class Meta:
        model = models.DigitalComplex
        fields = [
            "keywords",
            "description",
            "language",
            "format",
            "subjects",
            "directions",
            "competences",
            "results_edu",
            # "thematic_plan",
            # "form_control"
        ]


class AssignmentAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = models.AssignmentAcademicGroup
        fields = [
            "digital_complex",
            "academic_group",
            "group_subject",
            "learn_date"
        ]


class ThemeForm(forms.ModelForm):
    class Meta:
        model = models.Theme
        fields = [
            "title",
        ]


#
# class CellForm(forms.ModelForm):
#     class Meta:
#         model = grid_models.Cell
#         fields = '__all__'


class ComponentForm(forms.ModelForm):
    class Meta:
        model = models.ComponentComplex
        fields = "__all__"


class ThemeAdminForm(forms.ModelForm):
    class Meta:
        model = models.Theme
        fields = "__all__"

# class CellAdminForm(forms.ModelForm):
#     class Meta:
#         model = grid_models.Cell
#
#         fields = "__all__"
