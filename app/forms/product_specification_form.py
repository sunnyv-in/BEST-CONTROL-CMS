from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length


class ProductSpecificationForm(FlaskForm):

    specification_name = SelectField(
        "Specification",
        choices=[
            ("Input Voltage", "Input Voltage"),
            ("Output Voltage", "Output Voltage"),
            ("Power Rating", "Power Rating"),
            ("Output Current", "Output Current"),
            ("Frequency", "Frequency"),
            ("Phase", "Phase"),
            ("Cooling Type", "Cooling Type"),
            ("Efficiency", "Efficiency"),
            ("Dimensions", "Dimensions"),
            ("Weight", "Weight"),
            ("Warranty", "Warranty"),
            ("Other", "Other"),
        ],
        validators=[DataRequired()],
    )

    custom_name = StringField(
        "Custom Specification",
        validators=[Length(max=120)],
    )

    value = StringField(
        "Value",
        validators=[
            DataRequired(),
            Length(max=255),
        ],
    )

    submit = SubmitField("Add Specification")