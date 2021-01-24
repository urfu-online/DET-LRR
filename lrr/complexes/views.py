# -*- coding: utf-8 -*-

import logging

import django_filters
from django.shortcuts import render, get_object_or_404
from django.views import generic

from lrr.complexes import forms
from lrr.complexes import models as complex_model
from lrr.repository.filters import FilteredListView
from lrr.users.models import Person, Student

# import logging
#
logger = logging.getLogger(__name__)


def WorkPlanView(request):
    person = get_object_or_404(Person, user=request.user)
    academic_group = get_object_or_404(Student, person=Person.objects.get(user=request.user)).academic_group
    obj_plan = complex_model.WorkPlanAcademicGroup.objects.filter(academic_group=academic_group)
    return render(request, 'pages/work_plan_list.html',
                  {'academic_group': academic_group, 'obj_plan': obj_plan, 'person': person,  # 'status': status,
                   'DR': obj_plan[0].digital_resource.first()})


class DigitalComplexFilter(django_filters.FilterSet):
    class Meta:
        model = complex_model.DigitalComplex
        fields = {
            'keywords': ['contains'],
            'format': ['contains'],
            'language': ['exact'],
            'directions': ['exact'],
            'competences': ['exact'],
        }


# "keywords",
# "description",
# "language",
# "format",
# "subjects",
# "directions",
# "competences",
# "results_edu",
# "digital_resources",


class DigitalComplexListView(FilteredListView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalComplexFilter


class DigitalComplexMyListView(FilteredListView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalComplexFilter
    template_name = 'complexes/teacher/digitalcomplex_my_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_complexes'] = complex_model.DigitalComplex.objects.filter(owner__user=self.request.user)
        return context

    def get_queryset(self):
        queryset = complex_model.DigitalComplex.objects.filter(owner__user=self.request.user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class DigitalComplexCreateView(generic.CreateView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_form.html'

    def form_valid(self, form):
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.save()
        form_valid = super(DigitalComplexCreateView, self).form_valid(form)
        return form_valid


class DigitalComplexDetailView(generic.DetailView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_detail.html'


class DigitalComplexUpdateView(generic.UpdateView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_form.html'

    def form_valid(self, form):
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.save()
        form_valid = super(DigitalComplexUpdateView, self).form_valid(form)
        return form_valid
