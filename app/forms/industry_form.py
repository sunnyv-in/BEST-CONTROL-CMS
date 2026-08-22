from flask_wtf import FlaskForm

from flask_wtf.file import (
    FileField,
    FileAllowed,
)

from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    IntegerField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
)


class IndustryForm(FlaskForm):

    name = StringField(
        "Industry Name",
        validators=[
            DataRequired(),
            Length(max=100),
        ],
    )

    slug = StringField(
        "Slug",
        validators=[
            Length(max=120),
        ],
    )

    description = TextAreaField(
        "Description"
    )

    image = FileField(
        "Industry Image",
        validators=[
            FileAllowed(
                [
                    "jpg",
                    "jpeg",
                    "png",
                    "webp",
                ],
                "Images only!",
            )
        ],
    )

    display_order = IntegerField(
        "Display Order",
        default=0,
        validators=[
            NumberRange(min=0),
        ],
    )

    is_active = BooleanField(
        "Active",
        default=True,
    )

    meta_title = StringField(
        "Meta Title",
        validators=[
            Length(max=255),
        ],
    )

    meta_description = TextAreaField(
        "Meta Description"
    )

    submit = SubmitField(
        "Save Industry"
    )