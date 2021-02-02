from django.urls import path

from lrr.inspections import views

urlpatterns = (
    path("ExpertiseActiveSecretary/", views.ExpertiseActiveSecretaryListView.as_view(),
         name="inspections_ExpertiseActiveSecretary_list"),
    path("ExpertiseCloseSecretary/", views.ExpertiseCloseSecretaryListView.as_view(),
         name="inspections_ExpertiseCloseSecretary_list"),
    path("ExpertiseMy/", views.CheckListMyExpertListView.as_view(),
         name="inspections_ExpertiseMy_list"),
    path("ExpertiseActiveExpert/", views.ExpertiseActiveExpert.as_view(),
         name="inspections_ExpertiseActiveExpert_list"),
    path("ExpertiseMyClose/", views.CheckListMyCloseExpertListView.as_view(),
         name="inspections_ExpertiseMyClose_list"),
    path("Expertise/create/<uuid:pk>/", views.ExpertiseCreateView.as_view(), name="inspections_Expertise_create"),
    path("Expertise/detail/<uuid:pk>/", views.ExpertiseDetailView.as_view(), name="inspections_Expertise_detail"),
    path("Expertise/update/<uuid:pk>/", views.ExpertiseUpdateView.as_view(), name="inspections_Expertise_update"),

    path("CheckList/", views.CheckListListView.as_view(), name="inspections_CheckList_list"),
    path("CheckList/create/<uuid:digital_resource_pk>/<uuid:expertise_pk>/", views.CheckListCreateView.as_view(),
         name="inspections_CheckList_create"),
    path("CheckList/detail/<uuid:pk>/", views.CheckListDetailView.as_view(), name="inspections_CheckList_detail"),
    path("CheckList/expert/update/<uuid:pk>/", views.CheckListUpdateExpertView.as_view(),
         name="inspections_CheckList_expert_update"),
    path("CheckList/update/<uuid:pk>/", views.CheckListUpdateView.as_view(),
         name="inspections_CheckList_update"),

    path("Question/", views.QuestionListView.as_view(), name="inspections_Question_list"),
    path("Question/create/", views.QuestionCreateView.as_view(), name="inspections_Question_create"),
    path("Question/detail/<uuid:pk>/", views.QuestionDetailView.as_view(), name="inspections_Question_detail"),
    path("Question/update/<uuid:pk>/", views.QuestionUpdateView.as_view(), name="inspections_Question_update"),
)
