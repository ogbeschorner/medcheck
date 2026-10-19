"""Settings used only by the Django test suite."""

import os

os.environ.setdefault("DJANGO_SECRET_KEY", "test-only-placeholder-secret-key")

from .settings import *  # noqa: F403

DATABASES = {  # noqa: F405
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
