from django import forms

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
        ]


class DirectionForm(forms.ModelForm):
    class Meta:
        model = models.Direction
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
