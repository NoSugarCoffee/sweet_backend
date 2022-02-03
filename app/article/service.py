from app import db
from app.article import model


def add_article(validated_article):
    article = model.Article(**validated_article)
    db.session.add(article)
    db.session.commit()