from django.urls import path
from rest_framework import routers

from lrr.users.api.views import StudentViewSet, PersonViewSet
from lrr.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    # PersonDetailView,
    # PersonUpdateView,
    # StudentDetailView,
    # StudentUpdateView
)

router = routers.DefaultRouter()

# router.register("Person", PersonViewSet)
# router.register("Student", StudentViewSet)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    # path("Student/detail/<int:pk>/", StudentDetailView.as_view(), name="Student_detail"),
    # path("Student/update/<int:pk>/", StudentUpdateView.as_view(), name="Student_update"),
    # path("Person/detail/<int:pk>/", PersonDetailView.as_view(), name="Person_detail"),
    # path("Person/update/<int:pk>/", PersonUpdateView.as_view(), name="Person_update"),
]
