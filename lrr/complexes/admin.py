# -*- coding: utf-8 -*-
from django.contrib import admin

from lrr.complexes import forms_admin
from lrr.complexes import models


class ComplexSpaceCellInline(admin.TabularInline):
    model = models.ComplexSpaceCell
    list_display = [
        "title",
        "description",
        "cells",
        "digital_complex",
        "link"
    ]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = ['digital_complex', 'cells']


class CellWeeksInline(admin.TabularInline):
    model = models.CellWeeks
    list_display = ["beg_week_number", "end_week_number", "edu_form"]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = ["cell"]


class ComplexThemeAdminInline(admin.TabularInline):
    model = models.ComplexTheme
    list_display = ["title", "number"]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = ["digital_complex"]


class WorkPlanAcademicGroupAdminInline(admin.TabularInline):
    list_display = [
        "academic_group",
        "learn_date",
    ]
    readonly_fields = [
        "created",
    ]


@admin.register(models.DigitalComplex)
class DigitalComplexAdmin(admin.ModelAdmin):
    form = forms_admin.DigitalComplexAdminForm
    fields = [
        "keywords",
        "description",
        "language",
        "format",
        "subjects",
        "directions",
        "competences",
        "results_edu",
        "digital_resources",
    ]
    list_display = [
        "format",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]
    inlines = [
        ComplexSpaceCellInline,
        ComplexThemeAdminInline,
        # DRStatusInline
    ]
    # filter_horizontal = ["subjects_tags", ]
    autocomplete_fields = ["subjects", "competences", "results_edu", "directions", "digital_resources"]
    # list_filter = ["platform"]
    search_fields = ["keywords", "format"]


@admin.register(models.Cell)
class CellAdmin(admin.ModelAdmin):
    form = forms_admin.CellAdminForm

    readonly_fields = [
        "created",
    ]
    extra = 0
    search_fields = ['title']
    inlines = [
        CellWeeksInline,
    ]


@admin.register(models.WorkPlanAcademicGroup)
class WorkPlanAcademicGroupAdmin(admin.ModelAdmin):
    form = forms_admin.WorkPlanAcademicGroupAdminForm
    list_display = [
        "academic_group",
        "learn_date"
    ]
    readonly_fields = [
        "created",
    ]

    autocomplete_fields = ["subject", "digital_complex"]
