from flask import (Blueprint, request)
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.form)
        return 'POST /reptiles'
    else:
        return 'GET /reptiles'