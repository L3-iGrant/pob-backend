"""
Django settings for pob_backend project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "5*p8kund7xma&pq5(2!+@fmd74%^q+z$wb*91yjnrh@%l+^+r5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'constance',
    'constance.backends.database',
    "igrant_user",
    "connections",
    "certificate",
    "buyer",
    "seller",
    "webhook",
    "verifications",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "corsheaders",
    "django_jsonfield_backport",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pob_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pob_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db", "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "igrant_user.IGrantUser"

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'igrant_user.serializers.CustomTokenSerializer'
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

if os.environ.get("ENV") == "prod":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_NAME"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": 5432,
        }
    }

django_heroku.settings(locals())

ISSUER_AGENT_URL = "https://ds-agent.igrant.io"
COMPANY_AGENT_URL = "https://dus-agent.igrant.io"


CONSTANCE_ADDITIONAL_FIELDS = {
    'json_field': ['pob_backend.fields.JsonField']
}


CONSTANCE_CONFIG = {
    'WALLET_USER_ISSUANCE_CONFIG': (
        {
            'CREDENTIAL_DEFINITION_ID': "GsMTo44BktRxUFjRVxR1nL:3:CL:3878:default",
            'CONNECTION_ID': "1ea91d13-4d58-46d3-acc1-ef9f9fd01c75",
            'DATA_AGREEMENT_ID': "e53700ae-d782-470d-ad1c-98ca72fcdf92"
        },
        'Wallet user issuance config',
        'json_field',
        ),
    'USER_VERIFICATION_DATA_AGREEMENT_ID': ("a2f8d245-fb3d-4b19-bd2d-86f2346acc88", 'User verification data agreement id'),
    'BYGG_AB_ORG_ID': ("6343ecbb6de5d70001ac038e",'Organisation id of Bygg ab agent'),
    'PROCUREMENT_PORTAL_ORG_ID': ("6364ee3781f7df00012cdaba", 'Organisation id of Procurement Portal agent'),
    'BOLAGSVERKET_ORG_ID': ("624c025d7eff6f000164bb94", 'Organisation id of Bolagsverket agent'),
    'BYGG_AB_API_KEY': ("ApiKey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2MjRjMDFlNzdlZmY2ZjAwMDE2NGJiOTIiLCJvcmdpZCI6IiIsImV4cCI6MTY4MDI1Mjk0Mn0.g6gCu7Mr1DompSXK8kQYhBUqRJ1PsOtahhxmB-klV10", 'Api key for authentication towards cloud agent'),
    'BOLAGSVERKET_API_KEY': ("ApiKey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2MzQzZWM0ZjZkZTVkNzAwMDFhYzAzOGQiLCJvcmdpZCI6IiIsImVudiI6IiIsImV4cCI6MTY5NjUwMDAxOH0.8hSeQhWhU0xg8mbJbqNhx8OHHDF_PkJdNiRrAvgkjEs", 'Api key for authentication towards cloud agent'),
    'PROCUREMENT_PORTAL_API_KEY': ("ApiKey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2MzY0ZWUwNjgxZjdkZjAwMDEyY2RhYjkiLCJvcmdpZCI6IiIsImVudiI6IiIsImV4cCI6MTY5ODY2MzI5N30.XAgBDTmlJwofuCF_P-rLoVxTBeJuKQYKtYhiyji1kS0", 'Api key for authentication towards cloud agent'),
}