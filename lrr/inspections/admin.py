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

    readonly_fields = [
        "created",
    ]
    extra = 0


@admin.register(models.CheckListQestion)
class CheckListQestionAdmin(admin.ModelAdmin):
    form = forms_admin.CheckListQestionAdminForm

    readonly_fields = [
        "created",
    ]
    extra = 0


# class CheckListBaseChildAdmin(PolymorphicChildModelAdmin):
#     base_model = models.CheckListBase
#
#
# @admin.register(models.CheckListBase)
# class CheckListBaseParentAdmin(PolymorphicParentModelAdmin):
#     base_model = models.CheckListBase
#     search_fields = ["protocol", "date", "expert"]
#     # form = ProgramComponentForm
#     # autocomplete_fields = ["logistical_resource", "personnel_resource", "digital_resource", "competence"]
#     child_models = (
#         models.CheckListMethodical,
#         models.CheckListTechnical,
#         models.CheckListContent
#     )
#
#     list_filter = (PolymorphicChildModelFilter,)
#     fields = ("date", "status")
#
#
# # @admin.register(models.CheckListBase)
# class CheckListBaseChiledAdmin(CheckListBaseChildAdmin):
#     base_model = models.CheckListBase
#     search_fields = ["protocol", "expert", ]
#     # autocomplete_fields = ["digital_resource", ]
#     # show_in_index = True
#
#
# @admin.register(models.CheckListMethodical)
# class CheckListMethodicalAdmin(CheckListBaseChildAdmin):
#     base_model = models.CheckListMethodical
#     search_fields = ["protocol", "expert", ]
#     # autocomplete_fields = ["digital_resource", ]
#     # show_in_index = True
#
#
# @admin.register(models.CheckListTechnical)
# class CheckListTechnicalAdmin(CheckListBaseChildAdmin):
#     base_model = models.CheckListTechnical
#     search_fields = ["protocol", "expert", ]
#     # show_in_index = True
#
#
# @admin.register(models.CheckListContent)
# class CheckListContentAdmin(CheckListBaseChildAdmin):
#     base_model = models.CheckListContent
#     search_fields = ["protocol", "expert", ]
#     # autocomplete_fields = ["title", ]
#     # show_in_index = True


@admin.register(models.Question)
class QestionAdmin(admin.ModelAdmin):
    form = forms_admin.QestionAdminForm

    readonly_fields = [
        "created",
    ]
    extra = 0


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    form = forms_admin.AnswerAdminForm

    readonly_fields = [
        "created",
    ]
    extra = 0
