from django.views import generic

from lrr.users.models import Person, Student
from . import forms
from . import models


class DRStatusListView(generic.ListView):
    model = models.DRStatus
    form_class = forms.DRStatusForm


class DRStatusCreateView(generic.CreateView):
    model = models.DRStatus
    form_class = forms.DRStatusForm


class DRStatusDetailView(generic.DetailView):
    model = models.DRStatus
    form_class = forms.DRStatusForm


class DRStatusUpdateView(generic.UpdateView):
    model = models.DRStatus
    form_class = forms.DRStatusForm
    pk_url_kwarg = "pk"


class ExpertiseStatusListView(generic.ListView):
    model = models.ExpertiseStatus
    form_class = forms.ExpertiseStatusForm


class ExpertiseStatusCreateView(generic.CreateView):
    model = models.ExpertiseStatus
    form_class = forms.ExpertiseStatusForm


class ExpertiseStatusDetailView(generic.DetailView):
    model = models.ExpertiseStatus
    form_class = forms.ExpertiseStatusForm


class ExpertiseStatusUpdateView(generic.UpdateView):
    model = models.ExpertiseStatus
    form_class = forms.ExpertiseStatusForm
    pk_url_kwarg = "pk"


class SubjectListView(generic.ListView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectCreateView(generic.CreateView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectDetailView(generic.DetailView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectUpdateView(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    pk_url_kwarg = "pk"


class OrganizationListView(generic.ListView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationCreateView(generic.CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationDetailView(generic.DetailView):
    model = models.Organization
    form_class = forms.OrganizationForm


class OrganizationUpdateView(generic.UpdateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    pk_url_kwarg = "pk"


class EduProgramListView(generic.ListView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramCreateView(generic.CreateView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramDetailView(generic.DetailView):
    model = models.EduProgram
    form_class = forms.EduProgramForm


class EduProgramUpdateView(generic.UpdateView):
    model = models.EduProgram
    form_class = forms.EduProgramForm
    pk_url_kwarg = "pk"


class ProvidingDisciplineListView(generic.ListView):
    model = models.ProvidingDiscipline
    form_class = forms.ProvidingDisciplineForm


class ProvidingDisciplineCreateView(generic.CreateView):
    model = models.ProvidingDiscipline
    form_class = forms.ProvidingDisciplineForm


class ProvidingDisciplineDetailView(generic.DetailView):
    model = models.ProvidingDiscipline
    form_class = forms.ProvidingDisciplineForm


class ProvidingDisciplineUpdateView(generic.UpdateView):
    model = models.ProvidingDiscipline
    form_class = forms.ProvidingDisciplineForm
    pk_url_kwarg = "pk"


class ResultEduListView(generic.ListView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduCreateView(generic.CreateView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduDetailView(generic.DetailView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm


class ResultEduUpdateView(generic.UpdateView):
    model = models.ResultEdu
    form_class = forms.ResultEduForm
    pk_url_kwarg = "pk"


class DigitalResourceListView(generic.ListView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm


class DigitalResourceCreateView(generic.CreateView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    permission_class = []


class DigitalResourceDetailView(generic.DetailView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm

    def get_context_data(self, **kwargs):
        context = super(DigitalResourceDetailView, self).get_context_data(**kwargs)
        context['status'] = models.DRStatus.objects.filter(digital_resource=self.object)
        return context


class DigitalResourceUpdateView(generic.UpdateView):
    model = models.DigitalResource
    form_class = forms.DigitalResourceForm
    pk_url_kwarg = "pk"


class CompetenceListView(generic.ListView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceCreateView(generic.CreateView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceDetailView(generic.DetailView):
    model = models.Competence
    form_class = forms.CompetenceForm


class CompetenceUpdateView(generic.UpdateView):
    model = models.Competence
    form_class = forms.CompetenceForm
    pk_url_kwarg = "pk"


class PlatformListView(generic.ListView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformCreateView(generic.CreateView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformDetailView(generic.DetailView):
    model = models.Platform
    form_class = forms.PlatformForm


class PlatformUpdateView(generic.UpdateView):
    model = models.Platform
    form_class = forms.PlatformForm
    pk_url_kwarg = "pk"


class LanguageListView(generic.ListView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageCreateView(generic.CreateView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageDetailView(generic.DetailView):
    model = models.Language
    form_class = forms.LanguageForm


class LanguageUpdateView(generic.UpdateView):
    model = models.Language
    form_class = forms.LanguageForm
    pk_url_kwarg = "pk"


class SubjectTagListView(generic.ListView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagCreateView(generic.CreateView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagDetailView(generic.DetailView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm


class SubjectTagUpdateView(generic.UpdateView):
    model = models.SubjectTag
    form_class = forms.SubjectTagForm
    pk_url_kwarg = "pk"


# class StudentListView(generic.ListView):
#     model = models.Student
#     form_class = forms.StudentForm
#
#
# class StudentCreateView(generic.CreateView):
#     model = models.Student
#     form_class = forms.StudentForm
#
#
# class StudentDetailView(generic.DetailView):
#     model = models.Student
#     form_class = forms.StudentForm
#
#
# class StudentUpdateView(generic.UpdateView):
#     model = models.Student
#     form_class = forms.StudentForm
#     pk_url_kwarg = "pk"


class ConformityThemeListView(generic.ListView):
    model = models.ConformityTheme
    form_class = forms.ConformityThemeForm


class ConformityThemeCreateView(generic.CreateView):
    model = models.ConformityTheme
    form_class = forms.ConformityThemeForm


class ConformityThemeDetailView(generic.DetailView):
    model = models.ConformityTheme
    form_class = forms.ConformityThemeForm


class ConformityThemeUpdateView(generic.UpdateView):
    model = models.ConformityTheme
    form_class = forms.ConformityThemeForm
    pk_url_kwarg = "pk"


class EduProgramTagListView(generic.ListView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagCreateView(generic.CreateView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagDetailView(generic.DetailView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm


class EduProgramTagUpdateView(generic.UpdateView):
    model = models.EduProgramTag
    form_class = forms.EduProgramTagForm
    pk_url_kwarg = "pk"


class SubjectThemeListView(generic.ListView):
    model = models.SubjectTheme
    form_class = forms.SubjectThemeForm


class SubjectThemeCreateView(generic.CreateView):
    model = models.SubjectTheme
    form_class = forms.SubjectThemeForm


class SubjectThemeDetailView(generic.DetailView):
    model = models.SubjectTheme
    form_class = forms.SubjectThemeForm


class SubjectThemeUpdateView(generic.UpdateView):
    model = models.SubjectTheme
    form_class = forms.SubjectThemeForm
    pk_url_kwarg = "pk"


class ThematicPlanListView(generic.ListView):
    model = models.ThematicPlan
    form_class = forms.ThematicPlanForm


class ThematicPlanCreateView(generic.CreateView):
    model = models.ThematicPlan
    form_class = forms.ThematicPlanForm


class ThematicPlanDetailView(generic.DetailView):
    model = models.ThematicPlan
    form_class = forms.ThematicPlanForm


class ThematicPlanUpdateView(generic.UpdateView):
    model = models.ThematicPlan
    form_class = forms.ThematicPlanForm
    pk_url_kwarg = "pk"


# class PersonListView(generic.ListView):
#     model = models.Person
#     form_class = forms.PersonForm
#
#
# class PersonCreateView(generic.CreateView):
#     model = models.Person
#     form_class = forms.PersonForm
#
#
# class PersonDetailView(generic.DetailView):
#     model = models.Person
#     form_class = forms.PersonForm
#
#
# class PersonUpdateView(generic.UpdateView):
#     model = models.Person
#     form_class = forms.PersonForm
#     pk_url_kwarg = "pk"
from django.shortcuts import render, get_object_or_404
import logging

logger = logging.getLogger(__name__)


def WorkPlanView(request):
    person = get_object_or_404(Person, user=request.user)
    academic_group = get_object_or_404(Student, person=Person.objects.get(user=request.user)).academic_group
    obj_plan = models.WorkPlanAcademicGroup.objects.filter(academic_group=academic_group)
    status = []
    for i in obj_plan:
        for k in i.digital_resource.all():
            status.append(models.DRStatus.objects.get(digital_resource=k))
    # obj_plan = get_object_or_404(models.WorkPlanAcademicGroup, academic_group=academic_group)
    # digital_resource = obj_plan.digital_resource
    # thematic_paln = obj_plan.thematic_paln
    # academic_group = []
    # digital_resource = []
    # thematic_plans = models.WorkPlanAcademicGroup.objects.all()
    # for plan in thematic_plans:
    #     academic_group.append(plan.academic_group)

    return render(request, 'pages/work_plan_list.html',
                  {'academic_group': academic_group, 'obj_plan': obj_plan, 'person': person, 'status': status})


def ResourceListView(request):
    person = get_object_or_404(Person, user=request.user)
    my_resource = models.DigitalResource.objects.filter(owner=person)
    # status = models.DRStatus.objects.filter(digital_resource=for i in
    return render(request, 'pages/resource_list.html', {'my_resource': my_resource})
