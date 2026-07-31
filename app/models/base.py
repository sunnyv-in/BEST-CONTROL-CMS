from datetime import datetime

from app.extensions import db


class TimestampMixin:
    """
    Adds created_at and updated_at timestamps
    to any model that inherits from it.
    """

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


class BaseModel(db.Model):
    """
    Base model shared by all database models.
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True
    )