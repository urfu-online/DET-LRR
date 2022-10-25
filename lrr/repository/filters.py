import logging

import django_filters
from crispy_forms.helper import FormHelper
from django import forms
from django.core.paginator import Paginator
from django.views.generic import ListView
from django_filters.views import FilterView
from django_select2.forms import Select2Widget
from easy_select2 import Select2Multiple, Select2

from . import models

logger = logging.getLogger(__name__)


class ThemedSelect2Multiple(Select2Multiple):
    class Media:
        css = {
            'all': ('css/select2-bootstrap4.min.css',),
        }


class ThemedSelect2(Select2):
    class Media:
        css = {
            'all': ('css/select2-bootstrap4.min.css',),
        }


class FilteredListView(ListView, FilterView):
    allow_empty = True
    filterset_class = None
    filterset = None
    paginator_class = Paginator
    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset

    def get_paginator(self, queryset, per_page, orphans=3,
                      allow_empty_first_page=True, **kwargs):
        """Return an instance of the paginator for this view."""
        return self.paginator_class(
            queryset, per_page, orphans=orphans,
            allow_empty_first_page=self.allow_empty, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs  # .distinct()
        if not qs.exists():
            self.paginate_by = None
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class DigitalResourceFilterForm(forms.ModelForm):
    class Meta:
        model = models.DigitalResource
        fields = ['title', 'type', 'copyright_holder', 'platform', 'language', 'subjects_tags', 'edu_programs_tags']

        # widgets = {
        #     'platform': ThemedSelect2(select2attrs={'width': 'auto'}),
        #     'copyright_holder': ThemedSelect2(select2attrs={'width': 'auto'}),
        #     'subjects_tags': ThemedSelect2Multiple(select2attrs={'width': 'auto'}),
        #     'edu_programs_tags': ThemedSelect2Multiple(select2attrs={'width': 'auto'}),
        #     'type': ThemedSelect2(select2attrs={'width': 'auto'})
        #
        # }

    def __init__(self, *args, **kwargs):
        super(DigitalResourceFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            logger.info(f"{field}")
            # field.required = False
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-row'
        self.helper.disable_csrf = False
        self.helper.form_style = 'default'
        self.helper.render_required_fields = False
        # self.helper.layout = Layout(
        #     Div(
        #         Row(
        #             Column('subjects_tags', css_class='form-group col-12'),
        #             Column('edu_programs_tags', css_class='form-group col-12'),
        #
        #         ),
        #         Div(
        #             Column('title', css_class='form-group col-12 col-md-6'),
        #             Column('type', css_class='form-group col-12  col-md-6'),
        #             Column('copyright_holder', css_class='form-group col-12  col-md-6'),
        #             Column('platform', css_class='form-group col-12 col-md-6'),
        #             Column('language', css_class='form-group col-12 col-md-6'),
        #             css_class='row'),
        #         css_class="well")
        # )


class BookmarkDigitalResourceFilterForm(forms.ModelForm):
    class Meta:
        model = models.BookmarkDigitalResource
        fields = '__all__'
        exclude = ['user', 'obj']

        # widgets = {
        #     'platform': ThemedSelect2(select2attrs={'width': 'auto'}),
        #     'copyright_holder': ThemedSelect2(select2attrs={'width': 'auto'}),
        #     'subjects_tags': ThemedSelect2Multiple(select2attrs={'width': 'auto'}),
        #     'edu_programs_tags': ThemedSelect2Multiple(select2attrs={'width': 'auto'}),
        #     'type': ThemedSelect2(select2attrs={'width': 'auto'})
        #
        # }

    def __init__(self, *args, **kwargs):
        super(BookmarkDigitalResourceFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            logger.info(f"{field}")
            # field.required = False
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-row'
        self.helper.disable_csrf = False
        self.helper.form_style = 'default'
        self.helper.render_required_fields = False
        # self.helper.layout = Layout(
        #     Div(
        #         Row(
        #             Column('subjects_tags', css_class='form-group col-12'),
        #             Column('edu_programs_tags', css_class='form-group col-12'),
        #
        #         ),
        #         Div(
        #             Column('title', css_class='form-group col-12 col-md-6'),
        #             Column('type', css_class='form-group col-12  col-md-6'),
        #             Column('copyright_holder', css_class='form-group col-12  col-md-6'),
        #             Column('platform', css_class='form-group col-12 col-md-6'),
        #             Column('language', css_class='form-group col-12 col-md-6'),
        #             css_class='row'),
        #         css_class="well")
        # )


class DigitalResourceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr="icontains", label="Наименование")
    type = django_filters.ChoiceFilter(field_name='type', choices=models.DigitalResource.RESOURCE_TYPE, label="Тип")
    copyright_holder = django_filters.ModelChoiceFilter(field_name='copyright_holder', queryset=models.Organization.objects.all(), label="Правообладатель")
    platform = django_filters.ModelChoiceFilter(field_name='platform', queryset=models.Platform.objects.all(), label="Платформа")
    language = django_filters.ModelChoiceFilter(field_name='language', queryset=models.Language.objects.all(), label="Язык")
    subjects_tags = django_filters.ModelChoiceFilter(field_name='subjects_tags__tag__title', queryset=models.Subject.objects.all(), lookup_expr="icontains", widget=Select2Widget, label="Дисциплины")
    edu_programs_tags = django_filters.ModelChoiceFilter(field_name='edu_programs_tags__tag__title', lookup_expr="icontains", queryset=models.EduProgram.objects.all(), widget=Select2Widget, label="Направление / ОП")

    class Meta:
        form = DigitalResourceFilterForm
        model = models.DigitalResource
        fields = ['title', 'type', 'copyright_holder', 'platform', 'language', 'subjects_tags', 'edu_programs_tags', ]


class DigitalResourceBookmarkFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='obj__title', lookup_expr="icontains", label="Наименование")
    type = django_filters.ChoiceFilter(field_name='obj__type', choices=models.DigitalResource.RESOURCE_TYPE, label="Тип")
    copyright_holder = django_filters.ModelChoiceFilter(field_name='obj__copyright_holder', queryset=models.Organization.objects.all(), label="Правообладатель")
    platform = django_filters.ModelChoiceFilter(field_name='obj__platform', queryset=models.Platform.objects.all(), label="Платформа")
    language = django_filters.ModelChoiceFilter(field_name='obj__language', queryset=models.Language.objects.all(), label="Язык")
    subjects_tags = django_filters.ModelChoiceFilter(field_name='obj__subjects_tags__tag__title', queryset=models.Subject.objects.all(), lookup_expr="exact", widget=Select2Widget, label="Дисциплины")
    edu_programs_tags = django_filters.ModelChoiceFilter(field_name='obj__edu_programs_tags__tag__title', queryset=models.EduProgram.objects.all(), lookup_expr="exact", widget=Select2Widget, label="Направление / ОП")

    class Meta:
        model = models.BookmarkDigitalResource
        form = BookmarkDigitalResourceFilterForm
        fields = ['title', 'type', 'copyright_holder', 'platform', 'language', 'subjects_tags', 'edu_programs_tags', ]
        exclude = ['user', 'obj']

        # fields = {
        #     'obj__title': ['icontains'],
        #     'type': ['exact'],
        #     'obj__copyright_holder': ['exact'],
        #     'obj__platform': ['exact'],
        #     'obj__language': ['exact'],
        #     'obj__subjects_tags__tag__title': ['icontains'],
        #     'obj__edu_programs_tags__tag__title': ['icontains'],
        # }
