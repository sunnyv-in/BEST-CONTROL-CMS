from app.models import SpecificationLibrary


def get_active_specifications():
    return (
        SpecificationLibrary.query
        .filter_by(is_active=True)
        .order_by(
            SpecificationLibrary.group,
            SpecificationLibrary.display_order,
            SpecificationLibrary.name
        )
        .all()
    )