from django.urls import path

from lrr.inspections import views

urlpatterns = (
    path("expertise_completion/<str:uuid>/", views.RequestCompletionView.as_view(), name="expertise_completion"),
    path("RequestActiveSecretary/", views.RequestActiveSecretaryListView.as_view(),
         name="inspections_RequestActiveSecretary_list"),
    path("RequestCloseSecretary/", views.RequestCloseSecretaryListView.as_view(),
         name="inspections_RequestCloseSecretary_list"),
    path("RequestMy/", views.CheckListMyExpertListView.as_view(),
         name="inspections_RequestMy_list"),
    path("RequestActiveExpert/", views.ExpertiseActiveExpert.as_view(),
         name="inspections_ExpertiseActiveExpert_list"),
    path("ExpertiseMyClose/", views.ExpertiseOpinionMyCloseExpertListView.as_view(),
         name="inspections_ExpertiseMyClose_list"),
    path("Request/create/<uuid:pk>/", views.RequestCreateView.as_view(), name="inspections_Request_create"),
    path("Request/detail/<uuid:pk>/", views.RequestDetailView.as_view(), name="inspections_Request_detail"),
    path("Request/update/<uuid:pk>/", views.RequestUpdateView.as_view(), name="inspections_Request_update"),

    path("ExpertiseOpinion/", views.CheckListListView.as_view(), name="inspections_ExpertiseOpinion_list"),
    path("ExpertiseOpinion/create/<uuid:digital_resource_pk>/<uuid:expertise_pk>/",
         views.ExpertiseOpinionCreateView.as_view(),
         name="inspections_ExpertiseOpinion_create"),
    path("ExpertiseOpinion/detail/<uuid:pk>/", views.ExpertiseOpinionDetailView.as_view(),
         name="inspections_ExpertiseOpinion_detail"),
    path("ExpertiseOpinion/detail/close/<uuid:pk>/", views.ExpertiseOpinionDetailCloseView.as_view(),
         name="inspections_ExpertiseOpinionClose_detail"),
    path("ExpertiseOpinion/expert/update/<uuid:pk>/", views.ExpertiseOpinionUpdateExpertView.as_view(),
         name="inspections_ExpertiseOpinion_expert_update"),
    path("ExpertiseOpinion/update/<uuid:pk>/", views.ExpertiseOpinionUpdateView.as_view(),
         name="inspections_ExpertiseOpinion_update"),
    path("Answer/<uuid:request_pk>/", views.ExpertiseOpinionView.as_view(),
         name="inspections_answer"),
    # path("survey/<id:id>/<uuid:uuid_pk>/", SurveyDetail.as_view(), name="survey-detail"),
    path("(<uuid:id>/<uuid:expertise_opinion_pk>/", views.ExpertiseTypeDetail.as_view(), name="expertise-type-detail"),
    # url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    path("<uuid:id>/completed/", views.ExpertiseTypeCompleted.as_view(), name="expertise-type-completed"),
    path("<uuid:id>-<int:step>/", views.ExpertiseTypeDetail.as_view(), name="expertise-type-detail-step"),
    path("confirm/<uuid:id>/", views.ConfirmView.as_view(), name="expertise-type-confirmation"),

)
