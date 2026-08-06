from app.extensions import db
from app.models import ProductSpecification



def save_product_specifications(product, request):


    specification_ids = request.form.getlist("specification_id[]")

    specification_values = request.form.getlist("specification_value[]")

    custom_names = request.form.getlist("custom_specification_name[]")
    custom_values = request.form.getlist("custom_specification_value[]")

    for index, value in enumerate(specification_values):

        value = value.strip()

        if not value:
            continue

        specification = ProductSpecification(

            product_id=product.id,

            value=value,

            display_order=index,

        )

        if (
            index < len(specification_ids)
            and specification_ids[index]
        ):

            if specification_ids[index] == "custom":

                if (
                    index < len(custom_names)
                    and custom_names[index].strip()
                ):

                    specification.custom_name = custom_names[index].strip()

            else:

                specification.specification_library_id = int(
                    specification_ids[index]
                )

        db.session.add(specification)
        

    # -------------------------
    # Save Custom Specifications
    # -------------------------

    for index, custom_name in enumerate(custom_names):

        custom_name = custom_name.strip()

        if not custom_name:
            continue

        value = ""

        if index < len(custom_values):
            value = custom_values[index].strip()

        specification = ProductSpecification(

            product_id=product.id,

            custom_name=custom_name,

            value=value,

            display_order=len(specification_values) + index,

        )

        db.session.add(specification)

        db.session.commit()

   