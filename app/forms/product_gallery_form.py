from flask_wtf import FlaskForm
from flask_wtf.file import (
    MultipleFileField,
    FileAllowed,
)
from wtforms import SubmitField


class ProductGalleryForm(FlaskForm):

    images = MultipleFileField(
        "Gallery Images",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "webp"],
                "Images only!"
            )
        ],
    )

    submit = SubmitField(
        "Upload Images"
    )
    