from app.extensions import db
from app.models.base import BaseModel, TimestampMixin


class DocumentLibrary(TimestampMixin, BaseModel):
    __tablename__ = "document_library"

    name = db.Column(
        db.String(100),
        unique=True,
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

    product_documents = db.relationship(
        "ProductDocument",
        back_populates="document",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<DocumentLibrary {self.name}>"