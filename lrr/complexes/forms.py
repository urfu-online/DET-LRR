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
            "space_cell",
        ]


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
            "space_cell",
        ]


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
