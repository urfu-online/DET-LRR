from django import forms
from django_select2 import forms as s2forms
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild

from lrr.complexes import models as complex_models


class DirectionsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class SubjectsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class CompetencesWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "title__icontains",
        "code__icontains"
    ]
    max_results = 50


class ResultsEduWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


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
        ]
        exclude = ["owner", "digital_resources"]

        widgets = {
            "keywords": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "format": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "language": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "subjects": SubjectsWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "directions": DirectionsWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "competences": CompetencesWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "results_edu": ResultsEduWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            )
        }


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


class ComponentComplexForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComponentComplex
        fields = "__all__"


class ResourceComponentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class ResourceComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.ResourceComponent
        fields = ['digital_resource', 'description']
        widgets = {
            "digital_resource": ResourceComponentWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "description": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            )
        }


ComponentComplexFormSet = polymorphic_modelformset_factory(
    complex_models.ComponentComplex,
    fields='__all__',
    extra=1,
    formset_children=(
        PolymorphicFormSetChild(
            model=complex_models.ResourceComponent,
            form=ResourceComponentForm,
            # widgets={
            #     "digital_resource": ResourceComponentWidget(
            #         attrs={
            #             'class': 'form-control',
            #             'required': 'false'
            #         },
            #     ),
            #     "description": forms.TextInput(
            #         attrs={
            #             'class': 'form-control',
            #             'required': 'false'
            #         },
            #     )
            # },
        ),
        # PolymorphicFormSetChild(
        #     complex_models.PlatformComponent),
        # PolymorphicFormSetChild(
        #     complex_models.TraditionalSessionComponent),
    ))
