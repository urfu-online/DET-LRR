# -*- coding: utf-8 -*-
from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter)

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
    autocomplete_fields = ['digital_complex', ]


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
        "title",
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


@admin.register(models.AssignmentAcademicGroup)
class AssignmentAcademicGroupAdmin(admin.ModelAdmin):
    form = forms_admin.AssignmentAcademicGroupForm
    list_display = [
        "academic_group",
        "learn_date"
    ]
    readonly_fields = [
        "created",
    ]

    autocomplete_fields = ["subject", "digital_complex"]


class ComponentComplexChildAdmin(PolymorphicChildModelAdmin):
    base_model = models.ComponentComplex


# @admin.register(models.ComponentComplex)
class ComponentComplexParentAdmin(PolymorphicParentModelAdmin):
    base_model = models.ComponentComplex
    search_fields = ["digital_complex__title", "digital_complex__keywords", "digital_complex__format"]
    # form = ProgramComponentForm
    # autocomplete_fields = ["logistical_resource", "personnel_resource", "digital_resource", "competence"]
    child_models = (
        models.ResourceComponent,
        models.PlatformComponent,
        models.TraditionalSessionComponent,
        models.ComponentComplex
    )

    list_filter = (PolymorphicChildModelFilter,)
    fields = ("digital_complex", "description")


@admin.register(models.ComponentComplex)
class ComponentComplexChiledAdmin(ComponentComplexChildAdmin):
    base_model = models.ComponentComplex
    search_fields = ["digital_complex__title", "digital_complex__keywords", "digital_complex__format"]
    # autocomplete_fields = ["digital_resource", ]
    # show_in_index = True


@admin.register(models.ResourceComponent)
class ResourceComponentAdmin(ComponentComplexChildAdmin):
    base_model = models.ResourceComponent
    search_fields = ["digital_resource__title", ]
    autocomplete_fields = ["digital_resource", ]
    # show_in_index = True


@admin.register(models.PlatformComponent)
class PlatformComponentAdmin(ComponentComplexChildAdmin):
    base_model = models.PlatformComponent
    search_fields = ["platform__title", ]
    autocomplete_fields = ["platform", ]
    # show_in_index = True


@admin.register(models.LiterarySourcesComponent)
class LiterarySourcesComponentAdmin(ComponentComplexChildAdmin):
    base_model = models.LiterarySourcesComponent
    search_fields = ["title", ]
    # autocomplete_fields = ["title", ]


#
@admin.register(models.TraditionalSessionComponent)
class TraditionalSessionComponentAdmin(ComponentComplexChildAdmin):
    base_model = models.TraditionalSessionComponent
    search_fields = ["title", ]
    # autocomplete_fields = ["title", ]
    # show_in_index = True
