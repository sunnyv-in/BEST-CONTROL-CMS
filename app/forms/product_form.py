from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    BooleanField,
    SubmitField,
)

from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):

    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[DataRequired()]
    )

    name = StringField(
        "Product Name",
        validators=[
            DataRequired(),
            Length(max=150)
        ]
    )

    slug = StringField(
        "Slug",
        validators=[
            DataRequired(),
            Length(max=170)
        ]
    )

    model_number = StringField(
        "Model Number"
    )

    short_description = TextAreaField(
        "Short Description"
    )

    description = TextAreaField(
    "Description"
    )

    primary_image = FileField(
        "Primary Image",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "webp"],
                "Images only!"
            )
        ]
    )

    featured = BooleanField(
        "Featured"
    )
    
    published = BooleanField(
        "Published",
        default=True
    )

    meta_title = StringField(
    "Meta Title",
    validators=[
        Length(max=255)
    ]
    )

    meta_description = TextAreaField(
        "Meta Description"
    )

    keywords = TextAreaField(
        "Keywords"
    )

    submit = SubmitField(
        "Save Product"
    )