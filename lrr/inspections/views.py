import django_filters
import logging
from django.views import generic

from lrr.inspections import forms
from lrr.inspections import models as inspections_models

from .filters import FilteredListView
from django.urls import reverse


# Get an instance of a logger
logger = logging.getLogger(__name__)


class ExpertiseActiveListView(generic.ListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    template_name = 'inspections/expertiseactive_list.html'

    def get_queryset(self):
        return inspections_models.Expertise.get_expertise_not_assigned_status()


class ExpertiseCloseListView(generic.ListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    template_name = 'inspections/expertiseclose_list.html'

    def get_queryset(self):
        return inspections_models.Expertise.get_expertise_assigned_status()


class ExpertiseCreateView(generic.CreateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        form_valid = super(ExpertiseCreateView, self).form_valid(form)
        form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        return form_valid

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
        dig_res = inspections_models.Expertise.get_digital_resource(self)
        logger.warning(dig_res)
        initial['status'] = "SUB_APP"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dig_res = inspections_models.Expertise.get_digital_resource(self)
        context['dig_res'] = dig_res
        logger.warning(context)
        return context



class ExpertiseDetailView(generic.DetailView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm


class ExpertiseUpdateView(generic.UpdateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    pk_url_kwarg = "pk"


class CheckListListView(generic.ListView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm


class CheckListCreateView(generic.CreateView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm


class CheckListDetailView(generic.DetailView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm


class CheckListUpdateView(generic.UpdateView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm
    pk_url_kwarg = "pk"


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
