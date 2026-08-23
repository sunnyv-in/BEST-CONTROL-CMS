from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class Certificate(TimestampMixin, BaseModel):
    __tablename__ = "certificates"

    name = db.Column(
        db.String(150),
        nullable=False,
    )

    issuing_organization = db.Column(
        db.String(150),
        nullable=True,
    )

    certificate_number = db.Column(
        db.String(150),
        nullable=True,
    )

    issue_date = db.Column(
        db.Date,
        nullable=True,
    )

    expiry_date = db.Column(
        db.Date,
        nullable=True,
    )

    description = db.Column(
        db.Text,
        nullable=True,
    )

    file = db.Column(
        db.String(255),
        nullable=False,
    )

    file_type = db.Column(
        db.String(20),
        nullable=False,
        default="pdf",
    )

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False,
    )

    featured = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    def __repr__(self):
        return f"<Certificate {self.name}>"