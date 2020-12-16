# -*- coding: utf-8 -*-
from django.contrib import admin

from lrr.inspections import forms_admin
from lrr.inspections import models


class QuestionInline(admin.TabularInline):
    model = models.Question
    list_display = ["title", "answer"]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = ["checklist"]


class CheckListInline(admin.TabularInline):
    model = models.CheckList
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
        "direction",
        "digital_complex",
        "expert",
        "date_end",
        "file",
        "remarks",
        "status",
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


@admin.register(models.CheckList)
class CheckListAdmin(admin.ModelAdmin):
    form = forms_admin.CheckListAdminForm

    readonly_fields = [
        "created",
    ]
    extra = 0
    search_fields = ['title']
    inlines = [
        QuestionInline,
    ]
