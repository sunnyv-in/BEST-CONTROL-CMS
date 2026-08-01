from app.extensions import db


class ProductImage(db.Model):

    __tablename__ = "product_images"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
    )

    image = db.Column(
        db.String(255),
        nullable=False,
    )

    is_primary = db.Column(
        db.Boolean,
        default=False,
    )

    display_order = db.Column(
        db.Integer,
        default=0,
    )

    product = db.relationship(
        "Product",
        back_populates="gallery",
    )