from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class ProductDocument(TimestampMixin, BaseModel):
    __tablename__ = "product_documents"

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
    )

    document_library_id = db.Column(
        db.Integer,
        db.ForeignKey("document_library.id"),
        nullable=True,
    )

    custom_type = db.Column(
        db.String(120),
        nullable=True,
    )

    display_name = db.Column(
        db.String(200),
        nullable=False,
    )

    file_name = db.Column(
        db.String(255),
        nullable=False,
    )

    file_path = db.Column(
        db.String(500),
        nullable=False,
    )

    file_size = db.Column(
        db.Integer,
        nullable=True,
    )

    mime_type = db.Column(
        db.String(100),
        nullable=True,
    )

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    product = db.relationship(
        "Product",
        back_populates="documents",
    )

    document = db.relationship(
        "DocumentLibrary",
        back_populates="product_documents",
        lazy="joined",
    )

    def __repr__(self):
        return f"<ProductDocument {self.display_name}>"