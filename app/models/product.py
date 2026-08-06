from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class Product(TimestampMixin, BaseModel):
    __tablename__ = "products"

    specifications = db.relationship(
    "ProductSpecification",
    back_populates="product",
    cascade="all, delete-orphan",
    lazy=True,
    order_by="ProductSpecification.display_order"
    )

    documents = db.relationship(
    "ProductDocument",
    back_populates="product",
    cascade="all, delete-orphan",
    lazy=True,
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    gallery = db.relationship(
    "ProductImage",
    back_populates="product",
    cascade="all, delete-orphan",
    order_by="ProductImage.display_order",
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    slug = db.Column(
        db.String(170),
        unique=True,
        nullable=False,
        index=True
    )

    short_description = db.Column(
        db.String(300),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    model_number = db.Column(
        db.String(100),
        nullable=True
    )

    primary_image = db.Column(
        db.String(255),
        nullable=True
    )

    datasheet_pdf = db.Column(
        db.String(255),
        nullable=True
    )

    voltage = db.Column(
        db.String(50),
        nullable=True
    )

    current = db.Column(
        db.String(50),
        nullable=True
    )

    power_rating = db.Column(
        db.String(50),
        nullable=True
    )

    frequency = db.Column(
        db.String(50),
        nullable=True
    )

    phase = db.Column(
        db.String(50),
        nullable=True
    )

    cooling_type = db.Column(
        db.String(100),
        nullable=True
    )

    dimensions = db.Column(
        db.String(100),
        nullable=True
    )

    weight = db.Column(
        db.String(50),
        nullable=True
    )

    efficiency = db.Column(
        db.String(50),
        nullable=True
    )

    warranty = db.Column(
        db.String(100),
        nullable=True
    )

    featured = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    published = db.Column(
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

    category = db.relationship(
        "Category",
        back_populates="products"
    )

    def __repr__(self):
        return f"<Product {self.name}>"