from app import db
from app.utils import get_current_timestamp_CST


class TimestampMixin():
    created = db.Column(
        db.DateTime, nullable=False, default=get_current_timestamp_CST())
    updated = db.Column(db.DateTime, onupdate=get_current_timestamp_CST())


class SoftDeleteMixin():
    is_deleted = db.Column(db.Boolean, default=False)