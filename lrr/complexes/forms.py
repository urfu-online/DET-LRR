from django import forms
from django_select2 import forms as s2forms
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild

from lrr.complexes import grid_models
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
        exclude = ["title", "owner", "digital_resources"]

        widgets = {
            "keywords": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "format": forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            "language": forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            "subjects": SubjectsWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "directions": DirectionsWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "competences": CompetencesWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "results_edu": ResultsEduWidget(
                attrs={
                    'class': 'form-control',
                },
            )
        }


class CellForm(forms.ModelForm):
    class Meta:
        model = grid_models.Cell
        fields = "__all__"
        #
        # widgets = {
        #     "type": forms.Select(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        #     "methodology_description": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        # }


class DigitalComplexWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "title__icontains",
        "keywords__icontains",
        "format__icontains",
    ]
    max_results = 50


class AcademicGroupWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "number__icontains",
    ]
    max_results = 50


class SubjectWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class AssignmentAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = complex_models.AssignmentAcademicGroup
        fields = ['academic_group', 'subject', 'learn_date', 'semestr']
        widgets = {
            # "digital_complex": DigitalComplexWidget(
            #     attrs={
            #         'class': 'form-control',
            #
            #     },
            # ),
            "academic_group": AcademicGroupWidget(
                attrs={
                    'class': 'form-control',

                },
            ),
            "subject": SubjectWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "learn_date": forms.TextInput(
                attrs={
                    'class': 'form-control',

                },
            ),
            "semestr": forms.Select(
                attrs={
                    'class': 'form-control',

                },
            ),
        }


AssignmentAcademicGroupFormset = forms.inlineformset_factory(
    complex_models.DigitalComplex,
    complex_models.AssignmentAcademicGroup,
    fields=('academic_group', 'subject', 'learn_date', 'semestr'),
    extra=1,
    widgets={
        # "digital_complex": DigitalComplexWidget(
        #     attrs={
        #         'class': 'form-control',
        #
        #     },
        # ),
        "academic_group": AcademicGroupWidget(
            attrs={
                'class': 'form-control',

            },
        ),
        "subject": SubjectWidget(
            attrs={
                'class': 'form-control',

            },
        ),
        "learn_date": forms.TextInput(
            attrs={
                'class': 'form-control',

            },
        ),
        "semestr": forms.Select(
            attrs={
                'class': 'form-control',

            },
        ),
    }
)


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
        fields = ['digital_resource', 'description', 'order']
        widgets = {
            "digital_resource": ResourceComponentWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "order": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            )
        }


class PlatformComponentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class PlatformComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.PlatformComponent
        fields = ['title', 'description', 'url']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "url": forms.URLInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "order": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            )
        }


class TraditionalSessionComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.TraditionalSessionComponent
        fields = ['title', 'description_session', 'url', 'description']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description_session": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "url": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "order": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            )
        }


class LiterarySourcesComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.LiterarySourcesComponent
        fields = ['title', 'description', 'url']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "url": forms.URLInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "order": forms.TextInput(
                attrs={
                    'class': 'form-control',
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
            #
            #         },
            #     ),
            #     "description": forms.TextInput(
            #         attrs={
            #             'class': 'form-control',
            #
            #         },
            #     )
            # },
        ),
        # PolymorphicFormSetChild(
        #     complex_models.PlatformComponent),
        # PolymorphicFormSetChild(
        #     complex_models.TraditionalSessionComponent),
    ))
