from app.extensions import db
from app.models import ProductGallery
from app.utils.file_upload import save_uploaded_file


def save_product_gallery(product, request):
    """
    Save gallery images for a product.
    """

    files = request.files.getlist("gallery_images[]")
    alt_texts = request.form.getlist("gallery_alt_text[]")

    for index, file in enumerate(files):

        if not file or file.filename == "":
            continue

        filename = save_uploaded_file(
            file,
            "gallery",
        )

        gallery = ProductGallery(
            product_id=product.id,
            image_path=filename,
            alt_text=(
                alt_texts[index].strip()
                if index < len(alt_texts)
                else ""
            ),
            display_order=index,
        )

        db.session.add(gallery)

    db.session.commit()