import unittest
from django.urls import reverse
from django.test import Client
from .models import DigitalResource, Direction, Language, CompetenceCategory, Competence, Platform, Organisation, Author, Source, ResourceStatus, DisciplineTheme, Discipline, ThematicPlan, DisciplineThemeResource
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_digitalresource(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["type"] = "type"
    defaults["description"] = "description"
    defaults["keywords"] = "keywords"
    defaults["format"] = "format"
    defaults["content_count"] = "content_count"
    defaults["usage_stats"] = "usage_stats"
    defaults["programs_count"] = "programs_count"
    defaults.update(**kwargs)
    if "directions" not in defaults:
        defaults["directions"] = create_direction()
    if "disciplines" not in defaults:
        defaults["disciplines"] = create_discipline()
    if "language" not in defaults:
        defaults["language"] = create_language()
    if "rightholder" not in defaults:
        defaults["rightholder"] = create_organisation()
    if "competences" not in defaults:
        defaults["competences"] = create_competence()
    if "platform" not in defaults:
        defaults["platform"] = create_platform()
    if "authors" not in defaults:
        defaults["authors"] = create_author()
    if "sources" not in defaults:
        defaults["sources"] = create_source()
    if "owner" not in defaults:
        defaults["owner"] = create_django_contrib_auth_models_user()
    if "status" not in defaults:
        defaults["status"] = create_resourcestatus()
    return DigitalResource.objects.create(**defaults)


def create_direction(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults.update(**kwargs)
    return Direction.objects.create(**defaults)


def create_language(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["title"] = "title"
    defaults.update(**kwargs)
    return Language.objects.create(**defaults)


def create_competencecategory(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults.update(**kwargs)
    return CompetenceCategory.objects.create(**defaults)


def create_competence(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["title"] = "title"
    defaults.update(**kwargs)
    if "category" not in defaults:
        defaults["category"] = create_competencecategory()
    return Competence.objects.create(**defaults)


def create_platform(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["logo"] = "logo"
    defaults["url"] = "url"
    defaults["description"] = "description"
    defaults["contacts"] = "contacts"
    defaults.update(**kwargs)
    return Platform.objects.create(**defaults)


def create_organisation(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["logo"] = "logo"
    defaults["site_url"] = "site_url"
    defaults["contacts"] = "contacts"
    defaults.update(**kwargs)
    return Organisation.objects.create(**defaults)


def create_author(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    return Author.objects.create(**defaults)


def create_source(**kwargs):
    defaults = {}
    defaults["link"] = "link"
    defaults["status"] = "status"
    defaults["type"] = "type"
    defaults["file"] = "file"
    defaults["priority"] = "priority"
    defaults.update(**kwargs)
    return Source.objects.create(**defaults)


def create_resourcestatus(**kwargs):
    defaults = {}
    defaults["status"] = "status"
    defaults["model"] = "model"
    defaults["due_date"] = "due_date"
    defaults.update(**kwargs)
    return ResourceStatus.objects.create(**defaults)


def create_disciplinetheme(**kwargs):
    defaults = {}
    defaults["index"] = "index"
    defaults["title"] = "title"
    defaults.update(**kwargs)
    return DisciplineTheme.objects.create(**defaults)


def create_discipline(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["labor"] = "labor"
    defaults.update(**kwargs)
    return Discipline.objects.create(**defaults)


def create_thematicplan(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "discipline" not in defaults:
        defaults["discipline"] = create_discipline()
    if "themes" not in defaults:
        defaults["themes"] = create_thematicplan()
    return ThematicPlan.objects.create(**defaults)


def create_disciplinethemeresource(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "digital_resource_source" not in defaults:
        defaults["digital_resource_source"] = create_source()
    if "discipline_themes" not in defaults:
        defaults["discipline_themes"] = create_disciplinetheme()
    return DisciplineThemeResource.objects.create(**defaults)


class DigitalResourceViewTest(unittest.TestCase):
    '''
    Tests for DigitalResource
    '''
    def setUp(self):
        self.client = Client()

    def test_list_digitalresource(self):
        url = reverse('repository_digitalresource_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_digitalresource(self):
        url = reverse('repository_digitalresource_create')
        data = {
            "title": "title",
            "type": "type",
            "description": "description",
            "keywords": "keywords",
            "format": "format",
            "content_count": "content_count",
            "usage_stats": "usage_stats",
            "programs_count": "programs_count",
            "directions": create_direction().pk,
            "disciplines": create_discipline().pk,
            "language": create_language().pk,
            "rightholder": create_organisation().pk,
            "competences": create_competence().pk,
            "platform": create_platform().pk,
            "authors": create_author().pk,
            "sources": create_source().pk,
            "owner": create_django_contrib_auth_models_user().pk,
            "status": create_resourcestatus().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_digitalresource(self):
        digitalresource = create_digitalresource()
        url = reverse('repository_digitalresource_detail', args=[digitalresource.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_digitalresource(self):
        digitalresource = create_digitalresource()
        data = {
            "title": "title",
            "type": "type",
            "description": "description",
            "keywords": "keywords",
            "format": "format",
            "content_count": "content_count",
            "usage_stats": "usage_stats",
            "programs_count": "programs_count",
            "directions": create_direction().pk,
            "disciplines": create_discipline().pk,
            "language": create_language().pk,
            "rightholder": create_organisation().pk,
            "competences": create_competence().pk,
            "platform": create_platform().pk,
            "authors": create_author().pk,
            "sources": create_source().pk,
            "owner": create_django_contrib_auth_models_user().pk,
            "status": create_resourcestatus().pk,
        }
        url = reverse('repository_digitalresource_update', args=[digitalresource.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DirectionViewTest(unittest.TestCase):
    '''
    Tests for Direction
    '''
    def setUp(self):
        self.client = Client()

    def test_list_direction(self):
        url = reverse('repository_direction_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_direction(self):
        url = reverse('repository_direction_create')
        data = {
            "title": "title",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_direction(self):
        direction = create_direction()
        url = reverse('repository_direction_detail', args=[direction.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_direction(self):
        direction = create_direction()
        data = {
            "title": "title",
        }
        url = reverse('repository_direction_update', args=[direction.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LanguageViewTest(unittest.TestCase):
    '''
    Tests for Language
    '''
    def setUp(self):
        self.client = Client()

    def test_list_language(self):
        url = reverse('repository_language_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_language(self):
        url = reverse('repository_language_create')
        data = {
            "code": "code",
            "title": "title",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_language(self):
        language = create_language()
        url = reverse('repository_language_detail', args=[language.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_language(self):
        language = create_language()
        data = {
            "code": "code",
            "title": "title",
        }
        url = reverse('repository_language_update', args=[language.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CompetenceCategoryViewTest(unittest.TestCase):
    '''
    Tests for CompetenceCategory
    '''
    def setUp(self):
        self.client = Client()

    def test_list_competencecategory(self):
        url = reverse('repository_competencecategory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_competencecategory(self):
        url = reverse('repository_competencecategory_create')
        data = {
            "title": "title",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_competencecategory(self):
        competencecategory = create_competencecategory()
        url = reverse('repository_competencecategory_detail', args=[competencecategory.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_competencecategory(self):
        competencecategory = create_competencecategory()
        data = {
            "title": "title",
        }
        url = reverse('repository_competencecategory_update', args=[competencecategory.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CompetenceViewTest(unittest.TestCase):
    '''
    Tests for Competence
    '''
    def setUp(self):
        self.client = Client()

    def test_list_competence(self):
        url = reverse('repository_competence_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_competence(self):
        url = reverse('repository_competence_create')
        data = {
            "code": "code",
            "title": "title",
            "category": create_competencecategory().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_competence(self):
        competence = create_competence()
        url = reverse('repository_competence_detail', args=[competence.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_competence(self):
        competence = create_competence()
        data = {
            "code": "code",
            "title": "title",
            "category": create_competencecategory().pk,
        }
        url = reverse('repository_competence_update', args=[competence.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PlatformViewTest(unittest.TestCase):
    '''
    Tests for Platform
    '''
    def setUp(self):
        self.client = Client()

    def test_list_platform(self):
        url = reverse('repository_platform_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_platform(self):
        url = reverse('repository_platform_create')
        data = {
            "title": "title",
            "logo": "logo",
            "url": "url",
            "description": "description",
            "contacts": "contacts",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_platform(self):
        platform = create_platform()
        url = reverse('repository_platform_detail', args=[platform.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_platform(self):
        platform = create_platform()
        data = {
            "title": "title",
            "logo": "logo",
            "url": "url",
            "description": "description",
            "contacts": "contacts",
        }
        url = reverse('repository_platform_update', args=[platform.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrganisationViewTest(unittest.TestCase):
    '''
    Tests for Organisation
    '''
    def setUp(self):
        self.client = Client()

    def test_list_organisation(self):
        url = reverse('repository_organisation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_organisation(self):
        url = reverse('repository_organisation_create')
        data = {
            "title": "title",
            "description": "description",
            "logo": "logo",
            "site_url": "site_url",
            "contacts": "contacts",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_organisation(self):
        organisation = create_organisation()
        url = reverse('repository_organisation_detail', args=[organisation.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_organisation(self):
        organisation = create_organisation()
        data = {
            "title": "title",
            "description": "description",
            "logo": "logo",
            "site_url": "site_url",
            "contacts": "contacts",
        }
        url = reverse('repository_organisation_update', args=[organisation.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AuthorViewTest(unittest.TestCase):
    '''
    Tests for Author
    '''
    def setUp(self):
        self.client = Client()

    def test_list_author(self):
        url = reverse('repository_author_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_author(self):
        url = reverse('repository_author_create')
        data = {
            "title": "title",
            "description": "description",
            "image": "image",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_author(self):
        author = create_author()
        url = reverse('repository_author_detail', args=[author.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_author(self):
        author = create_author()
        data = {
            "title": "title",
            "description": "description",
            "image": "image",
        }
        url = reverse('repository_author_update', args=[author.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SourceViewTest(unittest.TestCase):
    '''
    Tests for Source
    '''
    def setUp(self):
        self.client = Client()

    def test_list_source(self):
        url = reverse('repository_source_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_source(self):
        url = reverse('repository_source_create')
        data = {
            "link": "link",
            "status": "status",
            "type": "type",
            "file": "file",
            "priority": "priority",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_source(self):
        source = create_source()
        url = reverse('repository_source_detail', args=[source.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_source(self):
        source = create_source()
        data = {
            "link": "link",
            "status": "status",
            "type": "type",
            "file": "file",
            "priority": "priority",
        }
        url = reverse('repository_source_update', args=[source.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResourceStatusViewTest(unittest.TestCase):
    '''
    Tests for ResourceStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_resourcestatus(self):
        url = reverse('repository_resourcestatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_resourcestatus(self):
        url = reverse('repository_resourcestatus_create')
        data = {
            "status": "status",
            "model": "model",
            "due_date": "due_date",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_resourcestatus(self):
        resourcestatus = create_resourcestatus()
        url = reverse('repository_resourcestatus_detail', args=[resourcestatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_resourcestatus(self):
        resourcestatus = create_resourcestatus()
        data = {
            "status": "status",
            "model": "model",
            "due_date": "due_date",
        }
        url = reverse('repository_resourcestatus_update', args=[resourcestatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DisciplineThemeViewTest(unittest.TestCase):
    '''
    Tests for DisciplineTheme
    '''
    def setUp(self):
        self.client = Client()

    def test_list_disciplinetheme(self):
        url = reverse('repository_disciplinetheme_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_disciplinetheme(self):
        url = reverse('repository_disciplinetheme_create')
        data = {
            "index": "index",
            "title": "title",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_disciplinetheme(self):
        disciplinetheme = create_disciplinetheme()
        url = reverse('repository_disciplinetheme_detail', args=[disciplinetheme.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_disciplinetheme(self):
        disciplinetheme = create_disciplinetheme()
        data = {
            "index": "index",
            "title": "title",
        }
        url = reverse('repository_disciplinetheme_update', args=[disciplinetheme.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DisciplineViewTest(unittest.TestCase):
    '''
    Tests for Discipline
    '''
    def setUp(self):
        self.client = Client()

    def test_list_discipline(self):
        url = reverse('repository_discipline_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_discipline(self):
        url = reverse('repository_discipline_create')
        data = {
            "title": "title",
            "description": "description",
            "labor": "labor",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_discipline(self):
        discipline = create_discipline()
        url = reverse('repository_discipline_detail', args=[discipline.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_discipline(self):
        discipline = create_discipline()
        data = {
            "title": "title",
            "description": "description",
            "labor": "labor",
        }
        url = reverse('repository_discipline_update', args=[discipline.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ThematicPlanViewTest(unittest.TestCase):
    '''
    Tests for ThematicPlan
    '''
    def setUp(self):
        self.client = Client()

    def test_list_thematicplan(self):
        url = reverse('repository_thematicplan_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_thematicplan(self):
        url = reverse('repository_thematicplan_create')
        data = {
            "discipline": create_discipline().pk,
            "themes": create_thematicplan().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_thematicplan(self):
        thematicplan = create_thematicplan()
        url = reverse('repository_thematicplan_detail', args=[thematicplan.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_thematicplan(self):
        thematicplan = create_thematicplan()
        data = {
            "discipline": create_discipline().pk,
            "themes": create_thematicplan().pk,
        }
        url = reverse('repository_thematicplan_update', args=[thematicplan.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DisciplineThemeResourceViewTest(unittest.TestCase):
    '''
    Tests for DisciplineThemeResource
    '''
    def setUp(self):
        self.client = Client()

    def test_list_disciplinethemeresource(self):
        url = reverse('repository_disciplinethemeresource_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_disciplinethemeresource(self):
        url = reverse('repository_disciplinethemeresource_create')
        data = {
            "digital_resource_source": create_source().pk,
            "discipline_themes": create_disciplinetheme().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_disciplinethemeresource(self):
        disciplinethemeresource = create_disciplinethemeresource()
        url = reverse('repository_disciplinethemeresource_detail', args=[disciplinethemeresource.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_disciplinethemeresource(self):
        disciplinethemeresource = create_disciplinethemeresource()
        data = {
            "digital_resource_source": create_source().pk,
            "discipline_themes": create_disciplinetheme().pk,
        }
        url = reverse('repository_disciplinethemeresource_update', args=[disciplinethemeresource.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


