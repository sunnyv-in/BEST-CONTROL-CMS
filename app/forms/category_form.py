from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField(
        "Category Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    slug = StringField(
        "Slug",
        validators=[
            DataRequired(),
            Length(max=120)
        ]
    )

    description = TextAreaField(
        "Description"
    )

    is_active = BooleanField(
        "Active",
        default=True
    )

    submit = SubmitField("Save Category")