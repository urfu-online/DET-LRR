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

    path("ExpertiseRequest/", views.CheckListListView.as_view(), name="inspections_ExpertiseRequest_list"),
    path("ExpertiseRequest/create/<uuid:digital_resource_pk>/<uuid:expertise_pk>/", views.ExpertiseRequestCreateView.as_view(),
         name="inspections_ExpertiseRequest_create"),
    path("ExpertiseRequest/detail/<uuid:pk>/", views.ExpertiseRequestDetailView.as_view(),
         name="inspections_ExpertiseRequest_detail"),
    path("ExpertiseRequest/expert/update/<uuid:pk>/", views.ExpertiseRequestUpdateExpertView.as_view(),
         name="inspections_ExpertiseRequest_expert_update"),
    path("ExpertiseRequest/update/<uuid:pk>/", views.ExpertiseRequestUpdateView.as_view(),
         name="inspections_ExpertiseRequest_update"),
    path("ExpertiseRequest/expertise/<uuid:pk>/", views.ExpertiseRequestUpdateView.as_view(),
         name="inspections_ExpertiseRequest_update"),
    path("Answer/<uuid:request_pk>/", views.AnswerView.as_view(),
         name="inspections_answer"),
    path("Question/", views.QuestionListView.as_view(), name="inspections_Question_list"),
    path("Question/create/", views.QuestionCreateView.as_view(), name="inspections_Question_create"),
    path("Question/detail/<uuid:pk>/", views.QuestionDetailView.as_view(), name="inspections_Question_detail"),
    path("Question/update/<uuid:pk>/", views.QuestionUpdateView.as_view(), name="inspections_Question_update"),
)
