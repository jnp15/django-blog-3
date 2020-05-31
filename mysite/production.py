import os

import dj_database_url

from .settings import *


DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS"), "localhost"]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ.get("vft2wvmefwrg34vjew4cjw09wec490gw0vpnj93jw0pmw90")