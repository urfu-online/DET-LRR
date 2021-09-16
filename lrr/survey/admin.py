# -*- coding: utf-8 -*-

from django.contrib import admin

from lrr.survey.actions import make_published
# from lrr.survey.exporter.csv import Survey2Csv
# from lrr.survey.exporter.tex import Survey2Tex
from lrr.survey.models import Answer, Category, Question, Response, Survey


class QuestionInline(admin.StackedInline):
    model = Question
    ordering = ("order", "category")
    extra = 1

    def get_formset(self, request, survey_obj, *args, **kwargs):
        formset = super(QuestionInline, self).get_formset(request, survey_obj, *args, **kwargs)
        if survey_obj:
            formset.form.base_fields["category"].queryset = survey_obj.categories.all()
        return formset


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "need_logged_user", "template")
    list_filter = ("is_published", "need_logged_user")
    inlines = [CategoryInline, QuestionInline]
    actions = [make_published]  # , Survey2Csv.export_as_csv, Survey2Tex.export_as_tex
    search_fields = ['name']
    save_on_top = True


class AnswerBaseInline(admin.StackedInline):
    fields = ("question", "discipline", "body")
    readonly_fields = ("question",)
    extra = 0
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("interview_uuid", "survey", "created", "user")
    list_filter = ("survey", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ("survey", "created", "updated", "interview_uuid", "user", "expertise_request")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "survey", "order")
    list_filter = ("survey", "name")
    search_fields = ['survey', ]
    autocomplete_fields = ['survey', ]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "survey", "order", "per_discipline")
    list_filter = ("survey", "category", "per_discipline")
    search_fields = ['text', 'survey__name', ]
    autocomplete_fields = ['survey', "category", "discipline"]
    readonly_fields = ("parent",)


# admin.site.register(Question, QuestionInline)
# admin.site.register(Category, CategoryInline)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)
