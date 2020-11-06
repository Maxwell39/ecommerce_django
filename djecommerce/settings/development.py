from .base import *

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'frontend_ecom',
        'USER': 'blouse_01',
        'PASSWORD': 'bHybCVIN4XvKb6zF',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

STRIPE_SECRET_KEY = "sk_test_51HcnrED7n8IhDniDMGfsBBCFni4HxoqBFqjrItHYLZcsz5lCg4MkaU16KIe4gEr1FoZ0kBzrajdbSJTfj0av633r00VLA4QZsA"
STRIPE_PUBLIC_KEY = "pk_test_51HcnrED7n8IhDniDP74UEhFusZL7R3hPemxK8yOE4p2Z6532KmgbAALD63FYDWkRcWajftvodM55XhlS9D6c7cc2004dugHLy5"
