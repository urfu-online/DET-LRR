import logging

import django_filters
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.shortcuts import redirect, render, reverse, get_object_or_404

from lrr.inspections import forms
from lrr.inspections import models as inspections_models
from lrr.repository.filters import FilteredListView
from lrr.repository.models import DigitalResource
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person, Expert
from lrr.survey.models.answer import Answer, Response, Question

# Get an instance of a logger
logger = logging.getLogger(__name__)


class DigitalResourceFilter(django_filters.FilterSet):
    class Meta:
        model = inspections_models.Expertise
        fields = {
            "digital_resource__title": ['contains'],
            "status": ['exact'],
        }


class ExpertiseActiveSecretaryListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['secretary', 'admins']
    template_name = 'inspections/secretary/expertiseactive_secretary_list.html'

    def get_queryset(self):
        queryset = self.model.get_expertise_not_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseCloseSecretaryListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['secretary', 'admins']
    template_name = 'inspections/secretary/expertiseclose_secretary_list.html'

    def get_queryset(self):
        queryset = self.model.get_expertise_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseActiveExpert(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['expert', 'admins']
    template_name = 'inspections/expert/expertise_active_expert_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = self.model.get_active_my_checklist(user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseCreateView(GroupRequiredMixin, generic.CreateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/expertise_form_create.html'
    group_required = [u"teacher", u"admins"]

    def dispatch(self, request, *args, **kwargs):
        self.digital_resource = get_object_or_404(inspections_models.DigitalResource,
                                                  pk=kwargs["digital_resource_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.instance.date = timezone.now()
        form.instance.status = "SUB_APP"
        form.instance.type = "FULL"
        form.save()
        form_valid = super(ExpertiseCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ExpertiseCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseCreateForm(self.request.POST, instance=self.object)
            # context["source_formset"] = forms.SourceFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.ExpertiseCreateForm(instance=self.object)
            # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class ExpertiseDetailView(GroupRequiredMixin, generic.DetailView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    group_required = ["teacher", "secretary", "admins", ]


class ExpertiseUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseUpdateForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/expertise_form_update.html'
    group_required = ["secretary", "admins", ]

    def form_valid(self, form):
        form.instance.status = "ASSIGNED_STATUS"
        form.save()
        form_valid = super(ExpertiseUpdateView, self).form_valid(form)
        return form_valid

    # TODO: формат date + digital_resource + избавиться от Expertise.get_checklists
    def get_context_data(self, **kwargs):
        context = super(ExpertiseUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            expertise = self.object
            expertise_request = expertise.get_expertise_request()
            context['expertise_request'] = expertise_request
            response = Response.objects.select_related('survey').all()
            logger.warning(response)
            answer = Answer.objects.filter(response=response)
            logger.warning(answer)
            context["form"] = forms.ExpertiseUpdateForm(instance=self.object)
        # self.object.digital_complex = inspections_models.Expertise.get_digital_resource(self)
        return context


class CheckListListView(generic.ListView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm


class CheckListMyExpertListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/expert/checklist_my_expert_active_list.html'
    group_required = ['expert', 'admins']

    def get_queryset(self):
        user = self.request.user
        queryset = self.model.get_my_checklist(user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseRequestMyCloseExpertListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/expert/checklist_my_expert_close_list.html'
    group_required = ['expert', 'admins']

    def get_queryset(self):
        user = self.request.user
        queryset = self.model.get_close_my_checklist(user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseRequestCreateView(GroupRequiredMixin, generic.CreateView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestCreateForm
    template_name = 'inspections/expertise_request_form_create.html'
    group_required = [u"expert", u"admins", u"secretary"]

    def dispatch(self, request, *args, **kwargs):
        self.expertise = get_object_or_404(inspections_models.Expertise, pk=kwargs["expertise_pk"])
        self.digital_resource = get_object_or_404(inspections_models.DigitalResource,
                                                  pk=kwargs["digital_resource_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        form.instance.expertise = self.expertise
        form.instance.status = "START"
        form.save()
        form_valid = super(ExpertiseRequestCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ExpertiseRequestCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseRequestCreateForm(self.request.POST, instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.ExpertiseRequestCreateForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy("inspections:inspections_Expertise_update", args=(self.object.expertise.pk,))


class ExpertiseRequestDetailView(generic.DetailView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm


class ExpertiseRequestDetailCloseView(generic.DetailView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    template_name = 'inspections/expert/expertiserequest_close_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExpertiseRequestDetailCloseView, self).get_context_data(**kwargs)
        logger.warning(self.object.survey)
        response = Response.objects.prefetch_related("user", "survey", "expertise_request").get(
            survey=self.object.survey, expertise_request=self.object
        )
        answers = Answer.objects.filter(response=response)
        context['answers'] = answers
        return context


class ExpertiseRequestUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    pk_url_kwarg = "pk"
    group_required = [u"expert", u"admins"]
    template_name = 'inspections/expertise_request_form_update.html'

    # METHODIGAL = 'METHODIGAL'
    # CONTENT = 'CONTENT'
    # TECH = 'TECH'

    def form_valid(self, form):
        person = Expert.get_expert(user=self.request.user)
        form.instance.status = "IN_PROCESS"
        form.instance.expert = person
        form.instance.expertise = self.get_object().expertise
        form_valid = super(ExpertiseRequestUpdateView, self).form_valid(form)
        return form_valid

    def get_success_url(self):
        return reverse_lazy("inspections:inspections_ExpertiseMy_list")

    def get_context_data(self, **kwargs):
        context = super(ExpertiseRequestUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseRequestUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            checklists = self.model.get_checklists(expertise=self.object.expertise)
            context['checklists'] = checklists
            context["form"] = forms.ExpertiseRequestUpdateForm(instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
        return context


class ExpertiseRequestUpdateExpertView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    pk_url_kwarg = "pk"
    group_required = [u"expert", u"admins"]
    template_name = 'inspections/expertise_request_form_update_expert.html'

    def dispatch(self, request, *args, **kwargs):
        self.digital_resource = get_object_or_404(inspections_models.DigitalResource,
                                                  pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        # form.instance.expertise = inspections_models.Expertise.get_expertise(self)
        # form.instance.status = "START"
        form.save()
        form_valid = super(ExpertiseRequestUpdateExpertView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseRequestUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.ExpertiseRequestUpdateForm(instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
        return context


class QuestionListView(generic.ListView):
    model = inspections_models.Question
    form_class = forms.QuestionForm


class QuestionCreateView(generic.CreateView):
    model = inspections_models.Question
    form_class = forms.QuestionForm


class QuestionDetailView(generic.DetailView):
    model = inspections_models.Question
    form_class = forms.QuestionForm


class QuestionUpdateView(generic.UpdateView):
    model = inspections_models.Question
    form_class = forms.QuestionForm
    pk_url_kwarg = "pk"


class ExpertiseRequestView(generic.View):
    template_name = 'inspections/expert/checklist_form_update.html'
    success_url = '/ExpertiseMy/'
