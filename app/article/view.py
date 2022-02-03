from flask import Blueprint
from flask import render_template

from app.article.model import Article

articles_bp = Blueprint('articles', __name__, url_prefix='/articles', template_folder="templates")


@articles_bp.get("/<int:article_id>")
def article(article_id):
    arcticle = Article.query.filter(Article.id == article_id).first()
    return render_template("article.html", arcticle=arcticle)