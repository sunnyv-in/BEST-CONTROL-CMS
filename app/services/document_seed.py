from app.extensions import db
from app.models import DocumentLibrary


def seed_documents():

    documents = [

        "Datasheet",

        "Manual",

        "Brochure",

        "Certificate",

        "Technical Drawing",

        "Installation Guide",

        "Warranty",

        "Catalogue",

        "Test Report",

    ]

    for index, name in enumerate(documents):

        existing = DocumentLibrary.query.filter_by(
            name=name
        ).first()

        if existing:
            continue

        db.session.add(
            DocumentLibrary(
                name=name,
                display_order=index,
            )
        )

    db.session.commit()