from django import forms

from lrr.complexes import models as complex_models


class DigitalComplexForm(forms.ModelForm):
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
        exclude = ["owner", ]


class CellForm(forms.ModelForm):
    class Meta:
        model = complex_models.Cell
        fields = [
            "type",
            "include_practice",
            "include_theory",
            "beg_theme_number",
            "end_theme_number",
            "methodology_description",
        ]


class CellWeeksForm(forms.ModelForm):
    class Meta:
        model = complex_models.CellWeeks
        fields = "__all__"


class ComplexSpaceCellForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexSpaceCell
        fields = [
            "title",
            "cells",
            "description",
        ]


class ComplexThemeForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexTheme
        fields = [
            "title",
            "number",
        ]


class WorkPlanAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = complex_models.WorkPlanAcademicGroup
        fields = "__all__"
