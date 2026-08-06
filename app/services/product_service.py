from app.extensions import db
from app.models import Product, product
from app.utils.file_upload import save_uploaded_file
from app.services.product_specification_service import (
    save_product_specifications,
)

from app.services.product_document_service import (
    save_product_documents,
)


def create_product(form, request):

    image_filename = None

    if form.primary_image.data:

        image_filename = save_uploaded_file(
            form.primary_image.data,
            "products",
        )

    product = Product(

        category_id=form.category_id.data,

        name=form.name.data,

        slug=form.slug.data,

        model_number=form.model_number.data,

        short_description=form.short_description.data,

        featured=form.featured.data,

        published=form.published.data,

        primary_image=image_filename,

    )

    db.session.add(product)
    db.session.commit()

    # -------------------------
    # Save Specifications
    # -------------------------

    save_product_specifications(
        product,
        request,
    )

    # -------------------------
    # Save Documents
    # -------------------------

    save_product_documents(
        product,
        request,
    )

    return product