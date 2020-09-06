from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import get_object_or_404

from lrr.users import forms
from lrr.users import models

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = models.User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_person(self):
        return get_object_or_404(models.Person, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # TODO: Если юзер - стафф, то не проверяем его на студента. Лучше сделать группу для стаффа
        context['person'] = get_object_or_404(models.Person, user__username=self.kwargs['username'])
        context['student'] = get_object_or_404(models.Student, person=context['person'])
        # context['person'] = models.Person.objects.filter(user__username__iexact=self.kwargs.get('username'))
        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Person
    fields = [
        "last_name",
        "first_name",
        "middle_name",
        "country",
        "location",
        "city",
        "date_birthday",
        "avatar",
    ]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        # TODO: Заменить get_object_or_404 на get_or_create, создав в модели Person classmethod
        return get_object_or_404(models.Person, user__username=self.request.user.username)


    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Информация успешно обновлена")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


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
