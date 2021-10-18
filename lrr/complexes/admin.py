# -*- coding: utf-8 -*-
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.db.models import JSONField
from django.utils.html import format_html_join
from django_json_widget.widgets import JSONEditorWidget
from import_export.admin import ImportExportModelAdmin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter)

from lrr.complexes import grid_models
from lrr.complexes import models


class ThemeAdminInline(SortableInlineAdminMixin, admin.StackedInline):
    model = grid_models.Theme
    extra = 1


@admin.register(grid_models.ThematicPlan)
class ThematicPlanAdmin(admin.ModelAdmin):
    autocomplete_fields = ['digital_complex']
    list_display = [
        'digital_complex',
        'themes',
        'created',
        'last_updated',
    ]
    inlines = [ThemeAdminInline]

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description='Темы')
    def themes(self, obj):
        return format_html_join(
            '\n', '<p>{}</p>',
            [[t.title] for t in obj.themes.all()]
        )


class ThematicPlanAdminInline(admin.StackedInline):
    model = grid_models.ThematicPlan
    list_display = [
        'plan_object',
    ]
    min_num = 1
    max_num = 1

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(models.ComponentComplex)
class ComponentAdmin(ImportExportModelAdmin):
    list_display = [
        '__str__',
    ]


class WorkPlanAcademicGroupAdminInline(admin.TabularInline):
    list_display = [
        'academic_group',
        'learn_date',
    ]
    readonly_fields = [
        'created',
    ]


@admin.register(models.DigitalComplex)
class DigitalComplexAdmin(ImportExportModelAdmin):
    fields = [
        'title',
        'keywords',
        'description',
        'language',
        'format',
        'subjects',
        'directions',
        'competences',
        'form_control',
    ]
    list_display = [
        'title',
        'description',
        'view_keywords',
        'format',
    ]
    readonly_fields = [
        'id',
        'created',
        'last_updated',
    ]
    inlines = [
        ThematicPlanAdminInline
    ]

    autocomplete_fields = ['subjects', 'competences', 'results_edu', 'directions']
    list_filter = ['form_control', 'format']
    search_fields = ['title', 'description', 'view_keywords']

    @admin.display(description='Ключевые слова')
    def view_keywords(self, obj):
        return format_html_join(
            '\n', '<tag>{}</tag>',
            [[o.name] for o in obj.keywords.all()]
        )


@admin.register(models.AssignmentAcademicGroup)
class AssignmentAcademicGroupAdmin(ImportExportModelAdmin):
    fields = [
        "digital_complex",
        "academic_group",
        "group_subject",
        "learn_date"
    ]
    list_display = [
        'academic_group',
        'learn_date'
    ]
    readonly_fields = [
        'created',
    ]
    autocomplete_fields = ['digital_complex', 'academic_group', 'group_subject']


# @admin.register(models.ComponentComplex)
class ComponentComplexChildAdmin(PolymorphicChildModelAdmin):
    base_model = models.ComponentComplex


class ComponentComplexParentAdmin(PolymorphicParentModelAdmin):
    base_model = models.ComponentComplex
    search_fields = ['digital_complex__title', 'digital_complex__keywords', 'digital_complex__format']
    # form = ProgramComponentForm
    # autocomplete_fields = ['logistical_resource', 'personnel_resource', 'digital_resource', 'competence']
    child_models = (
        models.ResourceComponent,
        models.PlatformComponent,
        models.TraditionalSessionComponent,
        models.ComponentComplex
    )

    list_filter = (PolymorphicChildModelFilter,)
    fields = ('digital_complex', 'description')


# @admin.register(models.ComponentComplex)
class ComponentComplexChiledAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.ComponentComplex
    search_fields = ['digital_complex__title', 'digital_complex__keywords', 'digital_complex__format']


@admin.register(models.ResourceComponent)
class ResourceComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.ResourceComponent
    search_fields = ['digital_resource__title', ]
    autocomplete_fields = ['digital_resource', ]


@admin.register(models.PlatformComponent)
class PlatformComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.PlatformComponent
    search_fields = ['title', ]


@admin.register(models.LiterarySourcesComponent)
class LiterarySourcesComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.LiterarySourcesComponent
    search_fields = ['title', ]


@admin.register(models.TraditionalSessionComponent)
class TraditionalSessionComponentAdmin(ComponentComplexChildAdmin, ImportExportModelAdmin):
    base_model = models.TraditionalSessionComponent
    search_fields = ['title', ]
