# -*- coding: utf-8 -*-
import logging

import django_filters
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

from lrr.complexes import forms
from lrr.complexes import models as complex_model
from lrr.repository.filters import FilteredListView
from lrr.repository.models import Subject, DigitalResource
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person, Student, AcademicGroup

logger = logging.getLogger(__name__)


# def WorkPlanView(request):
#     person = get_object_or_404(Person, user=request.user)
#     academic_group = get_object_or_404(Student, person=Person.objects.get(user=request.user)).academic_group
#     obj_plan = complex_model.AssignmentAcademicGroup.objects.filter(academic_group=academic_group)
#     return render(request, 'pages/work_plan_list.html',
#                   {'academic_group': academic_group, 'obj_plan': obj_plan, 'person': person,  # 'status': status,
#                    'DR': obj_plan[0].digital_resource.first()})


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


class DigitalComplexMyListView(GroupRequiredMixin, FilteredListView):
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


class DigitalComplexCreateView(GroupRequiredMixin, generic.CreateView):
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


class DigitalComplexDetailView(GroupRequiredMixin, generic.DetailView):
    model = complex_model.DigitalComplex
    form_class = forms.DigitalComplexForm
    template_name = 'complexes/teacher/digitalcomplex_detail.html'
    group_required = [u"teacher", u"admins"]

    def get_context_data(self, **kwargs):
        context = super(DigitalComplexDetailView, self).get_context_data(**kwargs)
        component_complex = complex_model.ComponentComplex.objects.instance_of(complex_model.ResourceComponent,
                                                                               complex_model.PlatformComponent,
                                                                               complex_model.LiterarySourcesComponent,
                                                                               complex_model.TraditionalSessionComponent)
        dig_complex = complex_model.DigitalComplex.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        context['component_complex'] = component_complex.filter(digital_complex=dig_complex)
        logger.warning(context['component_complex'])
        context['resource_components'] = complex_model.ResourceComponent.objects.filter(digital_complex=self.object)
        context['platform_components'] = complex_model.PlatformComponent.objects.filter(digital_complex=self.object)
        context['traditional_components'] = complex_model.TraditionalSessionComponent.objects.filter(
            digital_complex=self.object)
        context['literary_components'] = complex_model.LiterarySourcesComponent.objects.filter(
            digital_complex=self.object)
        context['assigment_academic_group'] = complex_model.AssignmentAcademicGroup.objects.filter(
            digital_complex=self.object)
        return context


class DigitalComplexUpdateView(GroupRequiredMixin, generic.UpdateView):
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

    # def __init__(self, *args, **kwargs):
    #     super(DigitalComplexUpdateView, self).__init__(*args, **kwargs)
    #     title = "Электронный учебно-методический комплекс по дисциплине {0}".format(self.fields['title'])
    #     self.fields['title'].initial =


class ComponentComplexCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    template_name = 'complexes/teacher/componentcomplex_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.digital_complex
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
            dig_complex = self.digital_complex
            context['dig_complex'] = self.digital_complex
            context['component_complex'] = complex_model.ComponentComplex.objects.filter(digital_complex=dig_complex)
            # context["form"] = forms.ComponentComplexForm(instance=self.object)
        # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class ComponentComplexUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    template_name = 'complexes/teacher/componentcomplex_form_update.html'
    group_required = [u"teacher", u"admins"]

    # def dispatch(self, request, *args, **kwargs):
    #     self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.object.digital_complex
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
            context['literary_components'] = complex_model.LiterarySourcesComponent.objects.filter(
                digital_complex=self.object.digital_complex)
            context['traditional_components'] = complex_model.TraditionalSessionComponent.objects.filter(
                digital_complex=self.object.digital_complex)
            # context["form"] = forms.ComponentComplexForm(instance=self.object)
        # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class ComponentComplexListView(GroupRequiredMixin, FilteredListView):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/componentcomplex_list.html'
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalComplexFilter

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        component_complex = complex_model.ComponentComplex.objects.instance_of(complex_model.ResourceComponent,
                                                                               complex_model.PlatformComponent,
                                                                               complex_model.LiterarySourcesComponent,
                                                                               complex_model.TraditionalSessionComponent)
        queryset = component_complex.filter(digital_complex=self.digital_complex)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs

    def get_context_data(self, **kwargs):
        context = super(ComponentComplexListView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        context['component_complex'] = complex_model.ComponentComplex.objects.filter(
            digital_complex=self.digital_complex)
        return context


class ResourceComponentCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.ResourceComponent
    form_class = forms.ResourceComponentForm
    template_name = 'complexes/teacher/resource_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.digital_complex
        form.save()
        form_valid = super(ResourceComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ResourceComponentCreateView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        return context

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class ComponentComplexDeleteView(GroupRequiredMixin, generic.DeleteView):
    model = complex_model.ComponentComplex
    form_class = forms.ComponentComplexForm
    template_name = 'complexes/teacher/resource_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class PlatformComponentCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.PlatformComponent
    form_class = forms.PlatformComponentForm
    template_name = 'complexes/teacher/platform_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.digital_complex
        form.save()
        form_valid = super(PlatformComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(PlatformComponentCreateView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        return context

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class PlatformComponentDeleteView(GroupRequiredMixin, generic.DeleteView):
    model = complex_model.PlatformComponent
    form_class = forms.PlatformComponentForm
    template_name = 'complexes/teacher/platform_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class TraditionalSessionComponentCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.TraditionalSessionComponent
    form_class = forms.TraditionalSessionComponentForm
    template_name = 'complexes/teacher/traditional_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.digital_complex
        form.save()
        form_valid = super(TraditionalSessionComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(TraditionalSessionComponentCreateView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        return context

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class TraditionalSessionComponentDeleteView(GroupRequiredMixin, generic.DeleteView):
    model = complex_model.TraditionalSessionComponent
    form_class = forms.TraditionalSessionComponentForm
    template_name = 'complexes/teacher/traditional_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class LiterarySourcesComponentCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.LiterarySourcesComponent
    form_class = forms.LiterarySourcesComponentForm
    template_name = 'complexes/teacher/literary_component/component_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_complex = self.digital_complex
        form.save()
        form_valid = super(LiterarySourcesComponentCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(LiterarySourcesComponentCreateView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        return context

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class LiterarySourcesComponentDeleteView(GroupRequiredMixin, generic.DeleteView):
    model = complex_model.LiterarySourcesComponent
    form_class = forms.LiterarySourcesComponentForm
    template_name = 'complexes/teacher/literary_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_ComponentComplex_list", args=(dig_complex_id,))


class AssignmentAcademicGroupListView(GroupRequiredMixin, FilteredListView):
    model = complex_model.AssignmentAcademicGroup
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/assigment_academic_group/list.html'
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalComplexFilter

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["digital_complex_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        request = self.request
        queryset = complex_model.AssignmentAcademicGroup.get_assignment_group_digital_complex(request)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs

    def get_context_data(self, **kwargs):
        context = super(AssignmentAcademicGroupListView, self).get_context_data(**kwargs)
        context['dig_complex'] = self.digital_complex
        return context


class AssignmentAcademicGroupDetailView(GroupRequiredMixin, generic.DetailView):
    model = complex_model.AssignmentAcademicGroup
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/assigment_academic_group/detail.html'


class AssignmentAcademicGroupDeleteView(GroupRequiredMixin, generic.DeleteView):
    model = complex_model.AssignmentAcademicGroup
    form_class = forms.AssignmentAcademicGroupForm
    template_name = 'complexes/teacher/resource_component/component_form_delete.html'
    group_required = [u"teacher", u"admins"]
    pk_url_kwarg = "pk"

    def get_success_url(self):
        dig_complex_pk = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_AssignmentAcademicGroup_list", args=(dig_complex_pk,))


class AssignmentAcademicGroupCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.AssignmentAcademicGroup
    form_class = forms.AssignmentAcademicGroupForm
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/assigment_academic_group/form_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.digital_complex = get_object_or_404(complex_model.DigitalComplex, pk=kwargs["digital_complex_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_DigitalComplex_detail", args=(dig_complex_id,))

    def form_valid(self, form):
        # context = self.get_context_data()
        form.instance.digital_complex = self.digital_complex
        # assignment_formset = context['assignment_formset']
        self.object = form.save()
        # if assignment_formset.is_valid():
        #     assignment_formset.instance = self.object
        #     assignment_formset.save()
        form_valid = super(AssignmentAcademicGroupCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(AssignmentAcademicGroupCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.AssignmentAcademicGroupForm(self.request.POST)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST)
        else:
            context["form"] = forms.AssignmentAcademicGroupForm()
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset()
            context['dig_complex'] = self.digital_complex
        return context


class AssignmentAcademicGroupUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = complex_model.AssignmentAcademicGroup
    form_class = forms.AssignmentAcademicGroupForm
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/assigment_academic_group/form_update.html'

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_DigitalComplex_detail", args=(dig_complex_id,))

    def form_valid(self, form):
        # context = self.get_context_data()
        form.instance.digital_complex = self.object.digital_complex
        # assignment_formset = context['assignment_formset']
        self.object = form.save()
        # if assignment_formset.is_valid():
        #     assignment_formset.instance = self.object
        #     assignment_formset.save()
        form_valid = super(AssignmentAcademicGroupUpdateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(AssignmentAcademicGroupUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.AssignmentAcademicGroupForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            context["form"] = forms.AssignmentAcademicGroupForm(instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
            context['dig_complex'] = self.object.digital_complex
        return context


class AssignmentAcademicGroupMyFilter(django_filters.FilterSet):
    class Meta:
        model = complex_model.AssignmentAcademicGroup
        fields = {
            'semestr': ['exact'],
        }


# TODO: change complex_model.AssignmentAcademicGroup to repository_models.Subject ?
class AssignmentAcademicGroupMyListView(GroupRequiredMixin, FilteredListView):
    model = complex_model.AssignmentAcademicGroup
    allow_empty = True
    paginate_by = 12
    group_required = [u'student', u'admins']
    filterset_class = AssignmentAcademicGroupMyFilter
    template_name = 'complexes/student/my_subjects_list.html'
    subjects = []

    def get_queryset(self, **kwargs):
        user = self.request.user
        academic_group = Student.get_academic_group_for_user(user)
        queryset = complex_model.AssignmentAcademicGroup.objects.filter(academic_group=academic_group)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(AssignmentAcademicGroupMyListView, self).get_context_data(**kwargs)
        user = self.request.user
        academic_group = Student.get_academic_group_for_user(user)
        direction = AcademicGroup.get_direction_for_number(academic_group)
        self.subjects = complex_model.AssignmentAcademicGroup.objects.filter(academic_group=academic_group).values_list(
            'subject', flat=True).distinct()
        context['subjects'] = Subject.objects.filter(pk__in=self.subjects)
        context['student'] = Student.get_student(user)
        context['academic_group'] = academic_group
        context['direction'] = direction
        return context


class CellMyFilter(django_filters.FilterSet):
    class Meta:
        model = complex_model.Cell
        fields = {
            'theme_name': ['contains'],
        }


class CellListView(GroupRequiredMixin, FilteredListView):
    model = complex_model.Cell
    allow_empty = True
    paginate_by = 12
    group_required = [u'teacher', u'admins']
    filterset_class = CellMyFilter
    template_name = 'complexes/teacher/thematic_plan/list.html'

    def get_queryset(self, **kwargs):
        try:
            queryset = complex_model.Cell.objects.filter(
                digital_complex=self.request.resolver_match.kwargs['digital_complex_pk'])
        except:
            queryset = complex_model.Cell.objects.all()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CellListView, self).get_context_data(**kwargs)
        context['dig_complex'] = complex_model.DigitalComplex.objects.get(
            pk=self.request.resolver_match.kwargs['digital_complex_pk'])
        return context


class CellCreateView(GroupRequiredMixin, generic.CreateView):
    model = complex_model.Cell
    form_class = forms.CellForm
    group_required = [u"teacher", u"admins"]
    template_name = 'complexes/teacher/thematic_plan/form_create.html'

    def get_success_url(self):
        dig_complex_id = self.object.digital_complex.pk
        return reverse_lazy("complexes:complexes_Cell_list", args=(dig_complex_id,))

    def form_valid(self, form):
        # context = self.get_context_data()
        form.instance.digital_complex = self.object.digital_complex
        # assignment_formset = context['assignment_formset']
        self.object = form.save()
        # if assignment_formset.is_valid():
        #     assignment_formset.instance = self.object
        #     assignment_formset.save()
        form_valid = super(CellCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(CellCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.CellForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            context["form"] = forms.CellForm(instance=self.object)
            context['digital_complex_pk'] = self.request.resolver_match.kwargs['digital_complex_pk']
            context['dig_complex'] = complex_model.DigitalComplex.objects.get(
                pk=self.request.resolver_match.kwargs['digital_complex_pk'])
            context['test_complex'] = DigitalResource.objects.filter(title__icontains='Строит')
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
        return context
