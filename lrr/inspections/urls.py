from django.urls import path
from lrr.inspections import views

urlpatterns = (
    path("ExpertiseActive/", views.ExpertiseActiveListView.as_view(), name="inspections_ExpertiseActive_list"),
    path("ExpertiseClose/", views.ExpertiseCloseListView.as_view(), name="inspections_ExpertiseClose_list"),
    path("Expertise/create/<uuid:pk>/", views.ExpertiseCreateView.as_view(), name="inspections_Expertise_create"),
    path("Expertise/detail/<uuid:pk>/", views.ExpertiseDetailView.as_view(), name="inspections_Expertise_detail"),
    path("Expertise/update/<uuid:pk>/", views.ExpertiseUpdateView.as_view(), name="inspections_Expertise_update"),

    path("CheckList/", views.CheckListListView.as_view(), name="inspections_CheckList_list"),
    path("CheckList/create/", views.CheckListCreateView.as_view(), name="inspections_CheckList_create"),
    path("CheckList/detail/<uuid:pk>/", views.CheckListDetailView.as_view(), name="inspections_CheckList_detail"),
    path("CheckList/update/<uuid:pk>/", views.CheckListUpdateView.as_view(), name="inspections_CheckList_update"),

    path("Question/", views.QuestionListView.as_view(), name="inspections_Question_list"),
    path("Question/create/", views.QuestionCreateView.as_view(), name="inspections_Question_create"),
    path("Question/detail/<uuid:pk>/", views.QuestionDetailView.as_view(), name="inspections_Question_detail"),
    path("Question/update/<uuid:pk>/", views.QuestionUpdateView.as_view(), name="inspections_Question_update"),
)
