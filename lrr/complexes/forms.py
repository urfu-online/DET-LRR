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
            "title",
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
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "keywords": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "description": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "format": forms.TextInput(
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
            'theme_name',
            'methodology_description'
        ]

        widgets = {
            "type": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "theme_name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "methodology_description": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
        }

class CellWeeksForm(forms.ModelForm):
    class Meta:
        model = complex_models.CellWeeks
        fields = "__all__"


class ComplexSpaceCellForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexSpaceCell
        fields = "__all__"


class ComplexThemeForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexTheme
        fields = [
            "title",
            "number",
        ]


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
            #         'required': 'false'
            #     },
            # ),
            "academic_group": AcademicGroupWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "subject": SubjectWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "learn_date": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "semestr": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
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
        #         'required': 'false'
        #     },
        # ),
        "academic_group": AcademicGroupWidget(
            attrs={
                'class': 'form-control',
                'required': 'false'
            },
        ),
        "subject": SubjectWidget(
            attrs={
                'class': 'form-control',
                'required': 'false'
            },
        ),
        "learn_date": forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'false'
            },
        ),
        "semestr": forms.Select(
            attrs={
                'class': 'form-control',
                'required': 'false'
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


class PlatformComponentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class PlatformComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.PlatformComponent
        fields = ['platform', 'description']
        widgets = {
            "platform": PlatformComponentWidget(
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


class TraditionalSessionComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.TraditionalSessionComponent
        fields = ['title', 'description_session', 'url', 'description']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "description_session": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "url": forms.TextInput(
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


class LiterarySourcesComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.LiterarySourcesComponent
        fields = ['title', 'url']
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "url": forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
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
