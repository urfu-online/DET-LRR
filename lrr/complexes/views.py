# -*- coding: utf-8 -*-


import logging

import django_filters
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from lrr.complexes import forms
from lrr.complexes import models as complex_model
from lrr.repository.filters import FilteredListView
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person, Student

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


class DigitalComplexMyListView(FilteredListView, GroupRequiredMixin):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalComplexFilter
    template_name = 'complexes/teacher/digitalcomplex_my_list.html'
    group_required = [u"teacher", u"admins"]

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


class DigitalComplexCreateView(generic.CreateView, GroupRequiredMixin):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_form.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.save()
        form_valid = super(DigitalComplexCreateView, self).form_valid(form)
        return form_valid


class DigitalComplexDetailView(generic.DetailView, GroupRequiredMixin):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_detail.html'
    group_required = [u"teacher", u"admins"]

    def get_context_data(self, **kwargs):
        context = super(DigitalComplexDetailView, self).get_context_data(**kwargs)
        component_complex = complex_model.ComponentComplex.objects.not_instance_of(complex_model.ResourceComponent,
                                                                                   complex_model.PlatformComponent,
                                                                                   complex_model.TraditionalSessionComponent)
        context['component_complex'] = component_complex.get(digital_complex=self.object)
        context['resource_components'] = complex_model.ResourceComponent.objects.filter(digital_complex=self.object)
        context['platform_components'] = complex_model.PlatformComponent.objects.filter(digital_complex=self.object)
        context['traditional_components'] = complex_model.TraditionalSessionComponent.objects.filter(
            digital_complex=self.object)
        return context


class DigitalComplexUpdateView(generic.UpdateView, GroupRequiredMixin):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_form.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.save()
        form_valid = super(DigitalComplexUpdateView, self).form_valid(form)
        return form_valid


class ComponentComplexCreateView(generic.CreateView, GroupRequiredMixin):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    template_name = 'complexes/teacher/componentcomplex_form_create.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        form.instance.digital_complex = complex_model.DigitalComplex.get_digital_complex(self)
        form.save()
        form_valid = super(ComponentComplexCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ComponentComplexCreateView, self).get_context_data(**kwargs)
        if self.request.method == "POST":
            formset = forms.ComponentComplexFormSet(self.request.POST, self.request.FILES,
                                                    queryset=complex_model.ComponentComplex.objects.all())
            if formset.is_valid():
                formset.save()
        else:
            context["formset"] = forms.ComponentComplexFormSet(queryset=complex_model.ComponentComplex.objects.all())
            dig_complex = complex_model.DigitalComplex.get_digital_complex(self)
            context['dig_complex'] = dig_complex
            context['resource_components'] = complex_model.ResourceComponent.objects.filter(digital_complex=dig_complex)
            context['platform_components'] = complex_model.PlatformComponent.objects.filter(digital_complex=dig_complex)
            context['traditional_components'] = complex_model.TraditionalSessionComponent.objects.filter(
                digital_complex=dig_complex)
            # context["form"] = forms.ComponentComplexForm(instance=self.object)
        # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class ComponentComplexUpdateView(generic.UpdateView, GroupRequiredMixin):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    template_name = 'complexes/teacher/componentcomplex_form_update.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        form.instance.digital_complex = complex_model.DigitalComplex.get_digital_complex(self)
        form.save()
        form_valid = super(ComponentComplexUpdateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ComponentComplexUpdateView, self).get_context_data(**kwargs)
        if self.request.method == "POST":
            formset = forms.ComponentComplexFormSet(self.request.POST, self.request.FILES,
                                                    queryset=complex_model.ComponentComplex.objects.all())
            if formset.is_valid():
                formset.save()
        else:
            context["formset"] = forms.ComponentComplexFormSet(queryset=complex_model.ComponentComplex.objects.all())
            context['resource_components'] = complex_model.ResourceComponent.objects.filter(
                digital_complex=self.object.digital_complex)
            context['platform_components'] = complex_model.PlatformComponent.objects.filter(
                digital_complex=self.object.digital_complex)
            context['traditional_components'] = complex_model.TraditionalSessionComponent.objects.filter(
                digital_complex=self.object.digital_complex)
            # context["form"] = forms.ComponentComplexForm(instance=self.object)
        # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class ResourceComponentCreateView(generic.CreateView, GroupRequiredMixin):
    model = complex_model.ResourceComponent
    form_class = forms.ResourceComponentForm
    template_name = 'complexes/teacher/resource_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        form.instance.digital_complex = complex_model.DigitalComplex.get_digital_complex(self)
        form.save()
        form_valid = super(ResourceComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ResourceComponentCreateView, self).get_context_data(**kwargs)
        dig_complex = complex_model.DigitalComplex.get_digital_complex(self)
        context['dig_complex'] = dig_complex
        return context


class ResourceComponentDeleteView(generic.DeleteView, GroupRequiredMixin):
    model = complex_model.ResourceComponent
    form_class = forms.ResourceComponentForm
    template_name = 'complexes/teacher/resource_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        logger.warning(self)
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_create", args=(dig_complex_id,))


class PlatformComponentCreateView(generic.CreateView, GroupRequiredMixin):
    model = complex_model.PlatformComponent
    form_class = forms.PlatformComponentForm
    template_name = 'complexes/teacher/platform_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        form.instance.digital_complex = complex_model.DigitalComplex.get_digital_complex(self)
        form.save()
        form_valid = super(PlatformComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(PlatformComponentCreateView, self).get_context_data(**kwargs)
        dig_complex = complex_model.DigitalComplex.get_digital_complex(self)
        context['dig_complex'] = dig_complex
        return context


class PlatformComponentDeleteView(generic.DeleteView, GroupRequiredMixin):
    model = complex_model.PlatformComponent
    form_class = forms.PlatformComponentForm
    template_name = 'complexes/teacher/platform_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        logger.warning(self)
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_create", args=(dig_complex_id,))


class TraditionalSessionComponentCreateView(generic.CreateView, GroupRequiredMixin):
    model = complex_model.TraditionalSessionComponent
    form_class = forms.TraditionalSessionComponentForm
    template_name = 'complexes/teacher/traditional_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def form_valid(self, form):
        form.instance.digital_complex = complex_model.DigitalComplex.get_digital_complex(self)
        form.save()
        form_valid = super(TraditionalSessionComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(TraditionalSessionComponentCreateView, self).get_context_data(**kwargs)
        dig_complex = complex_model.DigitalComplex.get_digital_complex(self)
        context['dig_complex'] = dig_complex
        return context


class TraditionalSessionComponentDeleteView(generic.DeleteView, GroupRequiredMixin):
    model = complex_model.TraditionalSessionComponent
    form_class = forms.TraditionalSessionComponentForm
    template_name = 'complexes/teacher/traditional_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        logger.warning(self)
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_create", args=(dig_complex_id,))
