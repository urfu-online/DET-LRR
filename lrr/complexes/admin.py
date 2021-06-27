# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter)

from lrr.complexes import forms_admin
from lrr.complexes import grid_models
from lrr.complexes import models


@admin.register(grid_models.Container)
class ContainerAdmin(admin.ModelAdmin):
    form = forms_admin.ContainerAdminForm
    list_display = [
        "type",
    ]
    readonly_fields = [
        "type",
    ]


@admin.register(grid_models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    form = forms_admin.ThemeAdminForm
    list_display = [
        "title",
    ]
    readonly_fields = [
        "title",
    ]


# @admin.register(grid_models.Cell)
# class CellAdmin(admin.ModelAdmin):
#     form = forms_admin.CellAdminForm
#     list_display = [
#     ]
#     readonly_fields = [
#     ]


@admin.register(models.ComponentComplex)
class ComponentAdmin(ImportExportModelAdmin):
    form = forms_admin.ComponentForm
    list_display = [
        "__str__",
    ]


# class ComplexSpaceCellInline(admin.TabularInline):
#     model = models.ComplexSpaceCell
#     list_display = [
#         "title",
#         "description",
#         "cells",
#         "digital_complex",
#         "link"
#     ]
#     readonly_fields = [
#         "created",
#     ]
#     extra = 0
#     autocomplete_fields = ['digital_complex', ]


class WorkPlanAcademicGroupAdminInline(admin.TabularInline):
    list_display = [
        "academic_group",
        "learn_date",
    ]
    readonly_fields = [
        "created",
    ]


@admin.register(models.DigitalComplex)
class DigitalComplexAdmin(ImportExportModelAdmin):
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
        "form_control"
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
        # ComplexSpaceCellInline,
        # DRStatusInline
    ]
    # filter_horizontal = ["subjects_tags", ]
    autocomplete_fields = ["subjects", "competences", "results_edu", "directions"]
    list_filter = ["form_control"]
    search_fields = ["keywords", "format"]


@admin.register(models.AssignmentAcademicGroup)
class AssignmentAcademicGroupAdmin(ImportExportModelAdmin):
    form = forms_admin.AssignmentAcademicGroupForm
    list_display = [
        "academic_group",
        "learn_date"
    ]
    readonly_fields = [
        "created",
    ]

    autocomplete_fields = ["digital_complex"]


# @admin.register(models.ComponentComplex)
class ComponentComplexChildAdmin(PolymorphicChildModelAdmin):
    base_model = models.ComponentComplex


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


# @admin.register(models.ComponentComplex)
class ComponentComplexChiledAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.ComponentComplex
    search_fields = ["digital_complex__title", "digital_complex__keywords", "digital_complex__format"]


@admin.register(models.ResourceComponent)
class ResourceComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.ResourceComponent
    search_fields = ["digital_resource__title", ]
    autocomplete_fields = ["digital_resource", ]


@admin.register(models.PlatformComponent)
class PlatformComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.PlatformComponent
    search_fields = ["title", ]


@admin.register(models.LiterarySourcesComponent)
class LiterarySourcesComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.LiterarySourcesComponent
    search_fields = ["title", ]
    # autocomplete_fields = ["title", ]


#
@admin.register(models.TraditionalSessionComponent)
class TraditionalSessionComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.TraditionalSessionComponent
    search_fields = ["title", ]
    # autocomplete_fields = ["title", ]
