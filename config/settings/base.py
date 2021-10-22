"""
Base settings to build other settings files upon.
"""
import os
import sys
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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

sys.modules['fontawesome_free'] = __import__('fontawesome-free')

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'adminactions',
    'admin_export_action',
    'data_wizard',
    'data_wizard.sources',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',
    # 'django.contrib.admin',
    'django.forms',
    'corsheaders',
    'django_filters',
]
THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_auth_adfs',
    'django_celery_beat',
    'rest_framework',
    'rest_framework.authtoken',
    'admin_interface',
    'colorfield',
    'rest_framework_swagger',
    'polymorphic',
    'dynamic_formsets',
    'six',
    'django_select2',
    'easy_select2',
    'django_better_admin_arrayfield',
    'adminsortable2',
    'lineup.apps.LineupConfig',
    'versatileimagefield',
    'rest_polymorphic',
    'pandas',
    'matplotlib',
    'pySankey',
    'seaborn',
    'taggit',
    'fontawesome_free',
    'django_bootstrap_icons',
    'permissions_auditor',
    # 'det',
    'smart_selects',
    'import_export',
    'import_export_celery',
    'widget_tweaks',
    'django_json_widget',
    'sortedm2m',
    'analytical',
    'postgres_metrics.apps.PostgresMetrics'
]

LOCAL_APPS = [
    'lrr.apps.LRRAdminConfig',
    'lrr.users.apps.UsersConfig',
    'lrr.repository.apps.RepositoryConfig',
    'lrr.complexes.apps.ComplexesConfig',
    'lrr.inspections.apps.InspectionsConfig',
    'lrr.survey.apps.DjangoSurveyAndReportConfig',
    'lrr.templatetags.user_tags',
    'lrr.templatetags.survey_extras',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

CORS_ORIGIN_ALLOW_ALL = True
# MIGRATIONS
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    "sites": "lrr.contrib.sites.migrations",
    "import_export_celery": "lrr.contrib.sites.import_export_celery.migrations"
}

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
IMPORT_EXPORT_CELERY_INIT_MODULE = "config.celery_app"
IMPORT_EXPORT_CELERY_MODELS = {
    "repository": {
        'app_label': 'lrr.repository',
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
DEFAULT_FORMFIELD_CLASSES = 'mt-4 shadow-sm bg-white border border-secondary'
# ACCOUNT_FORMS = {'signup': 'lrr.users.forms.UserSignupForm'}
ACCOUNT_FORMS = {
    'login': 'lrr.forms.DETLoginForm',
    'reset_password': 'lrr.forms.DETResetPasswordForm',
    'add_email': 'lrr.forms.DETAddEmailForm',
    'change_password': 'lrr.forms.DETChangePasswordForm',
}

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

DEFAULT_SOURCE_NAME = "---"
DEFAULT_SOURCE_TYPE = "---"

MATOMO_DOMAIN_PATH = 'tracker.urfu.online'
MATOMO_SITE_ID = '2'
ANALYTICAL_AUTO_IDENTIFY = False
ANALYTICAL_INTERNAL_IPS = []

SELECT2_JS = 'admin/js/vendor/select2/select2.full.js'
SELECT2_CSS = 'admin/css/vendor/select2/select2.css'
SELECT2_USE_BUNDLED_JQUERY = False

MD_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/@mdi/svg@5.9.55/'

HTML_MINIFY = True
TAGGIT_CASE_INSENSITIVE = True

AUTH_ADFS = {
    "SERVER": "sts.urfu.ru",
    "CLIENT_ID": "your-configured-client-id",
    "RELYING_PARTY_ID": "your-adfs-RPT-name",
    # Make sure to read the documentation about the AUDIENCE setting
    # when you configured the identifier as a URL!
    "AUDIENCE": "microsoft:identityserver:your-RelyingPartyTrust-identifier",
    # "CA_BUNDLE": "/path/to/ca-bundle.pem",
    "CLAIM_MAPPING": {"first_name": "given_name",
                      "last_name": "family_name",
                      "email": "email"},
}

DJRICHTEXTFIELD_CONFIG = {
    'js': ['https://cdn.ckeditor.com/ckeditor5/30.0.0/classic/ckeditor.js'],
    'init_template': 'includes/dj.js',
    'settings': {
        'menubar': True,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}

VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': True
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'eduapps_logo': [
        ('logo_large', 'thumbnail__1278x500'),
        ('logo_small', 'thumbnail__639x250')
    ],
}
COMPUTEDFIELDS_ALLOW_RECURSION = True
