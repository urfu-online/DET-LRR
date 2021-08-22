# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_json_widget.widgets import JSONEditorWidget
from django_reverse_admin import ReverseModelAdmin
from easy_select2 import select2_modelform
from django.db.models import JSONField
from lrr.inspections import forms_admin
from lrr.inspections import models


class CheckListInline(admin.TabularInline):
    model = models.ExpertiseRequest
    list_display = [
        "type",
        "expert",
        "date",
        "protocol",
    ]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = ["expertise"]


@admin.register(models.Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    form = forms_admin.ExpertiseAdminForm
    fields = [
        "digital_resource",
        "date",
        "subjects",
        "directions",
        "digital_complexes",
        "expert",
        "date_end",
        "file",
        "remarks",
        "status",
        "owner",
    ]
    list_display = [
        "digital_resource",
        "date_end",
        "status",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]
    inlines = [
        CheckListInline,
        # DRStatusInline
    ]
    filter_horizontal = ["subjects", "expert", ]
    autocomplete_fields = []
    # list_filter = ["platform"]
    search_fields = ["type"]


@admin.register(models.ExpertiseRequest)
class ExpertiseRequestAdmin(admin.ModelAdmin):
    form = forms_admin.ExpertiseRequestAdminForm

    list_display = ['survey', 'expert', 'status', 'expertise', 'created']
    extra = 0


@admin.register(models.IndicatorGroup)
class IndicatorGroupAdmin(admin.ModelAdmin):
    model = models.IndicatorGroup
    list_display = ["title"]
    search_fields = ["indicator"]


IndicatorForm = select2_modelform(models.Indicator, attrs={'width': '274px'})


def bind_questions(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.bind_question()


bind_questions.short_description = _('Bind questions to indicators')


@admin.register(models.Indicator)
class IndicatorAdmin(ReverseModelAdmin, DynamicArrayMixin):
    form = IndicatorForm
    list_display = ["title", "group", "values", "num_values", "question"]
    fields = ["title", "group", "values", "json_values", "num_values"]
    search_fields = ["title", "group__title"]
    list_filter = ["group", "question"]
    autocomplete_fields = ["group"]
    inline_type = 'tabular'
    inline_reverse = [('question', {'fields': ('text', 'order', 'required', 'category', 'survey', 'type', 'choices')})]
    actions = [bind_questions]

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


class StatusRequirementInline(admin.TabularInline):
    model = models.StatusRequirement
    autocomplete_fields = ["indicator"]
    extra = 0
    ordering = ["indicator__id"]
    readonly_fields = ["indicator"]
    fields = ["indicator", "allowed_values", "exclude_values", "allowed_num_values"]
    can_delete = False


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ["title", "group"]
    fields = ["title", "group"]
    search_fields = ["title", StatusRequirementInline]
    list_filter = ["group"]
    inlines = [
        StatusRequirementInline,
    ]
    # autocomplete_fields = [StatusRequirementInline]


@admin.register(models.TemporaryStatus)
class TemporaryStatus(admin.ModelAdmin):
    list_display = ["expertise", "name", "date"]
    fields = ["expertise", "name", "date"]
