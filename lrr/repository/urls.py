from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

urlpatterns = (
    path("DRStatus/", views.DRStatusListView.as_view(), name="repository_DRStatus_list"),
    path("DRStatus/create/", views.DRStatusCreateView.as_view(), name="repository_DRStatus_create"),
    path("DRStatus/detail/<uuid:pk>/", views.DRStatusDetailView.as_view(), name="repository_DRStatus_detail"),
    path("DRStatus/update/<uuid:pk>/", views.DRStatusUpdateView.as_view(), name="repository_DRStatus_update"),
    path("ExpertiseStatus/", views.ExpertiseStatusListView.as_view(), name="repository_ExpertiseStatus_list"),
    path("ExpertiseStatus/create/", views.ExpertiseStatusCreateView.as_view(), name="repository_ExpertiseStatus_create"),
    path("repository/ExpertiseStatus/detail/<uuid:pk>/", views.ExpertiseStatusDetailView.as_view(), name="repository_ExpertiseStatus_detail"),
    path("ExpertiseStatus/update/<uuid:pk>/", views.ExpertiseStatusUpdateView.as_view(), name="repository_ExpertiseStatus_update"),
    path("Subject/", views.SubjectListView.as_view(), name="repository_Subject_list"),
    path("Subject/create/", views.SubjectCreateView.as_view(), name="repository_Subject_create"),
    path("Subject/detail/<int:pk>/", views.SubjectDetailView.as_view(), name="repository_Subject_detail"),
    path("Subject/update/<int:pk>/", views.SubjectUpdateView.as_view(), name="repository_Subject_update"),
    path("Organization/", views.OrganizationListView.as_view(), name="repository_Organization_list"),
    path("Organization/create/", views.OrganizationCreateView.as_view(), name="repository_Organization_create"),
    path("Organization/detail/<int:pk>/", views.OrganizationDetailView.as_view(), name="repository_Organization_detail"),
    path("Organization/update/<int:pk>/", views.OrganizationUpdateView.as_view(), name="repository_Organization_update"),
    path("EduProgram/", views.EduProgramListView.as_view(), name="repository_EduProgram_list"),
    path("EduProgram/create/", views.EduProgramCreateView.as_view(), name="repository_EduProgram_create"),
    path("EduProgram/detail/<int:pk>/", views.EduProgramDetailView.as_view(), name="repository_EduProgram_detail"),
    path("EduProgram/update/<int:pk>/", views.EduProgramUpdateView.as_view(), name="repository_EduProgram_update"),
    path("ProvidingDiscipline/", views.ProvidingDisciplineListView.as_view(), name="repository_ProvidingDiscipline_list"),
    path("ProvidingDiscipline/create/", views.ProvidingDisciplineCreateView.as_view(), name="repository_ProvidingDiscipline_create"),
    path("ProvidingDiscipline/detail/<int:pk>/", views.ProvidingDisciplineDetailView.as_view(), name="repository_Providing_discipline_detail"),
    path("ProvidingDiscipline/update/<int:pk>/", views.ProvidingDisciplineUpdateView.as_view(), name="repository_ProvidingDiscipline_update"),
    path("ResultEdu/", views.ResultEduListView.as_view(), name="repository_ResultEdu_list"),
    path("ResultEdu/create/", views.ResultEduCreateView.as_view(), name="repository_ResultEdu_create"),
    path("ResultEdu/detail/<int:pk>/", views.ResultEduDetailView.as_view(), name="repository_ResultEdu_detail"),
    path("ResultEdu/update/<int:pk>/", views.ResultEduUpdateView.as_view(), name="repository_ResultEdu_update"),
    path("DigitalResource/", views.DigitalResourceListView.as_view(), name="repository_digitalresource_list"),
    path("DigitalResource/create/", views.DigitalResourceCreateView.as_view(), name="repository_DigitalResource_create"),
    path("DigitalResource/detail/<uuid:pk>/", views.DigitalResourceDetailView.as_view(), name="repository_DigitalResource_detail"),
    path("DigitalResource/update/<uuid:pk>/", views.DigitalResourceUpdateView.as_view(), name="repository_DigitalResource_update"),
    path("Competence/", views.CompetenceListView.as_view(), name="repository_Competence_list"),
    path("Competence/create/", views.CompetenceCreateView.as_view(), name="repository_Competence_create"),
    path("Competence/detail/<int:pk>/", views.CompetenceDetailView.as_view(), name="repository_Competence_detail"),
    path("Competence/update/<int:pk>/", views.CompetenceUpdateView.as_view(), name="repository_Competence_update"),
    path("Platform/", views.PlatformListView.as_view(), name="repository_Platform_list"),
    path("Platform/create/", views.PlatformCreateView.as_view(), name="repository_Platform_create"),
    path("Platform/detail/<int:pk>/", views.PlatformDetailView.as_view(), name="repository_Platform_detail"),
    path("Platform/update/<int:pk>/", views.PlatformUpdateView.as_view(), name="repository_Platform_update"),
    path("Language/", views.LanguageListView.as_view(), name="repository_Language_list"),
    path("Language/create/", views.LanguageCreateView.as_view(), name="repository_Language_create"),
    path("Language/detail/<int:pk>/", views.LanguageDetailView.as_view(), name="repository_Language_detail"),
    path("Language/update/<int:pk>/", views.LanguageUpdateView.as_view(), name="repository_Language_update"),
    path("SubjectTag/", views.SubjectTagListView.as_view(), name="repository_SubjectTag_list"),
    path("SubjectTag/create/", views.SubjectTagCreateView.as_view(), name="repository_SubjectTag_create"),
    path("SubjectTag/detail/<int:pk>/", views.SubjectTagDetailView.as_view(), name="repository_SubjectTag_detail"),
    path("SubjectTag/update/<int:pk>/", views.SubjectTagUpdateView.as_view(), name="repository_SubjectTag_update"),
    # path("repository/Student/", views.StudentListView.as_view(), name="repository_Student_list"),
    # path("repository/Student/create/", views.StudentCreateView.as_view(), name="repository_Student_create"),
    # path("repository/Student/detail/<int:pk>/", views.StudentDetailView.as_view(), name="repository_Student_detail"),
    # path("repository/Student/update/<int:pk>/", views.StudentUpdateView.as_view(), name="repository_Student_update"),
    path("ConformityTheme/", views.ConformityThemeListView.as_view(), name="repository_ConformityTheme_list"),
    path("ConformityTheme/create/", views.ConformityThemeCreateView.as_view(), name="repository_ConformityTheme_create"),
    path("ConformityTheme/detail/<int:pk>/", views.ConformityThemeDetailView.as_view(), name="repository_ConformityTheme_detail"),
    path("ConformityTheme/update/<int:pk>/", views.ConformityThemeUpdateView.as_view(), name="repository_ConformityTheme_update"),
    path("EduProgramTag/", views.EduProgramTagListView.as_view(), name="repository_EduProgramTag_list"),
    path("EduProgramTag/create/", views.EduProgramTagCreateView.as_view(), name="repository_EduProgramTag_create"),
    path("EduProgramTag/detail/<int:pk>/", views.EduProgramTagDetailView.as_view(), name="repository_EduProgramTag_detail"),
    path("EduProgramTag/update/<int:pk>/", views.EduProgramTagUpdateView.as_view(), name="repository_EduProgramTag_update"),
    path("SubjectTheme/", views.SubjectThemeListView.as_view(), name="repository_SubjectTheme_list"),
    path("SubjectTheme/create/", views.SubjectThemeCreateView.as_view(), name="repository_SubjectTheme_create"),
    path("SubjectTheme/detail/<int:pk>/", views.SubjectThemeDetailView.as_view(), name="repository_SubjectTheme_detail"),
    path("SubjectTheme/update/<int:pk>/", views.SubjectThemeUpdateView.as_view(), name="repository_SubjectTheme_update"),
    path("ThematicPlan/", views.ThematicPlanListView.as_view(), name="repository_ThematicPlan_list"),
    path("ThematicPlan/create/", views.ThematicPlanCreateView.as_view(), name="repository_ThematicPlan_create"),
    path("ThematicPlan/detail/<int:pk>/", views.ThematicPlanDetailView.as_view(), name="repository_ThematicPlan_detail"),
    path("ThematicPlan/update/<int:pk>/", views.ThematicPlanUpdateView.as_view(), name="repository_ThematicPlan_update"),
    # path("repository/Person/", views.PersonListView.as_view(), name="repository_Person_list"),
    # path("repository/Person/create/", views.PersonCreateView.as_view(), name="repository_Person_create"),
    # path("repository/Person/detail/<int:pk>/", views.PersonDetailView.as_view(), name="repository_Person_detail"),
    # path("repository/Person/update/<int:pk>/", views.PersonUpdateView.as_view(), name="repository_Person_update"),
    path("WorkPlan/", views.WorkPlanView, name="repository_WorkPlan"),
    path("resource/", views.ResourceListView, name="repository_Resource"),
    path("expertises/", views.ExpertiseListView, name="repository_Expertise"),
    path("statistics/", views.statistics, name="repository_statistics"),
)
