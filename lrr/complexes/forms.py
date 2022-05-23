from django import forms
from django_select2 import forms as s2forms
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild
from lrr.repository.models import DigitalResource

from . import grid_models
from . import models as complex_models


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
            "form_control"
        ]
        exclude = ["title", "owner", "digital_resources", "results_edu"]

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
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "directions": DirectionsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "competences": CompetencesWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "form_control": forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            # "results_edu": ResultsEduWidget(
            #     attrs={
            #         'class': 'form-control',
            #     },
            # )
        }


class ThematicPlanForm(forms.ModelForm):
    class Meta:
        model = grid_models.ThematicPlan
        fields = "__all__"


class DigitalComplexWidget(s2forms.Select2Widget):
    search_fields = [
        "title__icontains",
        "keywords__icontains",
        "format__icontains",
    ]
    max_results = 50


class AcademicGroupWidget(s2forms.Select2Widget):
    search_fields = [
        "number__icontains",
    ]
    max_results = 50


class SubjectWidget(s2forms.Select2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class AssignmentAcademicGroupForm(forms.ModelForm):
    class Meta:
        model = complex_models.AssignmentAcademicGroup
        fields = ['academic_group', 'group_subject', 'learn_date']
        # widgets = {
        #     "academic_group": forms.Select(
        #         attrs={
        #             'class': 'form-control',
        #
        #         },
        #     ),
        #     "learn_date": forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #
        #         },
        #     ),
        #     "group_subject": forms.Select(
        #         attrs={
        #             'class': 'form-control',
        #
        #         },
        #     )
        # }


# AssignmentAcademicGroupFormset = forms.inlineformset_factory(
#     complex_models.DigitalComplex,
#     complex_models.AssignmentAcademicGroup,
#     fields=('academic_group', 'learn_date',),
#     extra=1,
#     widgets={
#         # "digital_complex": DigitalComplexWidget(
#         #     attrs={
#         #         'class': 'form-control',
#         #
#         #     },
#         # ),
#         "academic_group": AcademicGroupWidget(
#             attrs={
#                 'class': 'form-control',
#
#             },
#         ),
#         "learn_date": forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#
#             },
#         ),
#     }
# )


class ComplexParentComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.ComplexParentComponent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ComplexParentComponentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ResourceComponentWidget(s2forms.Select2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class ResourceComponentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     # self.user = user
    #     super(ResourceComponentForm, self).__init__(*args, **kwargs)  # populates the post
    #     self.fields['digital_resource'].queryset = DigitalResource.objects.filter(
    #         owner=self.user)
    # TODO: limit choices

    class Meta:
        model = complex_models.ResourceComponent
        fields = ['digital_resource', 'description', 'order']
        widgets = {
            "digital_resource": forms.Select(
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


class PlatformComponentWidget(s2forms.Select2Widget):
    search_fields = [
        "title__icontains",
    ]
    max_results = 50


class PlatformComponentForm(forms.ModelForm):
    class Meta:
        model = complex_models.PlatformComponent
        fields = ['title', 'description', 'url', 'order']
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
        fields = ['title', 'description_session', 'url', 'description', 'order']
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
        fields = ['title', 'description', 'url', 'order']
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


ComplexParentComponentFormSet = polymorphic_modelformset_factory(
    complex_models.ComplexParentComponent,
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


class ThemeForm(forms.ModelForm):
    class Meta:
        model = complex_models.Theme
        fields = ["title"]
