from flask import Blueprint
from flask import render_template

from app.article.model import Article

space_bp = Blueprint('space', __name__, url_prefix='/space', template_folder="templates")
index_bp = Blueprint('index', __name__, url_prefix='/', template_folder="templates")


@space_bp.get("/<string:name>")
def space(name):
    return render_template(f"{name}space.html")


@space_bp.get("/")
@index_bp.get("/")
def index():
    return render_template("index.html")
