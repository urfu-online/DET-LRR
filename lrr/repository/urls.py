from django.urls import path, include
from rest_framework import routers

from lrr.repository import api
from lrr.repository import views

router = routers.DefaultRouter()
router.register(r'digitalresource', api.DigitalResourceViewSet)
router.register(r'direction', api.DirectionViewSet)
router.register(r'language', api.LanguageViewSet)
router.register(r'competencecategory', api.CompetenceCategoryViewSet)
router.register(r'competence', api.CompetenceViewSet)
router.register(r'platform', api.PlatformViewSet)
router.register(r'organisation', api.OrganisationViewSet)
router.register(r'author', api.AuthorViewSet)
router.register(r'source', api.SourceViewSet)
router.register(r'resourcestatus', api.ResourceStatusViewSet)
router.register(r'disciplinetheme', api.DisciplineThemeViewSet)
router.register(r'discipline', api.DisciplineViewSet)
router.register(r'thematicplan', api.ThematicPlanViewSet)
router.register(r'disciplinethemeresource', api.DisciplineThemeResourceViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for DigitalResource
    path('repository/digitalresource/', views.DigitalResourceListView.as_view(), name='repository_digitalresource_list'),
    path('repository/digitalresource/create/', views.DigitalResourceCreateView.as_view(), name='repository_digitalresource_create'),
    path('repository/digitalresource/detail/<uuid:pk>/', views.DigitalResourceDetailView.as_view(), name='repository_digitalresource_detail'),
    path('repository/digitalresource/update/<uuid:pk>/', views.DigitalResourceUpdateView.as_view(), name='repository_digitalresource_update'),
)

urlpatterns += (
    # urls for Direction
    path('repository/direction/', views.DirectionListView.as_view(), name='repository_direction_list'),
    path('repository/direction/create/', views.DirectionCreateView.as_view(), name='repository_direction_create'),
    path('repository/direction/detail/<uuid:pk>/', views.DirectionDetailView.as_view(), name='repository_direction_detail'),
    path('repository/direction/update/<uuid:pk>/', views.DirectionUpdateView.as_view(), name='repository_direction_update'),
)

urlpatterns += (
    # urls for Language
    path('repository/language/', views.LanguageListView.as_view(), name='repository_language_list'),
    path('repository/language/create/', views.LanguageCreateView.as_view(), name='repository_language_create'),
    path('repository/language/detail/<uuid:pk>/', views.LanguageDetailView.as_view(), name='repository_language_detail'),
    path('repository/language/update/<uuid:pk>/', views.LanguageUpdateView.as_view(), name='repository_language_update'),
)

urlpatterns += (
    # urls for CompetenceCategory
    path('repository/competencecategory/', views.CompetenceCategoryListView.as_view(), name='repository_competencecategory_list'),
    path('repository/competencecategory/create/', views.CompetenceCategoryCreateView.as_view(), name='repository_competencecategory_create'),
    path('repository/competencecategory/detail/<uuid:pk>/', views.CompetenceCategoryDetailView.as_view(), name='repository_competencecategory_detail'),
    path('repository/competencecategory/update/<uuid:pk>/', views.CompetenceCategoryUpdateView.as_view(), name='repository_competencecategory_update'),
)

urlpatterns += (
    # urls for Competence
    path('repository/competence/', views.CompetenceListView.as_view(), name='repository_competence_list'),
    path('repository/competence/create/', views.CompetenceCreateView.as_view(), name='repository_competence_create'),
    path('repository/competence/detail/<uuid:pk>/', views.CompetenceDetailView.as_view(), name='repository_competence_detail'),
    path('repository/competence/update/<uuid:pk>/', views.CompetenceUpdateView.as_view(), name='repository_competence_update'),
)

urlpatterns += (
    # urls for Platform
    path('repository/platform/', views.PlatformListView.as_view(), name='repository_platform_list'),
    path('repository/platform/create/', views.PlatformCreateView.as_view(), name='repository_platform_create'),
    path('repository/platform/detail/<uuid:pk>/', views.PlatformDetailView.as_view(), name='repository_platform_detail'),
    path('repository/platform/update/<uuid:pk>/', views.PlatformUpdateView.as_view(), name='repository_platform_update'),
)

urlpatterns += (
    # urls for Organisation
    path('repository/organisation/', views.OrganisationListView.as_view(), name='repository_organisation_list'),
    path('repository/organisation/create/', views.OrganisationCreateView.as_view(), name='repository_organisation_create'),
    path('repository/organisation/detail/<uuid:pk>/', views.OrganisationDetailView.as_view(), name='repository_organisation_detail'),
    path('repository/organisation/update/<uuid:pk>/', views.OrganisationUpdateView.as_view(), name='repository_organisation_update'),
)

urlpatterns += (
    # urls for Author
    path('repository/author/', views.AuthorListView.as_view(), name='repository_author_list'),
    path('repository/author/create/', views.AuthorCreateView.as_view(), name='repository_author_create'),
    path('repository/author/detail/<uuid:pk>/', views.AuthorDetailView.as_view(), name='repository_author_detail'),
    path('repository/author/update/<uuid:pk>/', views.AuthorUpdateView.as_view(), name='repository_author_update'),
)

urlpatterns += (
    # urls for Source
    path('repository/source/', views.SourceListView.as_view(), name='repository_source_list'),
    path('repository/source/create/', views.SourceCreateView.as_view(), name='repository_source_create'),
    path('repository/source/detail/<uuid:pk>/', views.SourceDetailView.as_view(), name='repository_source_detail'),
    path('repository/source/update/<uuid:pk>/', views.SourceUpdateView.as_view(), name='repository_source_update'),
)

urlpatterns += (
    # urls for ResourceStatus
    path('repository/resourcestatus/', views.ResourceStatusListView.as_view(), name='repository_resourcestatus_list'),
    path('repository/resourcestatus/create/', views.ResourceStatusCreateView.as_view(), name='repository_resourcestatus_create'),
    path('repository/resourcestatus/detail/<uuid:pk>/', views.ResourceStatusDetailView.as_view(), name='repository_resourcestatus_detail'),
    path('repository/resourcestatus/update/<uuid:pk>/', views.ResourceStatusUpdateView.as_view(), name='repository_resourcestatus_update'),
)

urlpatterns += (
    # urls for DisciplineTheme
    path('repository/disciplinetheme/', views.DisciplineThemeListView.as_view(), name='repository_disciplinetheme_list'),
    path('repository/disciplinetheme/create/', views.DisciplineThemeCreateView.as_view(), name='repository_disciplinetheme_create'),
    path('repository/disciplinetheme/detail/<uuid:pk>/', views.DisciplineThemeDetailView.as_view(), name='repository_disciplinetheme_detail'),
    path('repository/disciplinetheme/update/<uuid:pk>/', views.DisciplineThemeUpdateView.as_view(), name='repository_disciplinetheme_update'),
)

urlpatterns += (
    # urls for Discipline
    path('repository/discipline/', views.DisciplineListView.as_view(), name='repository_discipline_list'),
    path('repository/discipline/create/', views.DisciplineCreateView.as_view(), name='repository_discipline_create'),
    path('repository/discipline/detail/<uuid:pk>/', views.DisciplineDetailView.as_view(), name='repository_discipline_detail'),
    path('repository/discipline/update/<uuid:pk>/', views.DisciplineUpdateView.as_view(), name='repository_discipline_update'),
)

urlpatterns += (
    # urls for ThematicPlan
    path('repository/thematicplan/', views.ThematicPlanListView.as_view(), name='repository_thematicplan_list'),
    path('repository/thematicplan/create/', views.ThematicPlanCreateView.as_view(), name='repository_thematicplan_create'),
    path('repository/thematicplan/detail/<uuid:pk>/', views.ThematicPlanDetailView.as_view(), name='repository_thematicplan_detail'),
    path('repository/thematicplan/update/<uuid:pk>/', views.ThematicPlanUpdateView.as_view(), name='repository_thematicplan_update'),
)

urlpatterns += (
    # urls for DisciplineThemeResource
    path('repository/disciplinethemeresource/', views.DisciplineThemeResourceListView.as_view(), name='repository_disciplinethemeresource_list'),
    path('repository/disciplinethemeresource/create/', views.DisciplineThemeResourceCreateView.as_view(), name='repository_disciplinethemeresource_create'),
    path('repository/disciplinethemeresource/detail/<uuid:pk>/', views.DisciplineThemeResourceDetailView.as_view(), name='repository_disciplinethemeresource_detail'),
    path('repository/disciplinethemeresource/update/<uuid:pk>/', views.DisciplineThemeResourceUpdateView.as_view(), name='repository_disciplinethemeresource_update'),
)

