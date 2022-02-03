from app import db
from sqlalchemy import Column

from app.mixin import SoftDeleteMixin
from app.mixin import TimestampMixin


class Article(db.Model, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'article'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(120), nullable=False)
    content = Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
