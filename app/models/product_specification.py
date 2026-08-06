from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class ProductSpecification(TimestampMixin, BaseModel):
    __tablename__ = "product_specifications"

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
    )

    specification_library_id = db.Column(
    db.Integer,
    db.ForeignKey("specification_library.id"),
    nullable=True,
)
    custom_name = db.Column(
    db.String(120),
    nullable=True,
)

    value = db.Column(
    db.Text,
    nullable=False,
)

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    # Relationship with Product
    product = db.relationship(
        "Product",
        back_populates="specifications",
    )

    # Relationship with Specification Library
    specification = db.relationship(
        "SpecificationLibrary",
        back_populates="product_specifications",
        lazy="joined",
    )

    def __repr__(self):
        return f"<ProductSpecification {self.value}>"