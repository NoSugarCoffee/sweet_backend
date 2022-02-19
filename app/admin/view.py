from flask import Blueprint
from flask import render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder="templates")


@admin_bp.get("/")
def article():
    return render_template("admin/index.html")