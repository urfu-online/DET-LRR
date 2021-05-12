# -*- coding: utf-8 -*-
from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

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
    # filter_horizontal = ["subjects_tags", ]
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


@admin.register(models.Indicator)
class IndicatorAdmin(admin.ModelAdmin, DynamicArrayMixin):
    model = models.Indicator
    list_display = ["title", "group", "values", "num_values"]
    fields = ["title", "group", "values", "num_values"]
    search_fields = ["title", "group__title"]
    list_filter = ["group"]
    autocomplete_fields = ["group"]


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ["title", "group"]
    fields = ["title", "group"]
    search_fields = ["title"]
    list_filter = ["group"]
