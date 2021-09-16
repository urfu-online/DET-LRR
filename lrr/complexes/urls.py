from django.urls import path

from lrr.complexes import views

urlpatterns = (
    path("DigitalComplex/list/", views.DigitalComplexListView.as_view(), name="complexes_DigitalComplex_all_list"),
    path("DigitalComplex/", views.DigitalComplexMyListView.as_view(), name="complexes_DigitalComplex_list"),
    path("DigitalComplex/my/", views.DigitalComplexMyListView.as_view(), name="complexes_DigitalComplexMy_list"),
    path("DigitalComplex/create/", views.DigitalComplexCreateView.as_view(), name="complexes_DigitalComplex_create"),
    path("DigitalComplex/detail/<uuid:pk>/", views.DigitalComplexDetailView.as_view(),
         name="complexes_DigitalComplex_detail"),
    path("DigitalComplex/update/<uuid:pk>/", views.DigitalComplexUpdateView.as_view(),
         name="complexes_DigitalComplex_update"),
    path("ComponentComplex/create/<uuid:pk>/", views.ComponentComplexCreateView.as_view(),
         name="complexes_ComponentComplex_create"),
    # path("ComponentComplex/update/<uuid:pk>/", views.ComponentComplexUpdateView.as_view(),
    #      name="complexes_ComponentComplex_update"),
    path("ComponentComplex/list/<uuid:pk>/", views.ComponentComplexListView.as_view(),
         name="complexes_ComponentComplex_list"),
    path("ResourceComponent/create/<uuid:pk>/", views.ResourceComponentCreateView.as_view(),
         name="complexes_ResourceComponent_create"),
    path("ResourceComponent/update/<uuid:pk>/", views.ResourceComponentUpdateView.as_view(),
         name="complexes_ResourceComponent_update"),
    path("ResourceBookmarkComponent/create/<uuid:pk>/", views.ResourceBookmarkComponentCreateView.as_view(),
         name="complexes_ResourceBookmarkComponent_create"),
    # path("ResourceBookmarkComponent/update/<uuid:pk>/", views.ResourceBookmarkComponentUpdateView.as_view(),
    #      name="complexes_ResourceBookmarkComponent_update"),
    path("ComponentComplex/delete/<uuid:pk>/", views.ComponentComplexDeleteView.as_view(),
         name="complexes_ComponentComplex_delete"),
    path("PlatformComponent/create/<uuid:pk>/", views.PlatformComponentCreateView.as_view(),
         name="complexes_PlatformComponent_create"),
    path("PlatformComponent/delete/<uuid:pk>/", views.PlatformComponentDeleteView.as_view(),
         name="complexes_PlatformComponent_delete"),
    path("PlatformComponent/update/<uuid:pk>/", views.PlatformComponentUpdateView.as_view(),
         name="complexes_PlatformComponent_update"),
    path("TraditionalSessionComponent/create/<uuid:pk>/", views.TraditionalSessionComponentCreateView.as_view(),
         name="complexes_TraditionalSessionComponent_create"),
    path("TraditionalSessionComponent/delete/<uuid:pk>/", views.TraditionalSessionComponentDeleteView.as_view(),
         name="complexes_TraditionalSessionComponent_delete"),
    path("TraditionalSessionComponent/update/<uuid:pk>/", views.TraditionalSessionComponentUpdateView.as_view(),
         name="complexes_TraditionalSessionComponent_update"),
    path("LiterarySourcesComponent/create/<uuid:pk>/", views.LiterarySourcesComponentCreateView.as_view(),
         name="complexes_LiterarySourcesComponent_create"),
    path("LiterarySourcesComponent/delete/<uuid:pk>/", views.LiterarySourcesComponentDeleteView.as_view(),
         name="complexes_LiterarySourcesComponent_delete"),
    path("LiterarySourcesComponent/update/<uuid:pk>/", views.LiterarySourcesComponentUpdateView.as_view(),
         name="complexes_LiterarySourcesComponent_update"),
    path("AssignmentAcademicGroup/update/<uuid:pk>/",
         views.AssignmentAcademicGroupUpdateView.as_view(),
         name="complexes_AssignmentAcademicGroup_update"),
    path("AssignmentAcademicGroup/create/<uuid:digital_complex_pk>/", views.AssignmentAcademicGroupCreateView.as_view(),
         name="complexes_AssignmentAcademicGroup_create"),
    path("AssignmentAcademicGroup/list/<uuid:digital_complex_pk>/",
         views.AssignmentAcademicGroupListView.as_view(),
         name="complexes_AssignmentAcademicGroup_list"),
    path("AssignmentAcademicGroup/delete/<uuid:pk>/",
         views.AssignmentAcademicGroupDeleteView.as_view(),
         name="complexes_AssignmentAcademicGroup_delete"),
    path("my_subjects/<str:username>/", view=views.AssignmentAcademicGroupMyListView.as_view(),
         name="complexes_AssignmentAcademicGroupMy_list"),
    path("cell/list/<uuid:digital_complex_pk>/", views.ThematicPlanListView.as_view(),
         name="complexes_ThematicPlan_list"),
    path("cell/create/<uuid:digital_complex_pk>/", views.ThematicPlanCreateView.as_view(),
         name="complexes_ThematicPlan_create"),
)
