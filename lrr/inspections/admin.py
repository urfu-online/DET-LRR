# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from lrr.inspections import models


class CheckListInline(admin.TabularInline):
    model = models.ExpertiseOpinion
    list_display = [
        'expert',
        'date',
        'protocol',
        'expertise_type'
    ]
    readonly_fields = [
        'created',
    ]
    extra = 0
    autocomplete_fields = ['request', 'expert', 'expertise_type']


class CategoryInline(admin.TabularInline):
    model = models.Category
    extra = 0


class IndicatorInline(admin.StackedInline):
    model = models.Indicator
    ordering = ('order', 'category')
    autocomplete_fields = ['discipline']
    extra = 1

    def get_formset(self, request, expertise_type_obj, *args, **kwargs):
        formset = super(IndicatorInline, self).get_formset(request, expertise_type_obj, *args, **kwargs)
        if expertise_type_obj:
            formset.form.base_fields['category'].queryset = expertise_type_obj.categories.all()
        return formset


@admin.register(models.ExpertiseType)
class ExpertiseTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'template')
    inlines = [CategoryInline, IndicatorInline]
    search_fields = ['title']
    save_on_top = True


class OpinionIndicatorBaseInline(admin.StackedInline):
    fields = ('indicator', 'discipline', 'body')
    readonly_fields = ('indicator', 'discipline', 'body')
    autocomplete_fields = ['discipline']
    extra = 0
    model = models.OpinionIndicator


@admin.register(models.ExpertiseOpinion)
class ExpertiseOpinionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'request',
        'expert',
        'date',
        'expertise_type'
    ]
    list_filter = ('expertise_type', 'created')
    autocomplete_fields = ['expert', 'request', 'expertise_type']
    date_hierarchy = 'created'
    inlines = [OpinionIndicatorBaseInline]
    readonly_fields = ('id', 'expertise_type', 'created', 'last_updated', 'expert')


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    model = models.Request
    fields = [
        'digital_resource',
        'date',
        'subjects',
        'directions',
        'digital_complexes',
        'expert',
        'status_text',
        'status',
        'date_end',
        'file',
        'remarks',

        'owner',
    ]
    list_display = [
        'digital_resource',
        'date_end',
        'status',
    ]
    readonly_fields = [
        'id',
        'created',
        'last_updated',
    ]
    inlines = [
        CheckListInline,
        # DRStatusInline
    ]
    filter_horizontal = ['subjects', 'expert', ]
    autocomplete_fields = ['owner', 'digital_resource', 'subjects', 'directions', 'expert', 'digital_complexes']
    # list_filter = ['platform']
    search_fields = ['type', 'digital_resource__title']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'expertise_type', 'order')
    list_filter = ('expertise_type', 'title')
    search_fields = ('expertise_type',)
    autocomplete_fields = ('expertise_type',)
    list_editable = ('expertise_type', 'order')


def bind_questions(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.bind_question()


def prefill_json_values(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.prefill_json_values()


def prefill_json_values_force(modeladmin, request, queryset):
    for indicator in queryset:
        indicator.prefill_json_values(force=True)


# bind_questions.short_description = _('Bind questions to indicators')
# prefill_json_values.short_description = _('Prefill `json_values` from `values` field')
# prefill_json_values_force.short_description = _('Force prefill `json_values` from `values` field')

#
# @admin.register(models.Indicator)
# class IndicatorAdmin(ReverseModelAdmin, DynamicArrayMixin):
#     form = IndicatorForm
#     list_display = ['title', 'group', 'values_map', 'has_question', 'per_discipline']
#     fields = ['title', 'group', 'values', 'json_values', 'num_values']
#     autocomplete_fields = ['group']
#     inline_type = 'tabular'
#     inline_reverse = [('question', {'fields': ('text', 'order', 'required', 'category', 'survey', 'type', 'choices')})]
#     actions = [bind_questions, prefill_json_values, prefill_json_values_force]
#     readonly_fields = ['has_question', 'values_map']
#     search_fields = ['title', 'group__title']
#
#     formfield_overrides = {
#         JSONField: {'widget': JSONEditorWidget},
#     }
#     ordering = ['question__group', 'question__order']
#
#     list_filter = (
#         'group__title',
#         ('question', admin.EmptyFieldListFilter),
#         ('json_values', admin.EmptyFieldListFilter),
#     )
#
#     @admin.display(description=_('Has question'), boolean=True)
#     def has_question(self, obj):
#         return True if obj.question else False
#
#     @admin.display(description=_('Values map'))
#     def values_map(self, obj):
#         if obj.json_values:
#             return mark_safe('<br>'.join(list([f'<strong>{v['value']}</strong>: {v['title']}' for v in sorted(obj.json_values, key=lambda i: i['value'])])))
#         if obj.num_values:
#             return mark_safe(f'{obj.num_values.lower} - {obj.num_values.upper}')


class StatusRequirementInline(admin.TabularInline):
    model = models.StatusRequirement
    # autocomplete_fields = ['indicator']
    extra = 0
    ordering = ['indicator__category', 'indicator__order']
    readonly_fields = ['indicator', 'values_map', 'per_discipline']
    fields = ['indicator', 'per_discipline', 'values_map', 'allowed_values', 'exclude_values', 'allowed_num_values', 'available']
    search_fields = ['indicator__title', 'indicator__text', 'indicator__group']
    can_delete = True

    def per_discipline(self, obj):
        return obj.indicator.per_discipline

    per_discipline.boolean = True
    per_discipline.short_description = 'Для каждой дисциплины'

    def values_map(self, obj):
        if obj.indicator.json_values:
            return mark_safe('<br>'.join(list([f'<strong>{v["value"]}</strong>: {v["title"]}' for v in sorted(obj.indicator.json_values, key=lambda i: i['value'])])))
        if obj.indicator.num_values:
            return mark_safe(f'{obj.indicator.num_values.lower} - {obj.indicator.num_values.upper}')


@admin.register(models.Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('text', 'order', 'category', 'expertise_type', 'type', 'discipline', 'choices')
    autocomplete_fields = ('discipline', 'category', 'expertise_type',)
    search_fields = ('text',)


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['title', 'group']
    fields = ['title', 'group']
    search_fields = ['title', StatusRequirementInline]
    list_filter = ['group']
    inlines = [
        StatusRequirementInline,
    ]


@admin.register(models.TemporaryStatus)
class TemporaryStatus(admin.ModelAdmin):
    list_display = ['request', 'name', 'date']
    fields = ['request', 'name', 'date']


@admin.register(models.AcceptableIndicatorValue)
class AcceptableIndicatorValueAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'value', 'entity', 'location', 'interaction', 'compliance', 'per_discipline', 'rating',)
    fields = ('indicator', 'value', 'entity', 'location', 'interaction', 'compliance', 'per_discipline', 'rating',)
    autocomplete_fields = ('indicator',)


@admin.register(models.SummaryIndicator)
class SummaryIndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'entity', 'location', 'interaction', 'compliance', 'per_discipline', 'rating',)
    fields = ('request', 'indicator', 'entity', 'location', 'interaction', 'compliance', 'per_discipline', 'rating', 'have_conflicts')
    autocomplete_fields = ('indicator', 'request')
