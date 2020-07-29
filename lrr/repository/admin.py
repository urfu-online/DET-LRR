from django import forms
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelFilter, PolymorphicChildModelAdmin

from . import models


class DRStatusAdminForm(forms.ModelForm):
    class Meta:
        model = models.DRStatus
        fields = "__all__"


class DRStatusAdmin(admin.ModelAdmin):
    form = DRStatusAdminForm
    list_display = [
        "quality_category",
        "created",
        "interactive_category",
    ]
    readonly_fields = [
        "created",
        "quality_category",
        "interactive_category",
    ]



class ExpertiseStatusAdminForm(forms.ModelForm):
    class Meta:
        model = models.ExpertiseStatus
        fields = "__all__"


class ExpertiseStatusAdmin(admin.ModelAdmin):
    form = ExpertiseStatusAdminForm
    list_display = [
        "last_updated",
        "end_date",
        "accepted_status",
        "created",
        "last_updated",
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
    list_display = [
        "description",
        "created",
        "title",
        "last_updated",
        "labor",
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
        "last_updated",
        "description",
        "logo",
        "contacts",
        "title",
        "created",
        "url",
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
    list_display = [
        "description",
        "last_updated",
        "created",
        "short_description",
        "title",
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
    list_display = [
        "rate",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class ResultEduAdminForm(forms.ModelForm):
    class Meta:
        model = models.ResultEdu
        fields = "__all__"


class ResultEduAdmin(admin.ModelAdmin):
    form = ResultEduAdminForm
    list_display = [
        "title",
        "last_updated",
        "created",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


# class DigitalResourceAdminForm(forms.ModelForm):
#     class Meta:
#         model = models.DigitalResource
#         fields = "__all__"
#
#
# class DigitalResourceAdmin(admin.ModelAdmin):
#     form = DigitalResourceAdminForm
#     list_display = [
#         "title",
#         "created",
#         "type",
#         "source_data",
#         "last_updated",
#         "ketwords",
#         "description",
#     ]
#     readonly_fields = [
#         "created",
#         "last_updated",
#     ]

class DigitalResourceChild(PolymorphicChildModelAdmin):
    base_model = models.DigitalResource
    autocomplete_fields = ["copyright_holder"]


@admin.register(models.DigitalResourceLinks)
class DigitalResourceLinksAdmin(DigitalResourceChild):
    base_model = models.DigitalResourceLinks


@admin.register(models.DigitalResourceFiles)
class DigitalResourceFilesAdmin(DigitalResourceChild):
    base_model = models.DigitalResourceFiles


@admin.register(models.DigitalResource)
class DigitalResourceParentAdmin(PolymorphicParentModelAdmin):
    base_model = models.DigitalResource
    child_models = (models.DigitalResourceLinks, models.DigitalResourceFiles)
    list_filter = (PolymorphicChildModelFilter,)


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = "__all__"


class CompetenceAdmin(admin.ModelAdmin):
    form = CompetenceAdminForm
    list_display = [
        "created",
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
        "created",
        "url",
        "logo",
        "description",
        "contacts",
        "title",
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
        "created",
        "last_updated",
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
        "created",
        "last_updated",
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
        "description",
        "created",
        "title",
    ]
    readonly_fields = [
        "created",
        "title",
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
