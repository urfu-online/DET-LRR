import django_filters
import logging
from django.views import generic

from lrr.inspections import forms
from lrr.inspections import models as inspections_models
from lrr.users.models import Person
from .filters import FilteredListView
from django.urls import reverse
import django_filters

from lrr.repository.filters import FilteredListView

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
    form_class = forms.ExpertiseForm
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
    form_class = forms.ExpertiseForm
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


class ExpertiseActiveExpert(generic.ListView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    template_name = 'inspections/expert/expertise_active_expert_list.html'

    def get_queryset(self):
        return inspections_models.Expertise.get_expertise_assigned_status()


class ExpertiseCreateView(generic.CreateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/expertise_form_create.html'

    def form_valid(self, form):
        form.instance.digital_resource = inspections_models.Expertise.get_digital_resource(self)
        person = Person.get_person(user=self.request.user)
        form.instance.owner = person
        form.save()
        form_valid = super(ExpertiseCreateView, self).form_valid(form)
        return form_valid

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        initial['digital_resource'] = inspections_models.Expertise.get_digital_resource(self)
        initial['status'] = "SUB_APP"
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dig_res = inspections_models.Expertise.get_digital_resource(self)
        context['dig_res'] = dig_res
        return context


class ExpertiseDetailView(generic.DetailView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm


class ExpertiseUpdateView(generic.UpdateView):
    model = inspections_models.Expertise
    form_class = forms.ExpertiseForm
    pk_url_kwarg = "pk"
    template_name = 'inspections/expertise_form_update.html'

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
    form_class = forms.CheckListForm


class CheckListMyExpertListView(generic.ListView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm
    template_name = 'inspections/expert/checklist_my_expert_active_list.html'


class CheckListMyCloseExpertListView(generic.ListView):
    model = inspections_models.CheckList
    form_class = forms.CheckListForm
    template_name = 'inspections/expert/checklist_my_expert_close_list.html'


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
