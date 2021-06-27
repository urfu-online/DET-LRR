from django.urls import path

from lrr.inspections import views

urlpatterns = (
    path("expertise_completion/<str:uuid>/", views.ExpertiseCompletionView.as_view(), name="expertise_completion"),
    path("ExpertiseActiveSecretary/", views.ExpertiseActiveSecretaryListView.as_view(),
         name="inspections_ExpertiseActiveSecretary_list"),
    path("ExpertiseCloseSecretary/", views.ExpertiseCloseSecretaryListView.as_view(),
         name="inspections_ExpertiseCloseSecretary_list"),
    path("ExpertiseMy/", views.CheckListMyExpertListView.as_view(),
         name="inspections_ExpertiseMy_list"),
    path("ExpertiseActiveExpert/", views.ExpertiseActiveExpert.as_view(),
         name="inspections_ExpertiseActiveExpert_list"),
    path("ExpertiseMyClose/", views.ExpertiseRequestMyCloseExpertListView.as_view(),
         name="inspections_ExpertiseMyClose_list"),
    path("Expertise/create/<uuid:pk>/", views.ExpertiseCreateView.as_view(), name="inspections_Expertise_create"),
    path("Expertise/detail/<uuid:pk>/", views.ExpertiseDetailView.as_view(), name="inspections_Expertise_detail"),
    path("Expertise/update/<uuid:pk>/", views.ExpertiseUpdateView.as_view(), name="inspections_Expertise_update"),

    path("ExpertiseRequest/", views.CheckListListView.as_view(), name="inspections_ExpertiseRequest_list"),
    path("ExpertiseRequest/create/<uuid:digital_resource_pk>/<uuid:expertise_pk>/",
         views.ExpertiseRequestCreateView.as_view(),
         name="inspections_ExpertiseRequest_create"),
    path("ExpertiseRequest/detail/<uuid:pk>/", views.ExpertiseRequestDetailView.as_view(),
         name="inspections_ExpertiseRequest_detail"),
    path("ExpertiseRequest/detail/close/<uuid:pk>/", views.ExpertiseRequestDetailCloseView.as_view(),
         name="inspections_ExpertiseRequestClose_detail"),
    path("ExpertiseRequest/expert/update/<uuid:pk>/", views.ExpertiseRequestUpdateExpertView.as_view(),
         name="inspections_ExpertiseRequest_expert_update"),
    path("ExpertiseRequest/update/<uuid:pk>/", views.ExpertiseRequestUpdateView.as_view(),
         name="inspections_ExpertiseRequest_update"),
    path("Answer/<uuid:request_pk>/", views.ExpertiseRequestView.as_view(),
         name="inspections_answer"),
)
