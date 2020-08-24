from django import forms
from django.contrib import admin

from . import models


class DRStatusAdminForm(forms.ModelForm):
    class Meta:
        model = models.DRStatus
        fields = "__all__"


class DRStatusAdmin(admin.ModelAdmin):
    form = DRStatusAdminForm
    list_display = [
        "expertise_status",
        "quality_category",
        "interactive_category",
        "created",
    ]
    readonly_fields = [
        "created",
    ]


class ExpertiseStatusAdminForm(forms.ModelForm):
    class Meta:
        model = models.ExpertiseStatus
        fields = "__all__"


class ExpertiseStatusAdmin(admin.ModelAdmin):
    form = ExpertiseStatusAdminForm
    list_display = [
        "end_date",
        "status",
        "accepted_status",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class SubjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = "__all__"


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    search_fields = ['title']
    list_display = [
        "title",
        "labor",
        "created",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class OrganizationAdminForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = "__all__"


class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationAdminForm
    list_display = [
        "title",
        "url",
        "id",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    search_fields = ["title", ]


class EduProgramAdminForm(forms.ModelForm):
    class Meta:
        model = models.EduProgram
        fields = "__all__"


class EduProgramAdmin(admin.ModelAdmin):
    form = EduProgramAdminForm
    search_fields = ["title"]
    list_display = [
        "title",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class ProvidingDisciplineAdminForm(forms.ModelForm):
    class Meta:
        model = models.ProvidingDiscipline
        fields = "__all__"


class ProvidingDisciplineAdmin(admin.ModelAdmin):
    form = ProvidingDisciplineAdminForm
    autocomplete_fields = ["edu_program", "subject"]
    list_display = [
        "edu_program",
        "subject",
        "rate"
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


# class DigitalResourceCompetenceForm(forms.ModelForm):
#     class Meta:
#         model = models.DigitalResourceCompetence
#         fields = "__all__"
#
#
# class DigitalResourceCompetenceAdmin(admin.ModelAdmin):
#     form = DigitalResourceCompetenceForm
#     list_display = [
#         "digital_resource",
#         "competence"
#     ]
#     readonly_fields = [
#         "last_updated",
#         "created",
#     ]


class ResultEduAdminForm(forms.ModelForm):
    class Meta:
        model = models.ResultEdu
        fields = "__all__"


class ResultEduAdmin(admin.ModelAdmin):
    form = ResultEduAdminForm
    list_display = [
        "title",
        "competence"
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class DigitalResourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.DigitalResource
        fields = "__all__"


@admin.register(models.DigitalResource)
class DigitalResourceAdmin(admin.ModelAdmin):
    form = DigitalResourceAdminForm
    fields = [
        "title",
        "type",
        "source_data",
        "platform",
        "language",
        "keywords",
        "description",
        "authors",
        "copyright_holder",
        "subjects_tags",
        "edu_programs_tags",
        "status_cor",
        "owner",
        "provided_disciplines",
        "conformity_theme",
        "result_edu",

        "created",
        "last_updated",
    ]
    list_display = [
        "title",
        "type",
        "status_cor",
        "source_data",
        "copyright_holder",
        "created",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]


# class DigitalResourceChild(PolymorphicChildModelAdmin):
#     base_model = models.DigitalResource
#     autocomplete_fields = ["copyright_holder"]

class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Source
        fields = "__all__"


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    form = SourceAdminForm
    list_display = [
        "link_name",
        "URL",
        "file",
        "digital_resource",
    ]


# class DigitalResourceLinksAdmin(DigitalResourceChild):
#     base_model = models.DigitalResourceLinks
#
#
# @admin.register(models.DigitalResourceFiles)
# class DigitalResourceFilesAdmin(DigitalResourceChild):
#     base_model = models.DigitalResourceFiles

# class DigitalResourceAdminForm(forms.ModelForm):
#     class Meta:
#         model = models.DigitalResource
#         fields = "__all__"
#
# @admin.register(models.DigitalResource)
# class DigitalResourceAdmin(admin.ModelAdmin):
#     form = DigitalResourceAdminForm


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = "__all__"


class CompetenceAdmin(admin.ModelAdmin):
    form = CompetenceAdminForm
    list_display = [
        "title",
        "code",
    ]
    readonly_fields = [
        "created",
    ]


class PlatformAdminForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = "__all__"


class PlatformAdmin(admin.ModelAdmin):
    form = PlatformAdminForm
    list_display = [
        "title",
        "url",
        "id",
    ]
    readonly_fields = [
        "created"
    ]


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = [
        "code",
        "title",
        "created",
    ]
    readonly_fields = [
        "created",
    ]


class SubjectTagAdminForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTag
        fields = "__all__"


class SubjectTagAdmin(admin.ModelAdmin):
    form = SubjectTagAdminForm
    list_display = [
        "tag",
        "created",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class ConformityThemeAdminForm(forms.ModelForm):
    class Meta:
        model = models.ConformityTheme
        fields = "__all__"


class ConformityThemeAdmin(admin.ModelAdmin):
    form = ConformityThemeAdminForm
    list_display = [
        "practice",
        "theory",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class EduProgramTagAdminForm(forms.ModelForm):
    class Meta:
        model = models.EduProgramTag
        fields = "__all__"


class EduProgramTagAdmin(admin.ModelAdmin):
    form = EduProgramTagAdminForm
    list_display = [
        "tag",
        "created",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class SubjectThemeAdminForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTheme
        fields = "__all__"


class SubjectThemeAdmin(admin.ModelAdmin):
    form = SubjectThemeAdminForm
    list_display = [
        "title",
        "thematic_plan",
        "created",
    ]
    readonly_fields = [
        "created",
    ]


class ThematicPlanAdminForm(forms.ModelForm):
    class Meta:
        model = models.ThematicPlan
        fields = "__all__"


class ThematicPlanAdmin(admin.ModelAdmin):
    form = ThematicPlanAdminForm
    list_display = [
        "created",
        "title",
    ]
    readonly_fields = [
        "created",
    ]


# class PersonAdminForm(forms.ModelForm):
#     class Meta:
#         model = models.Person
#         fields = "__all__"


# class PersonAdmin(admin.ModelAdmin):
#     form = PersonAdminForm
#     list_display = [
#         "location",
#         "date_birthday",
#         "city",
#         "created",
#         "middle_name",
#         "country",
#         "first_name",
#         "avatar",
#         "last_name",
#     ]
#     readonly_fields = [
#         "created",
#     ]


admin.site.register(models.DRStatus, DRStatusAdmin)
admin.site.register(models.ExpertiseStatus, ExpertiseStatusAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.EduProgram, EduProgramAdmin)
admin.site.register(models.ProvidingDiscipline, ProvidingDisciplineAdmin)
admin.site.register(models.ResultEdu, ResultEduAdmin)
admin.site.register(models.Competence, CompetenceAdmin)
admin.site.register(models.Platform, PlatformAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.SubjectTag, SubjectTagAdmin)
admin.site.register(models.ConformityTheme, ConformityThemeAdmin)
admin.site.register(models.EduProgramTag, EduProgramTagAdmin)
admin.site.register(models.SubjectTheme, SubjectThemeAdmin)
admin.site.register(models.ThematicPlan, ThematicPlanAdmin)
