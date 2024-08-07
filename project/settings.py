"""
Django settings for project project.
Generated by 'django-admin startproject' using Django 5.0.6.
"""

from project.envs import BASE_DIR, env

"""
Third party apps and django apps
"""
DJANGO_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "blog_stack.accounts",
    "blog_stack.core",
]
THIRD_PARTY_APPS = [
    "waffle",
    "django_extensions",
    "allauth",
    "allauth.account",
    # Optional -- requires install using `django-allauth[socialaccount]`.
    # "allauth.socialaccount",
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

"""
Core Django settings
Django settings extracted from environment variables.
These settings are configured based on environment variables using the `env` utility.
"""
DEBUG = env.bool("DEBUG")
SECRET_KEY = env.str("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
DJANGO_ADMIN_URL = env.str("DJANGO_ADMIN_URL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

"""
Authentication settings for Django project.
Includes settings related to user authentication, such as login, logout, and password management.
"""
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = env("ACCOUNT_DEFAULT_HTTP_PROTOCOL")
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "DjangoBlog "
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_BLACKLIST = ''

SITE_ID = 1
AUTH_USER_MODEL = "accounts.User"
EMAIL_BACKEND = env.str("EMAIL_BACKEND")
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

"""
Django middleware
"""
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "waffle.middleware.WaffleMiddleware",
]

"""
Paths and URLs Static files
"""
ROOT_URLCONF = "project.urls"
WSGI_APPLICATION = "project.wsgi.application"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

"""
Template settings
"""
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]

"""
Miscellaneous 
"""
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GRAPH_MODELS = {
    "app_labels": [
        "accounts",
        "core",
    ],
    "rankdir": "BT",
    "output": "models.png",
}

# django-waffle
WAFFLE_CREATE_MISSING_FLAGS = True
