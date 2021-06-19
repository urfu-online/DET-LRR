from django import forms
from django.forms import inlineformset_factory
from django_select2 import forms as s2forms

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


class EduProgramsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["tag__title__icontains"]
    max_results = 50


class SubjectsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["tag__title__icontains"]
    max_results = 50


class ResultEduWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class CompetenceWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["title__icontains"]
    max_results = 50


class AuthorsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "last_name__icontains",
        "first_name__icontains",
        "middle_name__icontains",
        "user__email__icontains",
        "user__username__icontains",
    ]
    max_results = 50


class ProvidedDisciplinesWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "edu_program__title__icontains",
        "subject__title__icontains",
    ]
    max_results = 50


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
            "type": forms.Select(
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
            "copyright_holder": forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            "language": forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            "platform": forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            "edu_programs_tags": EduProgramsWidget(
                attrs={
                    'class': 'form-control',

                },
            ),
            "subjects_tags": SubjectsWidget(
                attrs={
                    'class': 'form-control',

                },
            ),
            "authors": AuthorsWidget(
                attrs={
                    'class': 'form-control',

                },
            ),
            "result_edu": ResultEduWidget(
                attrs={
                    'class': 'form-control',
                },
            ),
            "competences": CompetenceWidget(
                attrs={
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
    fields=('link_name', 'type', 'URL', 'file'),
    exclude=('id',),
    extra=0,
    widgets={
        'link_name': forms.TextInput(
            attrs={
                'class': 'form-control',

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
                'class': 'form-control-file',
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
