from django import forms
from django.contrib import admin

from . import models


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
    search_fields = ["title", ]


class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Source
        fields = "__all__"


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    form = SourceAdminForm
    search_fields = ["link_name", "digital_resource__title", "URL"]
    list_display = [
        "get_link_name",
        "digital_resource",
        "URL",
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
    search_fields = ["title"]


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Competence
        fields = "__all__"


class CompetenceAdmin(admin.ModelAdmin):
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
    search_fields = ["title", "url", "id", ]


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"


class LanguageAdmin(admin.ModelAdmin):
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


class SubjectTagAdmin(admin.ModelAdmin):
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
    search_fields = ["tag__title"]


class DirectionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Direction
        fields = "__all__"


class DirectionAdmin(admin.ModelAdmin):
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
class ScientificBranchAdmin(admin.ModelAdmin):
    form = ScientificBranchAdminForm
    list_display = ["code", "title", ]
    readonly_fields = ["created", ]
    search_fields = ["title"]


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
