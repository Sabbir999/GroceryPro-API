from emea_wholesale_api.settings.local import *


DEBUG = True
ALLOW_MASTER_DB_MIGRATION = True
TESTING = True
ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.joinpath("test_app_db.sqlite3"),
    }
}