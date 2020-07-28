from django import forms
from django.contrib import admin

from . import models


class StatusCORAdminForm(forms.ModelForm):
    class Meta:
        model = models.StatusCOR
        fields = "__all__"


class StatusCORAdmin(admin.ModelAdmin):
    form = StatusCORAdminForm
    list_display = [
        "created",
        "quality_category",
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
        "status",
        "accepted_status",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "end_date",
        "status",
        "accepted_status",
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
        "description",
        "created",
        "title",
        "last_updated",
        "labor",
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
        "description",
        "logo",
        "contacts",
        "title",
        "created",
        "url",
    ]


class ResultEduResourcesAdminForm(forms.ModelForm):
    class Meta:
        model = models.ResultEduResources
        fields = "__all__"


class ResultEduResourcesAdmin(admin.ModelAdmin):
    form = ResultEduResourcesAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


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
        "description",
        "last_updated",
        "created",
        "short_description",
        "title",
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
        "rate",
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
        "title",
        "last_updated",
        "created",
        "description",
    ]


class DigitalResourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.DigitalResource
        fields = "__all__"


class DigitalResourceAdmin(admin.ModelAdmin):
    form = DigitalResourceAdminForm
    list_display = [
        "id",
        "title",
        "created",
        "type",
        "source_data",
        "last_updated",
        "ketwords",
        "description",
    ]
    readonly_fields = [
        "id",
        "title",
        "created",
        "type",
        "source_data",
        "last_updated",
        "ketwords",
        "description",
    ]


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
        "title",
        "code",
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
        "created",
        "url",
        "logo",
        "description",
        "contacts",
        "title",
    ]


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = [
        "code",
        "titile",
        "created",
    ]
    readonly_fields = [
        "code",
        "titile",
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


class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = [
        "academic_group",
        "created",
    ]
    readonly_fields = [
        "academic_group",
        "created",
    ]


class ConformityThemesAdminForm(forms.ModelForm):
    class Meta:
        model = models.ConformityThemes
        fields = "__all__"


class ConformityThemesAdmin(admin.ModelAdmin):
    form = ConformityThemesAdminForm
    list_display = [
        "practice",
        "theory",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "practice",
        "theory",
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
        "description",
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
        "title",
    ]


class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = "__all__"


class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = [
        "location",
        "date_birthday",
        "city",
        "created",
        "middle_name",
        "country",
        "first_name",
        "avatar",
        "last_name",
    ]
    readonly_fields = [
        "location",
        "date_birthday",
        "city",
        "created",
        "middle_name",
        "country",
        "first_name",
        "avatar",
        "last_name",
    ]


admin.site.register(models.StatusCOR, StatusCORAdmin)
admin.site.register(models.ExpertiseStatus, ExpertiseStatusAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.ResultEduResources, ResultEduResourcesAdmin)
admin.site.register(models.EduProgram, EduProgramAdmin)
admin.site.register(models.ProvidingDiscipline, ProvidingDisciplineAdmin)
admin.site.register(models.ResultEdu, ResultEduAdmin)
admin.site.register(models.DigitalResource, DigitalResourceAdmin)
admin.site.register(models.Competence, CompetenceAdmin)
admin.site.register(models.Platform, PlatformAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.SubjectTag, SubjectTagAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.ConformityThemes, ConformityThemesAdmin)
admin.site.register(models.EduProgramTag, EduProgramTagAdmin)
admin.site.register(models.SubjectTheme, SubjectThemeAdmin)
admin.site.register(models.ThematicPlan, ThematicPlanAdmin)
admin.site.register(models.Person, PersonAdmin)
