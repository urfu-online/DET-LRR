import logging

# import the logging library
import django_filters
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView

from lrr.repository.filters import FilteredListView
from lrr.users import forms
from lrr.users import models
from lrr.users.mixins import GroupRequiredMixin

# Get an instance of a logger
logger = logging.getLogger(__name__)

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_person(self, request):
        return request.user.get_person()

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['person'] = models.Person.get_or_create(user=self.request.user)
        # context['student'] = get_object_or_404(models.Student, person=context['person'])
        return context


user_detail_view = UserDetailView.as_view()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Person
    form_class = forms.PersonForm

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=""):
        return models.Person.get_or_create(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.add_message(
            self.request, messages.INFO, _("Информация успешно обновлена")
        )
        return super().form_valid(form)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


# class StudentListView(ListView):
#     model = models.Student
#     form_class = forms.StudentForm
#
#
# class StudentCreateView(CreateView):
#     model = models.Student
#     form_class = forms.StudentForm


# class StudentDetailView(DetailView):
#     model = models.Student
#     form_class = forms.StudentForm
#
#
# class StudentUpdateView(UpdateView):
#     model = models.Student
#     form_class = forms.StudentForm
#     pk_url_kwarg = "pk"


# class PersonListView(ListView):
#     model = models.Person
#     form_class = forms.PersonForm
#
#
# class PersonCreateView(CreateView):
#     model = models.Person
#     form_class = forms.PersonForm


# class PersonDetailView(DetailView):
#     model = models.Person
#     form_class = forms.PersonForm
#
#
# class PersonUpdateView(UpdateView):
#     model = models.Person
#     form_class = forms.PersonForm
#     pk_url_kwarg = "pk"

class ExpertFilter(django_filters.FilterSet):
    class Meta:
        model = models.Expert
        fields = {
            'person__first_name': ['icontains'],
            'person__last_name': ['icontains'],
            'person__middle_name': ['icontains'],
            'types': ['exact'],
            'subdivision': ['icontains'],
        }


class ExpertListView(FilteredListView):
    model = models.Expert
    form_class = forms.ExpertForm
    allow_empty = True
    paginate_by = 12
    filterset_class = ExpertFilter


expert_list_view = ExpertListView.as_view()


class ExpertDetailView(DetailView):
    model = models.Expert
    form_class = forms.ExpertForm
    template_name = 'users/expert_detail.html'

    def get_slug_field(self):
        return 'person__user__username'


expert_detail_view = ExpertDetailView.as_view()


class ExpertCreateView(GroupRequiredMixin, CreateView):
    model = models.Expert
    form_class = forms.ExpertForm
    group_required = [u"admins", u"secretary"]

    def get_success_url(self):
        return reverse_lazy("users:expert_list")

    def form_valid(self, form):
        expert = Group.objects.get(name='expert')
        person = form.cleaned_data['person']
        expert.user_set.add(person.user)
        form.save()
        form_valid = super(ExpertCreateView, self).form_valid(form)
        return form_valid


expert_create_view = ExpertCreateView.as_view()


class ExpertUpdateView(GroupRequiredMixin, UpdateView):
    model = models.Expert
    form_class = forms.ExpertForm
    group_required = [u"admins", u"secretary"]

    def get_success_url(self):
        return reverse_lazy("users:expert_list")

    def get_slug_field(self):
        return 'person__user__username'

    # def form_valid(self, form):
    #     form.instance = self.object
    #     form_valid = super(ExpertUpdateView, self).form_valid(form)
    #     return form_valid
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ExpertUpdateView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context["form"] = forms.ExpertForm(self.request.POST, instance=self.object)
    #     else:
    #         context["form"] = forms.ExpertForm(instance=self.object)
    #     return context


expert_update_view = ExpertUpdateView.as_view()
