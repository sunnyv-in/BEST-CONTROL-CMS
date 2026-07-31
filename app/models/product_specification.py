from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class ProductSpecification(TimestampMixin, BaseModel):
    __tablename__ = "product_specifications"

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    value = db.Column(
        db.String(255),
        nullable=False
    )

    unit = db.Column(
        db.String(30),
        nullable=True
    )

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    product = db.relationship(
        "Product",
        back_populates="specifications"
    )

    def __repr__(self):
        return f"<Specification {self.name}: {self.value}>"