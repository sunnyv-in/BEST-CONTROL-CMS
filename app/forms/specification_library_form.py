from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    BooleanField,
    SelectField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length


class SpecificationLibraryForm(FlaskForm):

    name = StringField(
        "Specification Name",
        validators=[
            DataRequired(),
            Length(max=120),
        ],
    )

    group = SelectField(
        "Group",
        choices=[
            ("Electrical", "Electrical"),
            ("Mechanical", "Mechanical"),
            ("Environmental", "Environmental"),
            ("General", "General"),
        ],
        validators=[DataRequired()],
    )

    data_type = SelectField(
        "Data Type",
        choices=[
            ("text", "Text"),
            ("number", "Number"),
            ("dropdown", "Dropdown"),
            ("boolean", "Yes / No"),
        ],
        default="text",
    )

    unit = StringField(
        "Unit",
        validators=[
            Length(max=30),
        ],
    )

    is_required = BooleanField(
        "Required",
        default=False,
    )

    is_filterable = BooleanField(
        "Filterable",
        default=True,
    )

    display_order = IntegerField(
        "Display Order",
        default=0,
    )

    is_active = BooleanField(
        "Active",
        default=True,
    )

    submit = SubmitField(
        "Save Specification"
    )