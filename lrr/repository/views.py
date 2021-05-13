# -*- coding: utf-8 -*-
import json
import logging

import django_filters
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View

from lrr.inspections.models import Expertise
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person
from . import forms
from . import models
from .filters import FilteredListView

# Get an instance of a logger
logger = logging.getLogger(__name__)


class SubjectListView(generic.ListView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectCreateView(generic.CreateView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectDetailView(generic.DetailView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectUpdateView(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    pk_url_kwarg = "pk"


class OrganizationListView(generic.ListView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationCreateView(generic.CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationDetailView(generic.DetailView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationUpdateView(generic.UpdateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    pk_url_kwarg = "pk"


class EduProgramListView(generic.ListView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramCreateView(generic.CreateView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramDetailView(generic.DetailView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramUpdateView(generic.UpdateView):
    model = models.EduProgram
    form_class = forms.EduProgramForm
    pk_url_kwarg = "pk"


class ResultEduListView(generic.ListView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduCreateView(generic.CreateView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduDetailView(generic.DetailView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduUpdateView(generic.UpdateView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm
    pk_url_kwarg = "pk"


class DigitalResourceFilter(django_filters.FilterSet):
    class Meta:
        model = models.DigitalResource
        fields = {
            'title': ['icontains'],
            'type': ['exact'],
            'copyright_holder': ['exact'],
            'platform': ['exact'],
            'language': ['exact'],
            'subjects_tags__tag__title': ['icontains'],
            'edu_programs_tags__tag__title': ['icontains'],
        }


class DigitalResourceListView(FilteredListView):
    allow_empty = True
    paginate_by = 12
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    filterset_class = DigitalResourceFilter

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     product_filtered_list = DigitalResourceFilter(self.request.GET, queryset=qs)
    #     return product_filtered_list.qs


class ResourceListView(GroupRequiredMixin, FilteredListView):
    allow_empty = True
    paginate_by = 12
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    filterset_class = DigitalResourceFilter
    group_required = ['teacher', 'admins']
    template_name = "repository/digitalresource_list_owner.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['my_resources'] = models.DigitalResource.objects.filter(owner__user=self.request.user)
    #     return context

    def get_queryset(self):
        queryset = models.DigitalResource.objects.filter(owner__user=self.request.user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class DigitalResourceCreateView(GroupRequiredMixin, generic.CreateView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    group_required = ['teacher', 'admins']
    template_name = 'repository/digitalresource_form_create.html'

    def form_valid(self, form):
        context = self.get_context_data()
        source_formset = context['source_formset']
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.instance.source_data = "MANUAL"
        self.object = form.save()
        if source_formset.is_valid():
            source_formset.instance = self.object
            source_formset.save()
        form_valid = super(DigitalResourceCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.DigitalResourceForm(self.request.POST)
            context["source_formset"] = forms.SourceFormset(self.request.POST, self.request.FILES)
        else:
            context["form"] = forms.DigitalResourceForm()
            context["source_formset"] = forms.SourceFormset()
        return context


class DigitalResourceDetailView(GroupRequiredMixin, generic.DetailView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    group_required = ['teacher', 'admins']

    def get_context_data(self, **kwargs):
        context = super(DigitalResourceDetailView, self).get_context_data(**kwargs)
        context['expertise'] = Expertise.get_digital_resource_status(self.object)
        context['source'] = models.Source.objects.filter(digital_resource=self.object)
        # TODO: доделать нормальное отображение source
        return context


class DigitalResourceUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    group_required = ['teacher', 'admins']
    pk_url_kwarg = "pk"
    template_name = 'repository/digitalresource_form_update.html'

    def form_valid(self, form):
        context = self.get_context_data()
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form_valid = super(DigitalResourceUpdateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(DigitalResourceUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.DigitalResourceForm(self.request.POST, instance=self.object)
            # context["source_formset"] = forms.SourceFormset(self.request.POST, self.request.FILES, instance=self.object)
            source_formset = forms.SourceFormset(self.request.POST, self.request.FILES,
                                                 queryset=models.Source.objects.all(), instance=self.object)
            if source_formset.is_valid():
                source_formset.save()
        else:
            context["form"] = forms.DigitalResourceForm(instance=self.object)
            context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class CompetenceListView(generic.ListView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceCreateView(generic.CreateView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceDetailView(generic.DetailView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceUpdateView(generic.UpdateView):
    model = models.Competence
    form_class = forms.CompetenceForm
    pk_url_kwarg = "pk"


class PlatformListView(generic.ListView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformCreateView(generic.CreateView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformDetailView(generic.DetailView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformUpdateView(generic.UpdateView):
    model = models.Platform
    form_class = forms.PlatformForm
    pk_url_kwarg = "pk"


class LanguageListView(generic.ListView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageCreateView(generic.CreateView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageDetailView(generic.DetailView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageUpdateView(generic.UpdateView):
    model = models.Language
    form_class = forms.LanguageForm
    pk_url_kwarg = "pk"


class SubjectTagListView(generic.ListView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagCreateView(generic.CreateView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagDetailView(generic.DetailView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagUpdateView(generic.UpdateView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm
    pk_url_kwarg = "pk"


class EduProgramTagListView(generic.ListView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagCreateView(generic.CreateView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagDetailView(generic.DetailView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagUpdateView(generic.UpdateView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm
    pk_url_kwarg = "pk"


def statistics(request):
    context = dict()
    dp_count = str(models.DigitalResource.objects.count())
    context["dp_count"] = dp_count

    by_platform = dict()
    eduprograms = dict()
    for p in models.Platform.objects.all():
        by_platform[p.title] = models.DigitalResource.objects.filter(platform=p).count()

    for ep in models.EduProgram.objects.all():
        eduprograms[ep.title] = ep.get_count_resources()

    context["by_platform"] = by_platform
    context["eduprograms"] = eduprograms
    # context["stats_by_type"] = models.DigitalResource.get_stats_by_type()

    return render(request, "repository/report.html", context=context)


class BookmarkView(View):
    model = models.BookmarkDigitalResource

    def post(self, request, pk):
        # нам потребуется пользователь
        user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )


class DigitalResourceBookmarkFilter(django_filters.FilterSet):
    class Meta:
        model = models.BookmarkDigitalResource
        fields = {
            'obj__title': ['icontains'],
            'obj__type': ['exact'],
            'obj__copyright_holder': ['exact'],
            'obj__platform': ['exact'],
            'obj__language': ['exact'],
            'obj__subjects_tags__tag__title': ['icontains'],
            'obj__edu_programs_tags__tag__title': ['icontains'],
        }


class DigitalResourceBookmarkListView(FilteredListView):
    allow_empty = True
    paginate_by = 12
    model = models.BookmarkDigitalResource
    form_class = forms.DigitalResourceForm
    filterset_class = DigitalResourceBookmarkFilter

    # def get_queryset(self):
    #     queryset = models.BookmarkDigitalResource.objects.filter(obj__user=self.request.user)
    #     self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
    #     qs = self.filterset.qs.distinct()
    #     if qs.count() == 0:
    #         self.paginate_by = None
    #     return qs
