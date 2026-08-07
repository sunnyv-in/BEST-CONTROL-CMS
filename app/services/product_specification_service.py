from app.extensions import db
from app.models import ProductSpecification


def save_product_specifications(product, request):

    specification_ids = request.form.getlist("specification_id[]")
    specification_values = request.form.getlist("specification_value[]")

    custom_names = request.form.getlist("custom_specification_name[]")
    custom_values = request.form.getlist("custom_specification_value[]")

    print("\n========== SPEC DEBUG ==========")
    print("specification_id[]")
    print(specification_ids)

    print("\nspecification_value[]")
    print(specification_values)

    print("\ncustom_specification_name[]")
    print(custom_names)

    print("\ncustom_specification_value[]")
    print(custom_values)
    print("================================\n")

    # ---------------------------------------
    # Library Specifications
    # ---------------------------------------

    for index, specification_id in enumerate(specification_ids):

        if not specification_id:
            continue

        if specification_id == "custom":
            continue

        value = ""

        if index < len(specification_values):
            value = specification_values[index].strip()

        specification = ProductSpecification(
            product_id=product.id,
            specification_library_id=int(specification_id),
            value=value,
            display_order=index,
        )

        db.session.add(specification)

   # ---------------------------------------
    # Custom Specifications
    # ---------------------------------------

    custom_value_index = 0

    for custom_name in custom_names:

        custom_name = custom_name.strip()

        if not custom_name:
            continue

        value = ""

        if custom_value_index < len(custom_values):
            value = custom_values[custom_value_index].strip()

        specification = ProductSpecification(
            product_id=product.id,
            custom_name=custom_name,
            value=value,
            display_order=len(specification_ids) + custom_value_index,
        )

        db.session.add(specification)

        custom_value_index += 1