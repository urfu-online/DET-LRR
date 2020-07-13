from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import DigitalResource, Direction, Language, CompetenceCategory, Competence, Platform, Organisation, Author, Source, ResourceStatus, DisciplineTheme, Discipline, ThematicPlan, DisciplineThemeResource
from .forms import DigitalResourceForm, DirectionForm, LanguageForm, CompetenceCategoryForm, CompetenceForm, PlatformForm, OrganisationForm, AuthorForm, SourceForm, ResourceStatusForm, DisciplineThemeForm, DisciplineForm, ThematicPlanForm, DisciplineThemeResourceForm


class DigitalResourceListView(ListView):
    model = DigitalResource


class DigitalResourceCreateView(CreateView):
    model = DigitalResource
    form_class = DigitalResourceForm


class DigitalResourceDetailView(DetailView):
    model = DigitalResource


class DigitalResourceUpdateView(UpdateView):
    model = DigitalResource
    form_class = DigitalResourceForm


class DirectionListView(ListView):
    model = Direction


class DirectionCreateView(CreateView):
    model = Direction
    form_class = DirectionForm


class DirectionDetailView(DetailView):
    model = Direction


class DirectionUpdateView(UpdateView):
    model = Direction
    form_class = DirectionForm


class LanguageListView(ListView):
    model = Language


class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm


class LanguageDetailView(DetailView):
    model = Language


class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm


class CompetenceCategoryListView(ListView):
    model = CompetenceCategory


class CompetenceCategoryCreateView(CreateView):
    model = CompetenceCategory
    form_class = CompetenceCategoryForm


class CompetenceCategoryDetailView(DetailView):
    model = CompetenceCategory


class CompetenceCategoryUpdateView(UpdateView):
    model = CompetenceCategory
    form_class = CompetenceCategoryForm


class CompetenceListView(ListView):
    model = Competence


class CompetenceCreateView(CreateView):
    model = Competence
    form_class = CompetenceForm


class CompetenceDetailView(DetailView):
    model = Competence


class CompetenceUpdateView(UpdateView):
    model = Competence
    form_class = CompetenceForm


class PlatformListView(ListView):
    model = Platform


class PlatformCreateView(CreateView):
    model = Platform
    form_class = PlatformForm


class PlatformDetailView(DetailView):
    model = Platform


class PlatformUpdateView(UpdateView):
    model = Platform
    form_class = PlatformForm


class OrganisationListView(ListView):
    model = Organisation


class OrganisationCreateView(CreateView):
    model = Organisation
    form_class = OrganisationForm


class OrganisationDetailView(DetailView):
    model = Organisation


class OrganisationUpdateView(UpdateView):
    model = Organisation
    form_class = OrganisationForm


class AuthorListView(ListView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm


class AuthorDetailView(DetailView):
    model = Author


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm


class SourceListView(ListView):
    model = Source


class SourceCreateView(CreateView):
    model = Source
    form_class = SourceForm


class SourceDetailView(DetailView):
    model = Source


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm


class ResourceStatusListView(ListView):
    model = ResourceStatus


class ResourceStatusCreateView(CreateView):
    model = ResourceStatus
    form_class = ResourceStatusForm


class ResourceStatusDetailView(DetailView):
    model = ResourceStatus


class ResourceStatusUpdateView(UpdateView):
    model = ResourceStatus
    form_class = ResourceStatusForm


class DisciplineThemeListView(ListView):
    model = DisciplineTheme


class DisciplineThemeCreateView(CreateView):
    model = DisciplineTheme
    form_class = DisciplineThemeForm


class DisciplineThemeDetailView(DetailView):
    model = DisciplineTheme


class DisciplineThemeUpdateView(UpdateView):
    model = DisciplineTheme
    form_class = DisciplineThemeForm


class DisciplineListView(ListView):
    model = Discipline


class DisciplineCreateView(CreateView):
    model = Discipline
    form_class = DisciplineForm


class DisciplineDetailView(DetailView):
    model = Discipline


class DisciplineUpdateView(UpdateView):
    model = Discipline
    form_class = DisciplineForm


class ThematicPlanListView(ListView):
    model = ThematicPlan


class ThematicPlanCreateView(CreateView):
    model = ThematicPlan
    form_class = ThematicPlanForm


class ThematicPlanDetailView(DetailView):
    model = ThematicPlan


class ThematicPlanUpdateView(UpdateView):
    model = ThematicPlan
    form_class = ThematicPlanForm


class DisciplineThemeResourceListView(ListView):
    model = DisciplineThemeResource


class DisciplineThemeResourceCreateView(CreateView):
    model = DisciplineThemeResource
    form_class = DisciplineThemeResourceForm


class DisciplineThemeResourceDetailView(DetailView):
    model = DisciplineThemeResource


class DisciplineThemeResourceUpdateView(UpdateView):
    model = DisciplineThemeResource
    form_class = DisciplineThemeResourceForm

