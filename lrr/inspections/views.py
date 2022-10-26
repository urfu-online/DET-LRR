import logging
from copy import copy

import django_filters
from django.core.exceptions import EmptyResultSet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import View

from lrr.inspections import forms
from lrr.inspections import models as inspections_models
from lrr.repository.filters import FilteredListView
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person, Expert

# Get an instance of a logger
logger = logging.getLogger(__name__)


def value_to_int(value):
    values = [
        ("не-соотв", "нет", 'не-заполнено'),
        ("низк",),
        ("ниже",),
        ("средн",),
        ("выше",),
        ("высок", "да", "имею", "выявлено", 'заполнено', "имеется")
    ]
    value = value.lower()
    score = -1

    for i, vls in enumerate(values):
        if any([v in value for v in vls]):
            score = i
    return score


def calc_max_value(values_list: list):
    i = -1
    for val in values_list:
        if "отсутств" in val:
            i = i - 1
    return len(values_list) + i


def normalize_values_list(values_list: list):
    normalized_values_list = copy.deepcopy(values_list)
    for val in normalized_values_list:
        if "отсутств" in val:
            normalized_values_list.remove(val)
    return normalized_values_list


class DigitalResourceFilter(django_filters.FilterSet):
    class Meta:
        model = inspections_models.Request
        fields = {
            "digital_resource__title": ['contains'],
            "status": ['exact'],
        }


def find_by_title_with_answer(lst, title):
    logger.info("%s -- %s", title, lst)
    for el in lst:
        if title == el.get("title", None):
            return el if el.get("answer", None) else None
    return None


class RequestCompletionView(View):
    url = reverse_lazy("inspections:inspections_RequestMyClose_list")
    allow_heap = True

    def get(self, request, *args, **kwargs):
        try:
            expertise_opinion = inspections_models.ExpertiseOpinion.objects.select_related("expertise").get(
                pk=kwargs["uuid"])
        except EmptyResultSet:
            expertise_opinion = inspections_models.ExpertiseOpinion.objects.none()

        expertise = expertise_opinion.expertise
        statuses = inspections_models.Status.objects.all()

        if self.allow_heap:
            answers = inspections_models.OpinionIndicator.objects.filter(response__in=expertise.get_responses())
        else:
            typed_responses = expertise.get_typed_responses()

            methodical_response = typed_responses["methodical"]
            methodical_answers = inspections_models.OpinionIndicator.objects.filter(response=methodical_response)

            contental_response = typed_responses["contental"]
            contental_answers = inspections_models.OpinionIndicator.objects.filter(response=contental_response)

            technical_response = typed_responses["technical"]
            technical_answers = inspections_models.OpinionIndicator.objects.filter(response=technical_response)

            answers = methodical_answers | contental_answers | technical_answers

        achievments = []
        indicators = inspections_models.Indicator.objects.all()

        for indicator in indicators:
            if indicator.question.is_group_question():
                answer = "".join(answers.filter(question__parent=indicator.question).values_list('body', flat=True))
            else:
                answer = "".join(answers.filter(question=indicator.question).values_list('body', flat=True))
            achievments.append({
                "title": indicator.title,
                "answer": {
                    "title": answer,
                    "value": indicator.get_value(answer)
                }
            })
        expertise_statuses = []

        # def ss():
        for s in statuses:
            status = {
                "title": s.title,
                "group": s.get_group_display(),
                "answers": []
            }
            requirements = s.requirements.filter(available=True)
            for r in requirements:
                r_title = r.indicator.title
                for achievment in achievments:
                    if achievment["title"] == r_title:
                        success = r.is_ok(achievment["answer"].get("value", None))
                        status["answers"].append({"title": r_title, "success": success})

            expertise_statuses.append(status)

        context = {
            "expertise_statuses": expertise_statuses,
        }
        return render(request, "test.html", context)

    def get_context_data(self, **kwargs):
        context = super(RequestCompletionView, self).get_context_data(**kwargs)
        response = inspections_models.ExpertiseOpinion.objects.get(interview_uuid=context["uuid"])
        context["uuid"] = str(kwargs["uuid"])
        context["response"] = response
        return context


class RequestActiveSecretaryListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.Request
    form_class = forms.RequestCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['secretary', 'admins']
    template_name = 'inspections/secretary/request_active_secretary_list.html'

    def get_queryset(self):
        queryset = self.model.get_request_not_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class RequestCloseSecretaryListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.Request
    form_class = forms.RequestCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['secretary', 'admins']
    template_name = 'inspections/secretary/request_close_secretary_list.html'

    def get_queryset(self):
        queryset = self.model.get_request_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseActiveExpert(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['expert', 'admins']
    template_name = 'inspections/expert/expertise_active_expert_list.html'

    def get_queryset(self):
        user = self.request.user
        # TODO: доделать заявки
        queryset = self.model.get_active_my_checklist()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class RequestCreateView(GroupRequiredMixin, generic.CreateView):
    model = inspections_models.Request
    form_class = forms.RequestCreateForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/request_form_create.html'
    group_required = ["teacher", "admins"]

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
        request = inspections_models.ExpertiseOpinion.objects.create(expertise=form.instance, status="START")
        request.save()
        form_valid = super(RequestCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(RequestCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.RequestCreateForm(self.request.POST, instance=self.object)
            # context["source_formset"] = forms.SourceFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.RequestCreateForm(instance=self.object)
            # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context


class RequestDetailView(GroupRequiredMixin, generic.DetailView):
    model = inspections_models.Request
    form_class = forms.RequestCreateForm
    group_required = ["teacher", "secretary", "admins", ]


class RequestUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.Request
    form_class = forms.RequestUpdateForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/request_form_update.html'
    group_required = ["secretary", "admins", ]

    def dispatch(self, request, *args, **kwargs):
        self.request = get_object_or_404(inspections_models.Request, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.status = "ASSIGNED_STATUS"
        form.save()
        form_valid = super(RequestUpdateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(RequestUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.RequestUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            request = self.object
            context['temporary_status'] = request.get_temporary_status()
            expertise_opinion = request.get_expertise_opinion()
            context['expertise_opinion'] = expertise_opinion
            response = inspections_models.ExpertiseOpinion.objects.select_related('expertise_type').all()
            answer = inspections_models.OpinionIndicator.objects.filter(response=response)
            context["form"] = forms.RequestUpdateForm(instance=self.object)
        # self.object.digital_complex = inspections_models.Request.get_digital_resource(self)
        return context


class CheckListListView(generic.ListView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm


class CheckListMyExpertListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
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


class ExpertiseOpinionMyCloseExpertListView(GroupRequiredMixin, FilteredListView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
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


class ExpertiseOpinionCreateView(GroupRequiredMixin, generic.CreateView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionCreateForm
    template_name = 'inspections/expertise_opinion_form_create.html'
    group_required = ["expert", "admins", "secretary"]

    def dispatch(self, request, *args, **kwargs):
        self.expertise = get_object_or_404(inspections_models.Request, pk=kwargs["expertise_pk"])
        self.digital_resource = get_object_or_404(inspections_models.DigitalResource,
                                                  pk=kwargs["digital_resource_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        form.instance.expertise = self.expertise
        form.instance.status = "IN_PROCESS"
        form.save()
        form_valid = super(ExpertiseOpinionCreateView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super(ExpertiseOpinionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseOpinionCreateForm(self.request.POST, instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.ExpertiseOpinionCreateForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy("inspections:inspections_Request_update", args=(self.object.expertise.pk,))


class ExpertiseOpinionDetailView(generic.DetailView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm


class ExpertiseOpinionDetailCloseView(generic.DetailView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
    template_name = 'inspections/expert/expertiseopinion_close_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExpertiseOpinionDetailCloseView, self).get_context_data(**kwargs)
        logger.warning(self.object.expertise_type)
        try:
            response = inspections_models.ExpertiseOpinion.objects.prefetch_related("user", "expertise_type", "expertise_opinion").filter(
                user=self.request.user, expertise_type=self.object.expertise_type, expertise_opinion=self.object
            ).latest()
            answers = inspections_models.OpinionIndicator.objects.filter(response=response).select_related("question").prefetch_related(
                "question__category").order_by('question__order')
            context['answers'] = answers
            context['categories'] = list(set([a.category for a in answers]))
        except:
            context['answers'] = None
            context['categories'] = None
        return context


class ExpertiseOpinionUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
    pk_url_kwarg = "pk"
    group_required = ["expert", "admins"]
    template_name = 'inspections/expertise_opinion_form_update.html'

    # METHODICAL = 'METHODICAL'
    # CONTENT = 'CONTENT'
    # TECH = 'TECH'

    def form_valid(self, form):
        person = Expert.get_expert(user=self.request.user)
        form.instance.status = "IN_PROCESS"
        form.instance.expert = person
        form.instance.expertise = self.get_object().expertise
        form_valid = super(ExpertiseOpinionUpdateView, self).form_valid(form)
        return form_valid

    def get_success_url(self):
        return reverse_lazy("inspections:inspections_ExpertiseMy_list")

    def get_context_data(self, **kwargs):
        context = super(ExpertiseOpinionUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseOpinionUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            checklists = self.model.get_checklists(expertise=self.object.expertise)
            context['checklists'] = checklists
            logger.warning(checklists)
            context["form"] = forms.ExpertiseOpinionUpdateForm(instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
        return context


class ExpertiseOpinionUpdateExpertView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.ExpertiseOpinion
    form_class = forms.ExpertiseOpinionUpdateForm
    pk_url_kwarg = "pk"
    group_required = ["expert", "admins"]
    template_name = 'inspections/expertise_opinion_form_update_expert.html'

    def dispatch(self, request, *args, **kwargs):
        self.digital_resource = get_object_or_404(inspections_models.DigitalResource,
                                                  pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.digital_resource = self.digital_resource
        # form.instance.expertise = inspections_models.Request.get_request(self)
        # form.instance.status = "START"
        form.save()
        form_valid = super(ExpertiseOpinionUpdateExpertView, self).form_valid(form)
        return form_valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseOpinionUpdateForm(self.request.POST, instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(self.request.POST,
            #                                                                      instance=self.object)
        else:
            context['dig_res'] = self.digital_resource
            context["form"] = forms.ExpertiseOpinionUpdateForm(instance=self.object)
            # context["assignment_formset"] = forms.AssignmentAcademicGroupFormset(instance=self.object)
        return context


class ExpertiseOpinionView(generic.View):
    template_name = 'inspections/expert/checklist_form_update.html'
    success_url = '/ExpertiseMy/'
