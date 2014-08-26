from flask import Blueprint

aim = Blueprint('aim', __name__)

from . import views
