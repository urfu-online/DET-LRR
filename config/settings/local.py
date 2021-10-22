import logging

import sentry_sdk
from django.contrib import admin
from sentry_sdk import Hub
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.excepthook import ExcepthookIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="wqIxUuiCZKNIYaAxrc9NN7jLBlObdIgKSrFzjHI4ulxWiAgt52lcD4UAO2LmdbJY",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "lrr.urfu.online", "192.168.0.151", "212.220.200.128"]

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SELECT2_CACHE_BACKEND = "default"

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025

# WhiteNoise
# ------------------------------------------------------------------------------
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar", "schema_graph"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.history.HistoryPanel',
    # 'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    # 'debug_toolbar.panels.settings.SettingsPanel',
    # 'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    # 'djdt_flamegraph.FlamegraphPanel',
]

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2", "192.168.0.151"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["django_extensions"]  # noqa F405
# Celery
# ------------------------------------------------------------------------------
CELERY_TASK_EAGER_PROPAGATES = True
CSRF_COOKIE_SECURE = False
SILKY_ANALYZE_QUERIES = True
SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.DEBUG)
client = Hub.current.client

if client is not None:
    client.close(timeout=2.0)

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,
    event_level=logging.WARNING,
)

sentry_sdk.init(
    'https://40b9200bd9384638b40f68a9637cbc01@sentry.urfu.online/1',
    integrations=[sentry_logging, DjangoIntegration(), CeleryIntegration(), ExcepthookIntegration(always_run=True)],
    max_breadcrumbs=50,
    traces_sample_rate=1.0,
    send_default_pii=True,
    debug=False,
    release="LRR@0.1.0",
    attach_stacktrace=True,
    with_locals=True,
    environment="local",
)
