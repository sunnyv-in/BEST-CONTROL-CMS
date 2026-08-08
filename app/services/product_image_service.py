from app.extensions import db
from app.models import ProductImage
from app.utils.file_upload import save_uploaded_file


def save_product_images(product, request):
    """
    Handles product gallery images.

    Supports:
    - Existing gallery images
    - New image uploads
    - Alt text
    - Delete existing images
    - Set primary image
    - Automatic primary image fallback
    """

    # ============================================================
    # EXISTING IMAGES
    # ============================================================

    image_ids = request.form.getlist(
        "product_image_id[]"
    )

    delete_flags = request.form.getlist(
        "delete_product_image[]"
    )

    primary_flags = request.form.getlist(
        "product_image_primary[]"
    )

    alt_texts = request.form.getlist(
        "product_image_alt_text[]"
    )

    # ============================================================
    # NEW IMAGES
    # ============================================================

    new_files = request.files.getlist(
        "new_product_image[]"
    )

    new_alt_texts = request.form.getlist(
        "new_product_image_alt_text[]"
    )

    # ============================================================
    # PRIMARY IMAGE TRACKING
    # ============================================================

    primary_image_id = None

    # ============================================================
    # UPDATE EXISTING IMAGES
    # ============================================================

    for index, image_id in enumerate(image_ids):

        if not image_id:
            continue

        try:
            image_id = int(image_id)

        except (TypeError, ValueError):
            continue

        image = ProductImage.query.filter_by(
            id=image_id,
            product_id=product.id,
        ).first()

        if not image:
            continue

        # --------------------------------------------------------
        # DELETE
        # --------------------------------------------------------

        if (
            index < len(delete_flags)
            and delete_flags[index] == "1"
        ):

            db.session.delete(image)

            continue

        # --------------------------------------------------------
        # ALT TEXT
        # --------------------------------------------------------

        if index < len(alt_texts):

            image.alt_text = (
                alt_texts[index].strip()
            )

        # --------------------------------------------------------
        # PRIMARY
        # --------------------------------------------------------

        if (
            index < len(primary_flags)
            and primary_flags[index] == "1"
        ):

            primary_image_id = image.id

    # ============================================================
    # CREATE NEW IMAGES
    # ============================================================

    current_count = ProductImage.query.filter_by(
        product_id=product.id
    ).count()

    for index, file in enumerate(new_files):

        if not file or file.filename == "":
            continue

        filename = save_uploaded_file(
            file,
            "products",
        )

        alt_text = ""

        if index < len(new_alt_texts):

            alt_text = (
                new_alt_texts[index].strip()
            )

        image = ProductImage(
            product_id=product.id,

            image=filename,

            alt_text=alt_text,

            is_primary=False,

            display_order=current_count + index,
        )

        db.session.add(image)

        db.session.flush()

        # --------------------------------------------------------
        # If product has no primary image,
        # make first new image primary.
        # --------------------------------------------------------

        if primary_image_id is None:

            existing_primary = ProductImage.query.filter_by(
                product_id=product.id,
                is_primary=True,
            ).first()

            if not existing_primary:

                primary_image_id = image.id

    # ============================================================
    # PRIMARY IMAGE
    # ============================================================

    if primary_image_id:

        # Make every other image non-primary

        ProductImage.query.filter(
            ProductImage.product_id == product.id,
            ProductImage.id != primary_image_id,
        ).update(
            {
                ProductImage.is_primary: False,
            },
            synchronize_session=False,
        )

        primary = ProductImage.query.filter_by(
            id=primary_image_id,
            product_id=product.id,
        ).first()

        if primary:

            primary.is_primary = True

            # Keep gallery order
            primary.display_order = primary.display_order

    else:

        # --------------------------------------------------------
        # Make sure one image remains primary
        # --------------------------------------------------------

        remaining_primary = ProductImage.query.filter_by(
            product_id=product.id,
            is_primary=True,
        ).first()

        if not remaining_primary:

            first_image = (
                ProductImage.query
                .filter_by(
                    product_id=product.id
                )
                .order_by(
                    ProductImage.display_order
                )
                .first()
            )

            if first_image:

                first_image.is_primary = True

    # ============================================================
    # SAVE
    # ============================================================

    db.session.commit()