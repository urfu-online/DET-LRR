from django.urls import path

from lrr.inspections import views

urlpatterns = (
    path("expertise_completion/<str:uuid>/", views.RequestCompletionView.as_view(), name="expertise_completion"),
    path("RequestActiveSecretary/", views.RequestActiveSecretaryListView.as_view(),
         name="ExpertiseRequestActiveSecretary_list"),
    path("RequestCloseSecretary/", views.RequestCloseSecretaryListView.as_view(),
         name="ExpertiseRequestCloseSecretary_list"),
    path("RequestMy/", views.CheckListMyExpertListView.as_view(),
         name="ExpertiseRequestMy_list"),
    path("RequestActiveExpert/", views.ExpertiseActiveExpert.as_view(),
         name="inspections_ExpertiseActiveExpert_list"),
    path("ExpertiseMyClose/", views.ExpertiseOpinionMyCloseExpertListView.as_view(),
         name="inspections_ExpertiseMyClose_list"),
    path("ExpertiseRequest/create/<uuid:pk>/", views.RequestCreateView.as_view(), name="ExpertiseRequest_create"),
    path("ExpertiseRequest/detail/<uuid:pk>/", views.RequestDetailView.as_view(), name="ExpertiseRequest_detail"),
    path("ExpertiseRequest/update/<uuid:pk>/", views.RequestUpdateView.as_view(), name="ExpertiseRequest_update"),

    path("ExpertiseOpinion/", views.CheckListListView.as_view(), name="ExpertiseOpinion_list"),
    path("ExpertiseOpinion/create/<uuid:expertise_request_pk>",
         views.ExpertiseOpinionCreateView.as_view(),
         name="ExpertiseOpinion_create"),  # Назначение экспертов
    path("ExpertiseOpinion/detail/<uuid:pk>/", views.ExpertiseOpinionDetailView.as_view(),
         name="ExpertiseOpinion_detail"),
    path("ExpertiseOpinion/detail/close/<uuid:pk>/", views.ExpertiseOpinionDetailCloseView.as_view(),
         name="ExpertiseOpinionClose_detail"),
    path("ExpertiseOpinion/expert/update/<uuid:pk>/", views.ExpertiseOpinionUpdateExpertView.as_view(),
         name="ExpertiseOpinion_expert_update"),
    path("ExpertiseOpinion/update/<uuid:pk>/", views.ExpertiseOpinionUpdateView.as_view(),
         name="ExpertiseOpinion_update"),
    path("Answer/<uuid:request_pk>/", views.ExpertiseOpinionView.as_view(),
         name="inspections_answer"),
    # path("survey/<id:id>/<uuid:uuid_pk>/", SurveyDetail.as_view(), name="survey-detail"),
    # path("<int:id>/<uuid:expertise_request_pk>/", views.ExpertiseTypeDetail.as_view(), name="ExpertiseType-detail"),
    # url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    path("<uuid:id>/completed/", views.ExpertiseTypeCompleted.as_view(), name="ExpertiseType-completed"),
    # path("<uuid:id>-<int:step>/", views.ExpertiseTypeDetail.as_view(), name="ExpertiseType-detail-step"),
    path("confirm/<uuid:id>/", views.ConfirmView.as_view(), name="ExpertiseType-confirmation"),

)
