from app.extensions import db
from app.models import SpecificationLibrary


DEFAULT_SPECIFICATIONS = [

    # -------------------------
    # Electrical
    # -------------------------

    ("Power Rating", "Electrical", "text", "VA"),
    ("Input Voltage", "Electrical", "text", "VAC"),
    ("Output Voltage", "Electrical", "text", "VAC"),
    ("Frequency", "Electrical", "text", "Hz"),
    ("Current", "Electrical", "text", "A"),

    # -------------------------
    # Mechanical
    # -------------------------

    ("Dimensions", "Mechanical", "text", "mm"),
    ("Weight", "Mechanical", "text", "kg"),

    # -------------------------
    # General
    # -------------------------

    ("Phase", "General", "text", ""),
    ("Cooling Type", "General", "text", ""),
    ("Efficiency", "General", "text", "%"),
    ("Insulation Class", "General", "text", ""),
]


def seed_specifications():

    if SpecificationLibrary.query.count() > 0:

        print("Specification Library already seeded.")

        return

    for index, item in enumerate(DEFAULT_SPECIFICATIONS):

        specification = SpecificationLibrary(

            name=item[0],

            group=item[1],

            data_type=item[2],

            unit=item[3],

            display_order=index,

            is_active=True,

        )

        db.session.add(specification)

    db.session.commit()

    print("Specifications Seeded Successfully.")