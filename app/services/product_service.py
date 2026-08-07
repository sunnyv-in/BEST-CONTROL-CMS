from app.extensions import db

from app.models import (
    Product,
    ProductSpecification,
    ProductDocument,
)

from app.utils.file_upload import save_uploaded_file

from app.services.product_specification_service import (
    save_product_specifications,
)

from app.services.product_document_service import (
    save_product_documents,
)


# =====================================================
# Create Product
# =====================================================

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

        description=form.description.data,

        featured=form.featured.data,

        published=form.published.data,

        primary_image=image_filename,

        meta_title=(
            form.meta_title.data.strip()
            if form.meta_title.data
            else f"{form.name.data} | BEST CONTROL"
        ),

        meta_description=(
            form.meta_description.data.strip()
            if form.meta_description.data
            else f"Buy {form.name.data} from BEST CONTROL. {form.short_description.data or ''}"
        ),

        keywords=(
            form.keywords.data.strip()
            if form.keywords.data
            else ", ".join(
                filter(
                    None,
                    [
                        form.name.data,
                        "Transformer",
                        form.model_number.data,
                        "BEST CONTROL",
                    ],
                )
            )
        ),
    )

    db.session.add(product)
    db.session.commit()

    save_product_specifications(
        product,
        request,
    )

    save_product_documents(
        product,
        request,
    )

    db.session.commit()

    return product


# =====================================================
# Update Product
# =====================================================

def update_product(product, form, request):

    product.category_id = form.category_id.data
    product.name = form.name.data
    product.slug = form.slug.data
    product.model_number = form.model_number.data

    product.short_description = form.short_description.data
    product.description = form.description.data

    product.featured = form.featured.data
    product.published = form.published.data

    product.meta_title = (
        form.meta_title.data.strip()
        if form.meta_title.data
        else f"{form.name.data} | BEST CONTROL"
    )

    product.meta_description = (
        form.meta_description.data.strip()
        if form.meta_description.data
        else f"Buy {form.name.data} from BEST CONTROL. {form.short_description.data or ''}"
    )

    product.keywords = (
        form.keywords.data.strip()
        if form.keywords.data
        else ", ".join(
            filter(
                None,
                [
                    form.name.data,
                    "Transformer",
                    form.model_number.data,
                    "BEST CONTROL",
                ],
            )
        )
    )

    # -------------------------
    # Replace image only if uploaded
    # -------------------------

    if form.primary_image.data:

        product.primary_image = save_uploaded_file(
            form.primary_image.data,
            "products",
        )

    db.session.commit()

    # -------------------------
    # Update Specifications
    # -------------------------

    ProductSpecification.query.filter_by(
        product_id=product.id
    ).delete()

    save_product_specifications(
        product,
        request,
    )

    # -------------------------
    # Update Documents
    # -------------------------

    save_product_documents(
        product,
        request,
    )

    db.session.commit()

    return product