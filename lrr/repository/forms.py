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
            "edu_programs_tags": EduProgramsWidget,
            "subjects_tags": SubjectsWidget,
            "authors": AuthorsWidget,
            "provided_disciplines": ProvidedDisciplinesWidget,
            "result_edu": ResultEduWidget,
        }

        # def __init__(self, *args, **kwargs):
        #     super(DigitalResourceForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_tag = True
        #     self.helper.form_class = 'form-horizontal'
        #     self.helper.label_class = 'col-md-3 create-label'
        #     self.helper.field_class = 'col-md-9'
        #     self.helper.layout = Layout(
        #         Div(
        #             Fieldset('Добавить источники',
        #                      Formset('source')),
        #             HTML("<br>"),
        #         )
        #     )


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
