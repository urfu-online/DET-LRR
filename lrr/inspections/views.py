import django_filters
import logging
from copy import copy
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views import generic
from django.views.generic import View

from lrr.inspections import forms
from lrr.inspections import models as inspections_models
from lrr.repository.filters import FilteredListView
from lrr.repository.models import DigitalResource
from lrr.survey.models.answer import Answer, Response, Question
from lrr.survey.models.survey import Survey
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person, Expert
from .indicators import indicators

# Get an instance of a logger
logger = logging.getLogger(__name__)


class DigitalResourceFilter(django_filters.FilterSet):
    class Meta:
        model = inspections_models.Expertise
        fields = {
            "digital_resource__title": ['contains'],
            "status": ['exact'],
        }


class ExpertiseCompletionView(View):
    url = reverse_lazy("inspections:inspections_ExpertiseMyClose_list")
    allow_heap = True

    def get(self, request, *args, **kwargs):
        try:
            expertise_request = inspections_models.ExpertiseRequest.objects.get(pk=kwargs["uuid"])
        except EmptyResultSet:
            expertise_request = inspections_models.ExpertiseRequest.objects.none()

        expertise = expertise_request.expertise

        if self.allow_heap:
            answers = Answer.objects.filter(response__in=expertise.get_responses())
        else:
            typed_responses = expertise.get_typed_responses()
            methodical_response = typed_responses["methodical"]
            methodical_answers = Answer.objects.filter(response=methodical_response)

            contental_response = typed_responses["contental"]
            contental_answers = Answer.objects.filter(response=contental_response)

            technical_response = typed_responses["technical"]
            technical_answers = Answer.objects.filter(response=technical_response)

            answers = methodical_answers | contental_answers | technical_answers

        achievments_wait = list()
        achievments = list()
        for indicator in indicators:
            achievment = copy(indicator)
            ans = answers.filter(question__text=indicator["title"]).first()
            if ans:
                if '0-100' not in indicator["values"]:
                    logger.warning(f"Предполагаем список строк: {ans.body}")
                    achievment["value_interpreted"] = indicator["values"].index(slugify(ans.body, allow_unicode=True))
                    achievment["value"] = slugify(ans.body, allow_unicode=True)
                    achievment["max_value"] = len(indicator["values"]) - 1
                    achievment["SCORE"] = achievment["value_interpreted"] / achievment["max_value"]
                elif '0-100' in indicator["values"]:
                    try:
                        logging.warning(f"Предполагаем 0-100: {ans.body}")
                        achievment["value_interpreted"] = float(ans.body) / 100
                        achievment["value"] = ans.body
                    except:
                        achievment["value_interpreted"] = None
                        achievment["value"] = ans.body
            else:
                logging.warning(f"Отброшено значение {indicator['title']}")

            if "value_interpreted" not in achievment.keys():
                achievments_wait.append(achievment)
            else:
                achievments.append(achievment)
        status = {
            "answers": answers,
            "achievments": achievments,
            "achievments_wait": achievments_wait,
        }

        context = {
            "expertise_request": expertise_request,
            "expertise": expertise,
            "status": status,
        }
        return render(request, "test.html", context)

        # return redirect(self.url)

    def get_context_data(self, **kwargs):
        context = super(ExpertiseCompletionView, self).get_context_data(**kwargs)
        response = Response.objects.get(interview_uuid=context["uuid"])
        context["uuid"] = str(kwargs["uuid"])
        context["response"] = response
        return context


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
        queryset = self.model.get_active_my_checklist()
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
                                                  pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.instance.date = timezone.now()
        form.instance.status = "SUB_APP"
        form.instance.type = "FULL"
        form.save()
        request = inspections_models.ExpertiseRequest.objects.create(expertise=form.instance, status="START")
        request.save()
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
            answer = Answer.objects.filter(response=response)
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
        response = Response.objects.prefetch_related("user", "survey", "expertise_request").filter(
            survey=self.object.survey, expertise_request=self.object
        ).latest()
        answers = Answer.objects.filter(response=response).order_by('question__order')
        context['answers'] = answers
        return context


class ExpertiseRequestUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.ExpertiseRequest
    form_class = forms.ExpertiseRequestUpdateForm
    pk_url_kwarg = "pk"
    group_required = [u"expert", u"admins"]
    template_name = 'inspections/expertise_request_form_update.html'

    # METHODICAL = 'METHODICAL'
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


class ExpertiseRequestView(generic.View):
    template_name = 'inspections/expert/checklist_form_update.html'
    success_url = '/ExpertiseMy/'
