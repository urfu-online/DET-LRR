from django.urls import path

from lrr.complexes import views

urlpatterns = (
    path("WorkPlan/", views.WorkPlanView, name="complexes_WorkPlan"),
)
