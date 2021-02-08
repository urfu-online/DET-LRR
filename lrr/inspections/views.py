import logging

import django_filters
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from lrr.inspections import forms
from lrr.inspections import models as inspections_models
from lrr.repository.filters import FilteredListView
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Person

# Get an instance of a logger
logger = logging.getLogger(__name__)


class DigitalResourceFilter(django_filters.FilterSet):
    class Meta:
        model = inspections_models.Expertise
        fields = {
            "digital_resource__title": ['contains'],
            "status": ['exact'],
        }


class ExpertiseActiveSecretaryListView(FilteredListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/secretary/expertiseactive_secretary_list.html'

    def get_queryset(self):
        queryset = inspections_models.Expertise.get_expertise_not_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseCloseSecretaryListView(FilteredListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/secretary/expertiseclose_secretary_list.html'

    def get_queryset(self):
        queryset = inspections_models.Expertise.get_expertise_assigned_status()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class ExpertiseActiveExpert(FilteredListView, GroupRequiredMixin):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    group_required = ['expert', 'admins']
    template_name = 'inspections/expert/expertise_active_expert_list.html'

    def get_queryset(self):
        queryset = inspections_models.CheckList.get_active_my_checklist(self, inspections_models.CheckList)
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

    def form_valid(self, form):
        form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.instance.date = timezone.now()
        form.instance.status = "SUB_APP"
        form.save()
        form_valid = super(ExpertiseCreateView, self).form_valid(form)
        return form_valid

    # def get_initial(self):
    #     """
    #     Returns the initial data to use for forms on this view.
    #     """
    #     initial = super().get_initial()
    #     logger.warning(inspections_models.Expertise.get_digital_resource(self))
    #     # initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
    #     initial['status'] = "SUB_APP"
    #     return initial

    def get_context_data(self, **kwargs):
        context = super(ExpertiseCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = forms.ExpertiseCreateForm(self.request.POST, instance=self.object)
            # context["source_formset"] = forms.SourceFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            dig_res = inspections_models.Expertise.get_digital_resource(self)
            context['dig_res'] = dig_res
            context["form"] = forms.ExpertiseCreateForm(instance=self.object)
            # context["source_formset"] = forms.SourceFormset(instance=self.object)
        return context

        # context['directions'] = inspections_models.Expertise.check_empty_queryset(self, 'directions')
        # context['subjects'] = inspections_models.Expertise.check_empty_queryset(self, 'subjects')
        # context['digital_complexes'] = inspections_models.Expertise.check_empty_queryset(self, 'digital_complexes')


class ExpertiseDetailView(generic.DetailView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseCreateForm


class ExpertiseUpdateView(generic.UpdateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseUpdateForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/expertise_form_update.html'
    group_required = ["rop", "admins", ]

    def form_valid(self, form):
        # self.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        # person = Person.get_person(user=self.request.user)
        # form.instance.owner = person
        # form.save()
        form_valid = super(ExpertiseUpdateView, self).form_valid(form)
        return form_valid

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        # initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
        # initial['status'] = "SUB_APP"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # dig_res = inspections_models.Expertise.get_digital_resource(self)
        # context['dig_res'] = dig_res
        logger.warning(type(self.object.digital_complexes.all))
        # self.object.digital_complex = inspections_models.Expertise.get_digital_resource(self)
        return context


class CheckListListView(generic.ListView):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm


class CheckListMyExpertListView(FilteredListView, GroupRequiredMixin):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/expert/checklist_my_expert_active_list.html'
    group_required = ['expert', 'admins']

    def get_queryset(self):
        queryset = inspections_models.CheckList.get_my_checklist(self, inspections_models.CheckList)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class CheckListMyCloseExpertListView(FilteredListView, GroupRequiredMixin):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm
    allow_empty = True
    paginate_by = 12
    filterset_class = DigitalResourceFilter
    template_name = 'inspections/expert/checklist_my_expert_close_list.html'
    group_required = ['expert', 'admins']

    def get_queryset(self):
        queryset = inspections_models.CheckList.get_close_my_checklist(self, inspections_models.CheckList)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs


class CheckListCreateView(GroupRequiredMixin, generic.CreateView):
    model = inspections_models.CheckList
    form_class = forms.CheckListCreateForm
    template_name = 'inspections/checklist_form_create.html'
    group_required = [u"expert", u"admins", u"rop"]

    def form_valid(self, form):
        form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        form.instance.expertise = inspections_models.Expertise.get_expertise(self)
        form.instance.status = "START"
        form.save()
        form_valid = super(CheckListCreateView, self).form_valid(form)
        return form_valid

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        logger.warning(inspections_models.Expertise.get_expertise(self))
        initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
        initial['expertise'] = inspections_models.Expertise.get_expertise(self)
        initial['status'] = "START"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dig_res = inspections_models.Expertise.get_digital_resource(self)
        expertise = inspections_models.Expertise.get_expertise(self)
        context['dig_res'] = dig_res
        context['checklists'] = inspections_models.Expertise.get_checklists(expertise)
        return context

    def get_success_url(self):
        return reverse_lazy("inspections:inspections_Expertise_update", args=(self.object.expertise.pk,))


class CheckListDetailView(generic.DetailView):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm


class CheckListUpdateView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm
    pk_url_kwarg = "pk"
    group_required = [u"expert", u"admins"]
    template_name = 'inspections/checklist_form_update.html'

    # def form_valid(self, form):
    #     form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
    #     # form.instance.expertise = inspections_models.Expertise.get_expertise(self)
    #     # form.instance.status = "START"
    #     form.save()
    #     form_valid = super(CheckListUpdateExpertView, self).form_valid(form)
    #     return form_valid
    #
    # def get_initial(self):
    #     """
    #     Returns the initial data to use for forms on this view.
    #     """
    #     initial = super().get_initial()
    #     logger.warning(inspections_models.Expertise.get_expertise(self))
    #     initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
    #     # initial['expertise'] = inspections_models.Expertise.get_expertise(self)
    #     # initial['status'] = "START"
    #     return initial
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     dig_res = inspections_models.Expertise.get_digital_resource(self)
    #     # expertise = inspections_models.Expertise.get_expertise(self)
    #     context['dig_res'] = dig_res
    #     # context['checklists'] = inspections_models.Expertise.get_checklists(expertise)
    #     return context


class CheckListUpdateExpertView(GroupRequiredMixin, generic.UpdateView):
    model = inspections_models.CheckList
    form_class = forms.CheckListUpdateForm
    pk_url_kwarg = "pk"
    group_required = [u"expert", u"admins"]
    template_name = 'inspections/checklist_form_update_expert.html'

    def form_valid(self, form):
        form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        # form.instance.expertise = inspections_models.Expertise.get_expertise(self)
        # form.instance.status = "START"
        form.save()
        form_valid = super(CheckListUpdateExpertView, self).form_valid(form)
        return form_valid

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        logger.warning(inspections_models.Expertise.get_expertise(self))
        initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
        # initial['expertise'] = inspections_models.Expertise.get_expertise(self)
        # initial['status'] = "START"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dig_res = inspections_models.Expertise.get_digital_resource(self)
        # expertise = inspections_models.Expertise.get_expertise(self)
        context['dig_res'] = dig_res
        # context['checklists'] = inspections_models.Expertise.get_checklists(expertise)
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
