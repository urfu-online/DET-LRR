from django import forms
from django.forms import inlineformset_factory
from django_select2 import forms as s2forms

from . import models


class DRStatusForm(forms.ModelForm):
    class Meta:
        model = models.DRStatus
        fields = [
            "digital_resource",
            "quality_category",
            "interactive_category",
            "expertise_status",
            "edu_program",
            "subject"
        ]


class ExpertiseStatusForm(forms.ModelForm):
    class Meta:
        model = models.ExpertiseStatus
        fields = [
            "end_date",
            "status",
            "accepted_status",
        ]


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


class ProvidingDisciplineForm(forms.ModelForm):
    class Meta:
        model = models.ProvidingDiscipline
        fields = [
            "rate",
            "edu_program",
            "subject",
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
            "source_data",
            "keywords",
            "description",
            "edu_programs_tags",
            "authors",
            "copyright_holder",
            "subjects_tags",
            "owner",
            "language",
            "provided_disciplines",
            "platform",
            "result_edu",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "type": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "source_data": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "keywords": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "copyright_holder": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "language": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "platform": forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                }
            ),
            "edu_programs_tags": EduProgramsWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "subjects_tags": SubjectsWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "authors": AuthorsWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "provided_disciplines": ProvidedDisciplinesWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),
            "result_edu": ResultEduWidget(
                attrs={
                    'class': 'form-control',
                    'required': 'false'
                },
            ),

        }


SourceFormset = inlineformset_factory(
    models.DigitalResource,
    models.Source,
    fields=('link_name', 'URL', 'file', 'type'),
    extra=1
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
            "url",
            "logo",
            "description",
            "contacts",
            "title",
        ]


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


class ConformityThemeForm(forms.ModelForm):
    class Meta:
        model = models.ConformityTheme
        fields = [
            "practice",
            "theory",
            "theme",
        ]


class EduProgramTagForm(forms.ModelForm):
    class Meta:
        model = models.EduProgramTag
        fields = [
            "tag",
        ]


class SubjectThemeForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTheme
        fields = [
            "description",
            "title",
        ]


class ThematicPlanForm(forms.ModelForm):
    class Meta:
        model = models.ThematicPlan
        fields = [
            "title",
            "subject",
            "edu_program",
        ]
