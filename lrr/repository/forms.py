from django import forms
from . import models


class StatusCORForm(forms.ModelForm):
    class Meta:
        model = models.StatusCOR
        fields = [
            "quality_category",
            "interactive_category",
            "expertise_status",
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


class ResultEduResourcesForm(forms.ModelForm):
    class Meta:
        model = models.ResultEduResources
        fields = [
            "status",
            "result_edu",
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
            "ketwords",
            "description",
            "edu_programs_tags",
            "conformity_themes",
            "authors",
            "copyright_holder",
            "subjects_tags",
            "status_cor",
            "owner",
            "result_edu_resource",
            "language",
            "provided_disciplines",
            "platform",
        ]


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
            "titile",
        ]


class SubjectTagForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTag
        fields = [
            "tag",
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            "academic_group",
            "person",
        ]


class ConformityThemesForm(forms.ModelForm):
    class Meta:
        model = models.ConformityThemes
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
            "subject_themes",
            "subject",
            "edu_programs",
        ]


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            "location",
            "date_birthday",
            "city",
            "middle_name",
            "country",
            "first_name",
            "avatar",
            "last_name",
            "user",
        ]
