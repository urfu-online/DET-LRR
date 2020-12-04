# -*- coding: utf-8 -*-
from django.contrib import admin

from lrr.complexes import forms
from lrr.complexes import models


@admin.register(models.ComplexSpaceCell)
class ComplexSpaceCellInline(admin.TabularInline):
    model = models.ComplexSpaceCell
    list_display = [
        "title",
        "description",
        "cells",
    ]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = [
        "title",
        "description",
    ]


@admin.register(models.DigitalComplex)
class DigitalComplexAdmin(admin.ModelAdmin):
    form = forms.DigitalComplexAdminForm
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
        "space_cell",
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
        # DRStatusInline
    ]
    # filter_horizontal = ["subjects_tags", ]
    # autocomplete_fields = ["subjects_tags", "provided_disciplines", "copyright_holder", "edu_programs_tags", "platform",
    #                        "language"]
    # list_filter = ["platform"]
    # search_fields = ["title"]


@admin.register(models.Cell)
class Cell(admin.ModelAdmin):
    form = models.Cell
    fields = "__all__"
    list_display = [
        "title",
        "description",
        "cells",
    ]
    readonly_fields = [
        "created",
    ]
    extra = 0
    autocomplete_fields = [
        "title",
        "description",
    ]
