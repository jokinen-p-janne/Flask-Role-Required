from flask import Blueprint

bp = Blueprint('auth', __name__)

from project.auth import routes  # noqa:E402,F401
