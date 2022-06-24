from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django import forms
from django.forms import inlineformset_factory
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget, Select2Widget

from . import models


class SubjectForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = [
            "description",
            "title",
            "labor",
        ]


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = [
            "description",
            "logo",
            "contacts",
            "title",
            "url",
        ]


class EduProgramForm(forms.ModelForm):
    class Meta:
        model = models.EduProgram
        fields = [
            "description",
            "short_description",
            "title",
        ]


class ResultEduForm(forms.ModelForm):
    class Meta:
        model = models.ResultEdu
        fields = [
            "title",
            "description",
        ]


class EduProgramsWidget(ModelSelect2MultipleWidget):
    search_fields = ["tag__title__icontains"]
    max_results = 20


class SubjectsWidget(ModelSelect2MultipleWidget):
    search_fields = ["tag__title__icontains"]
    max_results = 20


class ResultEduWidget(ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 20


class CompetenceWidget(ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 20


class AuthorsWidget(ModelSelect2MultipleWidget):
    search_fields = [
        "last_name__icontains",
        "first_name__icontains",
        "middle_name__icontains",
        "user__email__icontains",
        "user__username__icontains",
    ]
    max_results = 20


class ProvidedDisciplinesWidget(ModelSelect2MultipleWidget):
    search_fields = [
        "edu_program__title__icontains",
        "subject__title__icontains",
    ]
    max_results = 20


class LanguageWidget(ModelSelect2Widget):
    search_fields = ["title__search", "code__search"]
    max_results = 20


class PlatformWidget(ModelSelect2Widget):
    search_fields = ["title__search", "description__search", "url__search"]
    max_results = 10


class OrganizationWidget(ModelSelect2Widget):
    search_fields = ["title__search", "description__search"]
    max_results = 10


class TypeWidget(Select2Widget):
    max_results = 10


class DigitalResourceForm(forms.ModelForm):
    class Meta:
        model = models.DigitalResource
        fields = [
            "title",
            "type",
            "keywords",
            "description",
            "edu_programs_tags",
            "authors",
            "copyright_holder",
            "subjects_tags",
            "owner",
            "language",
            "platform",
            "result_edu",
            "competences",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            "type": TypeWidget(
                attrs={
                    'class': 'form-control',

                }
            ),
            "keywords": forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            "copyright_holder": OrganizationWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',

                }
            ),
            "language": LanguageWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',

                }
            ),
            "platform": PlatformWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',

                }
            ),
            "edu_programs_tags": EduProgramsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',

                },
            ),
            "subjects_tags": SubjectsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "authors": AuthorsWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',

                },
            ),
            "result_edu": ResultEduWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),
            "competences": CompetenceWidget(
                attrs={
                    'data-minimum-input-length': 0,
                    'class': 'form-control',
                },
            ),

        }


# class SourceForm(forms.ModelForm):
#     class Meta:
#         model = models.Source
#
#     fields = ['link_name', 'URL', 'file', 'type']
#
#     widgets = {
#
#     }


SourceFormset = inlineformset_factory(
    models.DigitalResource,
    models.Source,
    fields=('type', 'link_name', 'file', 'URL',),
    exclude=('id',),
    extra=1,
    max_num=1,
    widgets={
        'link_name': forms.TextInput(
            attrs={
                'class': 'form-control'
                # 'required': 'required'

            },
        ),
        'type': forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
        'URL': forms.TextInput(
            attrs={
                'class': 'form-control',

            },
        ),
        'file': forms.FileInput(
            attrs={
                'class': 'custom-file-input',
            },
        ),
    }
)


class CompetenceForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = [
            "title",
            "code",
        ]


class PlatformForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = [
            "title",
            "url",
            "logo",
            "description",
            "contacts",
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',

                },
            ),
            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',

                },
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',

                },
            ),
            'contacts': forms.Textarea(
                attrs={
                    'class': 'form-control',

                },
            ),
        }


class LanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = [
            "code",
            "title",
        ]


class SubjectTagForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTag
        fields = [
            "tag",
        ]


class EduProgramTagForm(forms.ModelForm):
    class Meta:
        model = models.EduProgramTag
        fields = [
            "tag",
        ]


class DigitalResourceFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            'title',
            'type',
            'copyright_holder__title',
            'language',
            'subjects_tags__tag__title',
            'edu_programs_tags__tag__title',
            Submit('submit', 'Найти'),
            css_class="form-row",
        ))
