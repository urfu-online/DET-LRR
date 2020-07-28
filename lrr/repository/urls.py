from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("StatusCOR", api.StatusCORViewSet)
router.register("ExpertiseStatus", api.ExpertiseStatusViewSet)
router.register("Subject", api.SubjectViewSet)
router.register("Organization", api.OrganizationViewSet)
router.register("EduProgram", api.EduProgramViewSet)
router.register("ProvidingDiscipline", api.ProvidingDisciplineViewSet)
router.register("ResultEdu", api.ResultEduViewSet)
router.register("DigitalResource", api.DigitalResourceViewSet)
router.register("Competence", api.CompetenceViewSet)
router.register("Platform", api.PlatformViewSet)
router.register("Language", api.LanguageViewSet)
router.register("SubjectTag", api.SubjectTagViewSet)
router.register("Student", api.StudentViewSet)
router.register("ConformityTheme", api.ConformityThemeViewSet)
router.register("EduProgramTag", api.EduProgramTagViewSet)
router.register("SubjectTheme", api.SubjectThemeViewSet)
router.register("ThematicPlan", api.ThematicPlanViewSet)
router.register("Person", api.PersonViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("repository/StatusCOR/", views.StatusCORListView.as_view(), name="repository_StatusCOR_list"),
    path("repository/StatusCOR/create/", views.StatusCORCreateView.as_view(), name="repository_StatusCOR_create"),
    path("repository/StatusCOR/detail/<int:pk>/", views.StatusCORDetailView.as_view(), name="repository_StatusCOR_detail"),
    path("repository/StatusCOR/update/<int:pk>/", views.StatusCORUpdateView.as_view(), name="repository_StatusCOR_update"),
    path("repository/ExpertiseStatus/", views.ExpertiseStatusListView.as_view(), name="repository_ExpertiseStatus_list"),
    path("repository/ExpertiseStatus/create/", views.ExpertiseStatusCreateView.as_view(), name="repository_ExpertiseStatus_create"),
    path("repository/ExpertiseStatus/detail/<int:pk>/", views.ExpertiseStatusDetailView.as_view(), name="repository_ExpertiseStatus_detail"),
    path("repository/ExpertiseStatus/update/<int:pk>/", views.ExpertiseStatusUpdateView.as_view(), name="repository_ExpertiseStatus_update"),
    path("repository/Subject/", views.SubjectListView.as_view(), name="repository_Subject_list"),
    path("repository/Subject/create/", views.SubjectCreateView.as_view(), name="repository_Subject_create"),
    path("repository/Subject/detail/<int:pk>/", views.SubjectDetailView.as_view(), name="repository_Subject_detail"),
    path("repository/Subject/update/<int:pk>/", views.SubjectUpdateView.as_view(), name="repository_Subject_update"),
    path("repository/Organization/", views.OrganizationListView.as_view(), name="repository_Organization_list"),
    path("repository/Organization/create/", views.OrganizationCreateView.as_view(), name="repository_Organization_create"),
    path("repository/Organization/detail/<int:pk>/", views.OrganizationDetailView.as_view(), name="repository_Organization_detail"),
    path("repository/Organization/update/<int:pk>/", views.OrganizationUpdateView.as_view(), name="repository_Organization_update"),
    path("repository/EduProgram/", views.EduProgramListView.as_view(), name="repository_EduProgram_list"),
    path("repository/EduProgram/create/", views.EduProgramCreateView.as_view(), name="repository_EduProgram_create"),
    path("repository/EduProgram/detail/<int:pk>/", views.EduProgramDetailView.as_view(), name="repository_EduProgram_detail"),
    path("repository/EduProgram/update/<int:pk>/", views.EduProgramUpdateView.as_view(), name="repository_EduProgram_update"),
    path("repository/ProvidingDiscipline/", views.ProvidingDisciplineListView.as_view(), name="repository_ProvidingDiscipline_list"),
    path("repository/ProvidingDiscipline/create/", views.ProvidingDisciplineCreateView.as_view(), name="repository_ProvidingDiscipline_create"),
    path("repository/ProvidingDiscipline/detail/<int:pk>/", views.ProvidingDisciplineDetailView.as_view(), name="repository_Providing_discipline_detail"),
    path("repository/ProvidingDiscipline/update/<int:pk>/", views.ProvidingDisciplineUpdateView.as_view(), name="repository_ProvidingDiscipline_update"),
    path("repository/ResultEdu/", views.ResultEduListView.as_view(), name="repository_ResultEdu_list"),
    path("repository/ResultEdu/create/", views.ResultEduCreateView.as_view(), name="repository_ResultEdu_create"),
    path("repository/ResultEdu/detail/<int:pk>/", views.ResultEduDetailView.as_view(), name="repository_ResultEdu_detail"),
    path("repository/ResultEdu/update/<int:pk>/", views.ResultEduUpdateView.as_view(), name="repository_ResultEdu_update"),
    path("repository/DigitalResource/", views.DigitalResourceListView.as_view(), name="repository_DigitalResource_list"),
    path("repository/DigitalResource/create/", views.DigitalResourceCreateView.as_view(), name="repository_DigitalResource_create"),
    path("repository/DigitalResource/detail/<int:pk>/", views.DigitalResourceDetailView.as_view(), name="repository_DigitalResource_detail"),
    path("repository/DigitalResource/update/<int:pk>/", views.DigitalResourceUpdateView.as_view(), name="repository_DigitalResource_update"),
    path("repository/Competence/", views.CompetenceListView.as_view(), name="repository_Competence_list"),
    path("repository/Competence/create/", views.CompetenceCreateView.as_view(), name="repository_Competence_create"),
    path("repository/Competence/detail/<int:pk>/", views.CompetenceDetailView.as_view(), name="repository_Competence_detail"),
    path("repository/Competence/update/<int:pk>/", views.CompetenceUpdateView.as_view(), name="repository_Competence_update"),
    path("repository/Platform/", views.PlatformListView.as_view(), name="repository_Platform_list"),
    path("repository/Platform/create/", views.PlatformCreateView.as_view(), name="repository_Platform_create"),
    path("repository/Platform/detail/<int:pk>/", views.PlatformDetailView.as_view(), name="repository_Platform_detail"),
    path("repository/Platform/update/<int:pk>/", views.PlatformUpdateView.as_view(), name="repository_Platform_update"),
    path("repository/Language/", views.LanguageListView.as_view(), name="repository_Language_list"),
    path("repository/Language/create/", views.LanguageCreateView.as_view(), name="repository_Language_create"),
    path("repository/Language/detail/<int:pk>/", views.LanguageDetailView.as_view(), name="repository_Language_detail"),
    path("repository/Language/update/<int:pk>/", views.LanguageUpdateView.as_view(), name="repository_Language_update"),
    path("repository/SubjectTag/", views.SubjectTagListView.as_view(), name="repository_SubjectTag_list"),
    path("repository/SubjectTag/create/", views.SubjectTagCreateView.as_view(), name="repository_SubjectTag_create"),
    path("repository/SubjectTag/detail/<int:pk>/", views.SubjectTagDetailView.as_view(), name="repository_SubjectTag_detail"),
    path("repository/SubjectTag/update/<int:pk>/", views.SubjectTagUpdateView.as_view(), name="repository_SubjectTag_update"),
    path("repository/Student/", views.StudentListView.as_view(), name="repository_Student_list"),
    path("repository/Student/create/", views.StudentCreateView.as_view(), name="repository_Student_create"),
    path("repository/Student/detail/<int:pk>/", views.StudentDetailView.as_view(), name="repository_Student_detail"),
    path("repository/Student/update/<int:pk>/", views.StudentUpdateView.as_view(), name="repository_Student_update"),
    path("repository/ConformityTheme/", views.ConformityThemeListView.as_view(), name="repository_ConformityTheme_list"),
    path("repository/ConformityTheme/create/", views.ConformityThemeCreateView.as_view(), name="repository_ConformityTheme_create"),
    path("repository/ConformityTheme/detail/<int:pk>/", views.ConformityThemeDetailView.as_view(), name="repository_ConformityTheme_detail"),
    path("repository/ConformityTheme/update/<int:pk>/", views.ConformityThemeUpdateView.as_view(), name="repository_ConformityTheme_update"),
    path("repository/EduProgramTag/", views.EduProgramTagListView.as_view(), name="repository_EduProgramTag_list"),
    path("repository/EduProgramTag/create/", views.EduProgramTagCreateView.as_view(), name="repository_EduProgramTag_create"),
    path("repository/EduProgramTag/detail/<int:pk>/", views.EduProgramTagDetailView.as_view(), name="repository_EduProgramTag_detail"),
    path("repository/EduProgramTag/update/<int:pk>/", views.EduProgramTagUpdateView.as_view(), name="repository_EduProgramTag_update"),
    path("repository/SubjectTheme/", views.SubjectThemeListView.as_view(), name="repository_SubjectTheme_list"),
    path("repository/SubjectTheme/create/", views.SubjectThemeCreateView.as_view(), name="repository_SubjectTheme_create"),
    path("repository/SubjectTheme/detail/<int:pk>/", views.SubjectThemeDetailView.as_view(), name="repository_SubjectTheme_detail"),
    path("repository/SubjectTheme/update/<int:pk>/", views.SubjectThemeUpdateView.as_view(), name="repository_SubjectTheme_update"),
    path("repository/ThematicPlan/", views.ThematicPlanListView.as_view(), name="repository_ThematicPlan_list"),
    path("repository/ThematicPlan/create/", views.ThematicPlanCreateView.as_view(), name="repository_ThematicPlan_create"),
    path("repository/ThematicPlan/detail/<int:pk>/", views.ThematicPlanDetailView.as_view(), name="repository_ThematicPlan_detail"),
    path("repository/ThematicPlan/update/<int:pk>/", views.ThematicPlanUpdateView.as_view(), name="repository_ThematicPlan_update"),
    path("repository/Person/", views.PersonListView.as_view(), name="repository_Person_list"),
    path("repository/Person/create/", views.PersonCreateView.as_view(), name="repository_Person_create"),
    path("repository/Person/detail/<int:pk>/", views.PersonDetailView.as_view(), name="repository_Person_detail"),
    path("repository/Person/update/<int:pk>/", views.PersonUpdateView.as_view(), name="repository_Person_update"),
)
