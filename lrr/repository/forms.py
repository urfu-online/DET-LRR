from django import forms
from .models import DigitalResource, Direction, Language, CompetenceCategory, Competence, Platform, Organisation, Author, Source, ResourceStatus, DisciplineTheme, Discipline, ThematicPlan, DisciplineThemeResource


class DigitalResourceForm(forms.ModelForm):
    class Meta:
        model = DigitalResource
        fields = ['title', 'type', 'description', 'keywords', 'format', 'content_count', 'usage_stats', 'programs_count', 'directions', 'disciplines', 'language', 'rightholder', 'competences', 'platform', 'authors', 'sources', 'owner', 'status']


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['title']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['code', 'title']


class CompetenceCategoryForm(forms.ModelForm):
    class Meta:
        model = CompetenceCategory
        fields = ['title']


class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['code', 'title', 'category']


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['title', 'logo', 'url', 'description', 'contacts']


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['title', 'description', 'logo', 'site_url', 'contacts']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['title', 'description', 'image']


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['link', 'status', 'type', 'file', 'priority']


class ResourceStatusForm(forms.ModelForm):
    class Meta:
        model = ResourceStatus
        fields = ['status', 'model', 'due_date']


class DisciplineThemeForm(forms.ModelForm):
    class Meta:
        model = DisciplineTheme
        fields = ['index', 'title']


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['title', 'description', 'labor']


class ThematicPlanForm(forms.ModelForm):
    class Meta:
        model = ThematicPlan
        fields = ['discipline', 'themes']


class DisciplineThemeResourceForm(forms.ModelForm):
    class Meta:
        model = DisciplineThemeResource
        fields = ['digital_resource_source', 'discipline_themes']


