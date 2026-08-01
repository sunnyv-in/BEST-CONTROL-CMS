from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class Category(TimestampMixin, BaseModel):
    __tablename__ = "categories"

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    slug = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    image = db.Column(
        db.String(255),
        nullable=True
    )

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    meta_title = db.Column(
        db.String(255),
        nullable=True
    )

    meta_description = db.Column(
        db.Text,
        nullable=True
    )

    products = db.relationship(
        "Product",
        back_populates="category",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"