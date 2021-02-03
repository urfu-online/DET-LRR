from django.urls import path

from lrr.complexes import views

urlpatterns = (
    path("WorkPlan/", views.WorkPlanView, name="complexes_WorkPlan"),
    path("DigitalComplex/", views.DigitalComplexMyListView.as_view(), name="complexes_DigitalComplex_list"),
    path("DigitalComplex/my/", views.DigitalComplexMyListView.as_view(), name="complexes_DigitalComplexMy_list"),
    path("DigitalComplex/create/", views.DigitalComplexCreateView.as_view(), name="complexes_DigitalComplex_create"),
    path("DigitalComplexDetail/<uuid:pk>/", views.DigitalComplexDetailView.as_view(),
         name="complexes_DigitalComplex_detail"),
    path("DigitalComplex/update/<uuid:pk>/", views.DigitalComplexUpdateView.as_view(),
         name="complexes_DigitalComplex_update"),
    path("ComponentComplex/create/<uuid:pk>/", views.ComponentComplexCreateView.as_view(),
         name="complexes_ComponentComplex_create"),
    path("ComponentComplex/update/<uuid:pk>/", views.ComponentComplexUpdateView.as_view(),
         name="complexes_ComponentComplex_update"),
    path("ResourceComponent/create/<uuid:pk>/", views.ResourceComponentCreateView.as_view(),
         name="complexes_ResourceComponent_create"),
    path("ResourceComponent/delete/<uuid:pk>/", views.ResourceComponentDeleteView.as_view(),
         name="complexes_ResourceComponent_delete"),
    path("PlatformComponent/create/<uuid:pk>/", views.PlatformComponentCreateView.as_view(),
         name="complexes_PlatformComponent_create"),
    path("PlatformComponent/delete/<uuid:pk>/", views.PlatformComponentDeleteView.as_view(),
         name="complexes_PlatformComponent_delete"),
    path("TraditionalSessionComponent/create/<uuid:pk>/", views.TraditionalSessionComponentCreateView.as_view(),
         name="complexes_TraditionalSessionComponent_create"),
    path("TraditionalSessionComponent/delete/<uuid:pk>/", views.TraditionalSessionComponentDeleteView.as_view(),
         name="complexes_TraditionalSessionComponent_delete"),
)
