from flask import Blueprint
from flask import render_template

index_bp = Blueprint('/', __name__, url_prefix='/', template_folder="templates")


@index_bp.get("/")
def space(name):
    return render_template("index.html")
