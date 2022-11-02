from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export_celery.admin_actions import create_export_job_action
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from . import models
from .models import EduProgramSubject, SubjectChild, EduProgramChild


class EduProgramSubjectChildAdmin(PolymorphicChildModelAdmin):
    base_model = EduProgramSubject


@admin.register(SubjectChild)
class SubjectChildAdmin(EduProgramSubjectChildAdmin):
    base_model = SubjectChild  # Explicitly set here!
    show_in_index = False
    autocomplete_fields = ["subject"]


@admin.register(EduProgramChild)
class EduProgramChildAdmin(EduProgramSubjectChildAdmin):
    base_model = EduProgramChild  # Explicitly set here!
    show_in_index = False
    autocomplete_fields = ["program"]


@admin.register(EduProgramSubject)
class EduProgramSubjectParentAdmin(PolymorphicParentModelAdmin):
    child_models = (SubjectChild, EduProgramChild)
    list_filter = (PolymorphicChildModelFilter,)
    polymorphic_list = True


class SubjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = "__all__"


class SubjectAdmin(ImportExportModelAdmin):
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


class OrganizationAdmin(ImportExportModelAdmin):
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


class EduProgramAdmin(ImportExportModelAdmin):
    form = EduProgramAdminForm
    search_fields = ["title"]
    list_display = [
        "title",
        "cipher",
        "standard",
        "approve_year",
        "admission_years",
        "head",
        "site_admin"
    ]
    list_filter = ["standard"]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class ResultEduAdminForm(forms.ModelForm):
    class Meta:
        model = models.ResultEdu
        fields = "__all__"


class ResultEduAdmin(ImportExportModelAdmin):
    form = ResultEduAdminForm
    list_display = [
        "title",
        "competence"
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]
    search_fields = ["title", ]


class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Source
        fields = "__all__"


@admin.register(models.Source)
class SourceAdmin(ImportExportModelAdmin):
    form = SourceAdminForm
    search_fields = ["link_name", "digital_resource__title", "URL"]
    list_display = [
        "get_link_name",
        "digital_resource",
        "URL",
        "type",
    ]
    actions = ['update_source_type']

    def update_source_type(modeladmin, request, queryset):
        for source in queryset:
            source.update_type()

    update_source_type.short_description = "Обновить тип компонентов"


class DigitalResourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.DigitalResource
        fields = "__all__"


class SourceInline(admin.TabularInline):
    model = models.Source
    extra = 1


@admin.register(models.DigitalResource)
class DigitalResourceAdmin(ImportExportModelAdmin):
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

        "edu_programs_tags",
        "owner",
        "result_edu",
        "subjects_tags",
        "created",
        "last_updated",
    ]
    list_display = [
        "title",
        "type",
        "source_data",
        "copyright_holder",
        "created",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]
    inlines = [
        SourceInline,
    ]
    # filter_horizontal = ["subjects_tags", ]
    autocomplete_fields = ["subjects_tags", "copyright_holder", "edu_programs_tags", "platform",
                           "language"]
    list_filter = ["platform"]
    search_fields = ["title", "description", ]
    actions = (create_export_job_action,)


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = "__all__"


class CompetenceAdmin(ImportExportModelAdmin):
    form = CompetenceAdminForm
    list_filter = ["okso", "code"]
    list_display = [
        "title",
        "code",
    ]
    readonly_fields = [
        "created",
    ]
    search_fields = ["title", "code", 'okso']


class PlatformAdminForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = "__all__"


class PlatformAdmin(ImportExportModelAdmin):
    form = PlatformAdminForm
    list_display = [
        "title",
        "url",
        "id",
    ]
    readonly_fields = [
        "created"
    ]
    search_fields = ["title", "url", "id", ]


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"


class LanguageAdmin(ImportExportModelAdmin):
    form = LanguageAdminForm
    list_display = [
        "code",
        "title",
        "pk"
    ]
    readonly_fields = [
        "created",
    ]
    search_fields = ["code", "title", ]


class SubjectTagAdminForm(forms.ModelForm):
    class Meta:
        model = models.SubjectTag
        fields = "__all__"


class SubjectTagAdmin(ImportExportModelAdmin):
    form = SubjectTagAdminForm
    search_fields = ["tag__title"]
    list_display = [
        "tag",
        "created",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class EduProgramTagAdminForm(forms.ModelForm):
    class Meta:
        model = models.EduProgramTag
        fields = "__all__"


class EduProgramTagAdmin(ImportExportModelAdmin):
    form = EduProgramTagAdminForm
    list_display = [
        "tag",
        "created",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    search_fields = ["tag__title"]


class DirectionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Direction
        fields = "__all__"


class DirectionAdmin(ImportExportModelAdmin):
    form = DirectionAdminForm
    list_display = [
        "code",
        "title",
    ]
    readonly_fields = [
        "created",
    ]
    list_filter = ["scientific_branch"]
    search_fields = ["title", "code"]


class ScientificBranchAdminForm(forms.ModelForm):
    class Meta:
        model = models.ScientificBranch
        fields = "__all__"


@admin.register(models.ScientificBranch)
class ScientificBranchAdmin(ImportExportModelAdmin):
    form = ScientificBranchAdminForm
    list_display = ["code", "title", ]
    readonly_fields = ["created", ]
    search_fields = ["title"]


class BookmarkDigitalResourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.BookmarkDigitalResource
        fields = "__all__"


@admin.register(models.BookmarkDigitalResource)
class BookmarkDigitalResourceAdmin(ImportExportModelAdmin):
    form = BookmarkDigitalResourceAdminForm
    list_display = ["obj", "user", ]
    readonly_fields = ["created", ]
    search_fields = ["obj"]


admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.EduProgram, EduProgramAdmin)
admin.site.register(models.ResultEdu, ResultEduAdmin)
admin.site.register(models.Competence, CompetenceAdmin)
admin.site.register(models.Platform, PlatformAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.SubjectTag, SubjectTagAdmin)
admin.site.register(models.EduProgramTag, EduProgramTagAdmin)
admin.site.register(models.Direction, DirectionAdmin)
