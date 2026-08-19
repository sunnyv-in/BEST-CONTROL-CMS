from app.extensions import db


class CompanyMedia(db.Model):

    __tablename__ = "company_media"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.String(150),
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=True,
    )

    media_type = db.Column(
        db.String(20),
        nullable=False,
        default="image",
    )

    file = db.Column(
        db.String(255),
        nullable=False,
    )

    alt_text = db.Column(
        db.String(255),
        nullable=True,
    )

    category = db.Column(
        db.String(100),
        nullable=True,
    )

    featured = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    display_order = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False,
    )

    def __repr__(self):
        return f"<CompanyMedia {self.title}>"