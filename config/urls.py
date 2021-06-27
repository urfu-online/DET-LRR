from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from lrr.repository.views import DigitalResourceListView

schema_view = get_swagger_view(title='LRR API')

urlpatterns = [

                  path("", DigitalResourceListView.as_view(), name="home"),
                  path(
                      "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
                  ),

                  # User management
                  path("users/", include("lrr.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  path("repository/", include(("lrr.repository.urls", "lrr.repository"), namespace="repository")),
                  path("complexes/", include(("lrr.complexes.urls", "lrr.complexes"), namespace="complexes")),
                  path("inspections/", include(("lrr.inspections.urls", "lrr.inspections"), namespace="inspections")),
                  path("survey/", include(("lrr.survey.urls", "lrr.survey"), namespace="survey")),

                  path("select2/", include("django_select2.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/v0/", include("config.api_router_v0")),

    # Swagger
    path('api_docs/', schema_view),

    # DRF auth token
    path("auth-token/", obtain_auth_token),

]

if 'silk' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk'))
    ]

if "admin_export_action" in settings.INSTALLED_APPS:
    urlpatterns += [
        path('export_action/', include("admin_export_action.urls", namespace="admin_export_action")),
    ]

if "data_wizard" in settings.INSTALLED_APPS:
    urlpatterns += [
        path('datawizard/', include('data_wizard.urls')),
    ]

if settings.DEBUG or settings.DEVELOPMENT:
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

# if 'schema_graph' in settings.INSTALLED_APPS:
#     from schema_graph.views import Schema
#
#     urlpatterns += [
#         path("schema/", Schema.as_view())
#     ]

if "postgres_metrics.apps.PostgresMetrics" in settings.INSTALLED_APPS:
    urlpatterns += [path(f"{settings.ADMIN_URL}postgres-metrics/", include('postgres_metrics.urls')), path(settings.ADMIN_URL, admin.site.urls)]
else:
    urlpatterns += [path(settings.ADMIN_URL, admin.site.urls)]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
