"""
Base settings to build other settings files upon.
"""
import os
from pathlib import Path

import environ
from django.conf.global_settings import DATETIME_INPUT_FORMATS

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# lrr/
APPS_DIR = ROOT_DIR / "lrr"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

#### Remove for production use
DEVELOPMENT = True

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env.bool("w", False)
TIME_ZONE = "Asia/Yekaterinburg"
LANGUAGE_CODE = "ru"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = 120

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'adminactions',
    'admin_export_action',
    'data_wizard',
    'data_wizard.sources',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # "django.contrib.admin",
    "django.forms",
    "corsheaders",
    "django_filters",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "admin_interface",
    "colorfield",
    "rest_framework_swagger",
    "polymorphic",
    "dynamic_formsets",
    "six",
    "django_select2",
    'django_better_admin_arrayfield',
    "rest_polymorphic",
    "bootstrapform",
    "pandas",
    "matplotlib",
    "pySankey",
    "seaborn",
    "fontawesome-free",
    "silk",
    'permissions_auditor',
    # "det",
    "smart_selects",
    'import_export',
    'import_export_celery',
    'widget_tweaks',
]

LOCAL_APPS = [
    "lrr.apps.LRRAdminConfig",
    "lrr.users.apps.UsersConfig",
    "lrr.repository.apps.RepositoryConfig",
    "lrr.complexes.apps.ComplexesConfig",
    "lrr.inspections.apps.InspectionsConfig",
    "lrr.survey.apps.DjangoSurveyAndReportConfig",
    "lrr.templatetags.user_tags",
    "lrr.templatetags.survey_extras",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

CORS_ORIGIN_ALLOW_ALL = True
# MIGRATIONS
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {"sites": "lrr.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "silk.middleware.SilkyMiddleware",
    "author.middlewares.AuthorDefaultBackendMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(APPS_DIR, "media")
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "libraries": {
                "user_tags": "lrr.templatetags.user_tags",
                "survey_extras": "lrr.templatetags.survey_extras"
            },
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "lrr.utils.context_processors.settings_context",
            ],
        },
    }
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# FIXTURES
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "SAMEORIGIN"

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = "admin/"
ADMINS = [("""urfu.online""", "mastergowen@gmail.com")]
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 120
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
IMPORT_EXPORT_CELERY_INIT_MODULE = "lrr.celery"
IMPORT_EXPORT_CELERY_MODELS = {
    "repository": {
        'app_label': 'repository',
        'model_name': 'DigitalResource',
    }
}
# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_ADAPTER = "lrr.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "lrr.users.adapters.SocialAccountAdapter"

ACCOUNT_FORMS = {'signup': 'lrr.users.forms.UserSignupForm'}

# ACCOUNT_SIGNUP_FORM_CLASS = 'lrr.users.forms.UserSignupForm'

# django-rest-framework
# -------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    "DATETIME_INPUT_FORMATS": [
        "iso-8601"
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

DATETIME_INPUT_FORMATS += ('%d/%m/%Y %H:%M',)

EXCEL_COMPATIBLE_CSV = True
CHOICES_SEPARATOR = ","
USER_DID_NOT_ANSWER = "NAA"
SURVEY_DEFAULT_PIE_COLOR = "blue!50"
DEFAULT_SURVEY_PUBLISHING_DURATION = 7

SUPPORT_URL = "https://itoo.urfu.ru"

# Cookie names

LANGUAGE_COOKIE_NAME = "lrr_language"
SESSION_COOKIE_NAME = "lrr_sessionid"
CSRF_COOKIE_NAME = "lrr_csrftoken"

SESSION_COOKIE_SECURE = True

DATA_WIZARD = {
    'BACKEND': 'data_wizard.backends.immediate',
    'LOADER': 'data_wizard.loaders.FileLoader',
    'IDMAP': 'data_wizard.idmap.never',  # 'data_wizard.idmap.existing' in 2.0
    'AUTHENTICATION': 'rest_framework.authentication.SessionAuthentication',
    'PERMISSION': 'rest_framework.permissions.IsAdminUser',
}

USE_DJANGO_JQUERY = True
