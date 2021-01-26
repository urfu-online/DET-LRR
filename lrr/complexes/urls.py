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
)
