# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import JSONField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_json_widget.widgets import JSONEditorWidget
from django_reverse_admin import ReverseModelAdmin
from easy_select2 import select2_modelform

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


def prefill_json_values(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.prefill_json_values()


def prefill_json_values_force(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.prefill_json_values(force=True)


bind_questions.short_description = _('Bind questions to indicators')
prefill_json_values.short_description = _("Prefill `json_values` from `values` field")
prefill_json_values_force.short_description = _("Force prefill `json_values` from `values` field")


@admin.register(models.Indicator)
class IndicatorAdmin(ReverseModelAdmin, DynamicArrayMixin):
    form = IndicatorForm
    list_display = ["title", "group", "values_map", "has_question"]
    fields = ["title", "group", "values", "json_values", "num_values"]
    autocomplete_fields = ["group"]
    inline_type = 'tabular'
    inline_reverse = [('question', {'fields': ('text', 'order', 'required', 'category', 'survey', 'type', 'choices')})]
    actions = [bind_questions, prefill_json_values, prefill_json_values_force]
    readonly_fields = ["has_question", "values_map"]
    search_fields = ["title", "group"]

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    ordering = ["question__group", "question__order"]

    list_filter = (
        "group__title",
        ('question', admin.EmptyFieldListFilter),
        ('json_values', admin.EmptyFieldListFilter),
    )

    @admin.display(description=_("Has question"), boolean=True)
    def has_question(self, obj):
        return True if obj.question else False

    @admin.display(description=_("Values map"))
    def values_map(self, obj):
        if obj.json_values:
            return mark_safe("<br>".join(list([f"<strong>{v['value']}</strong>: {v['title']}" for v in sorted(obj.json_values, key=lambda i: i['value'])])))
        if obj.num_values:
            return mark_safe(f"{obj.num_values.lower} - {obj.num_values.upper}")


class StatusRequirementInline(admin.TabularInline):
    model = models.StatusRequirement
    autocomplete_fields = ["indicator"]
    extra = 0
    ordering = ["indicator__question__group", "indicator__question__order"]
    readonly_fields = ["indicator"]
    fields = ["indicator", "allowed_values", "exclude_values", "allowed_num_values"]
    search_fields = ["indicator__title", "indicator__question__text", "indicator__group"]
    can_delete = True


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
