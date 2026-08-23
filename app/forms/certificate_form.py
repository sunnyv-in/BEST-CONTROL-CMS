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
    DateField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
)


class CertificateForm(FlaskForm):

    name = StringField(
        "Certificate Name",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
    )

    issuing_organization = StringField(
        "Issuing Organization",
        validators=[
            Length(max=150),
        ],
    )

    certificate_number = StringField(
        "Certificate Number",
        validators=[
            Length(max=150),
        ],
    )

    issue_date = DateField(
        "Issue Date",
        format="%Y-%m-%d",
    )

    expiry_date = DateField(
        "Expiry Date",
        format="%Y-%m-%d",
    )

    description = TextAreaField(
        "Description",
    )

    file = FileField(
        "Certificate File",
        validators=[
            FileAllowed(
                [
                    "pdf",
                    "jpg",
                    "jpeg",
                    "png",
                    "webp",
                ],
                "PDF or image files only!",
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

    featured = BooleanField(
        "Featured",
        default=False,
    )

    submit = SubmitField(
        "Save Certificate"
    )