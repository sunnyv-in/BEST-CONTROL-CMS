from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class SpecificationLibrary(TimestampMixin, BaseModel):
    __tablename__ = "specification_library"

    name = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
    )

    group = db.Column(
        db.String(80),
        nullable=False,
    )

    data_type = db.Column(
        db.String(30),
        default="text",
        nullable=False,
    )

    unit = db.Column(
        db.String(30),
        nullable=True,
    )

    is_required = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    is_filterable = db.Column(
        db.Boolean,
        default=True,
        nullable=False,
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

    product_specifications = db.relationship(
    "ProductSpecification",
    back_populates="specification",
)

    def __repr__(self):
        return f"<SpecificationLibrary {self.name}>"