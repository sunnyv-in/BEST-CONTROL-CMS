from app.extensions import db
from app.models import ProductDocument
from app.utils.file_upload import save_uploaded_file


def save_product_documents(product, request):

    # -------------------------
    # Library Documents
    # -------------------------

    document_ids = request.form.getlist(
        "document_library_id[]"
    )

    display_names = request.form.getlist(
        "document_display_name[]"
    )

    files = request.files.getlist(
        "document_file[]"
    )

    for index, document_id in enumerate(document_ids):

        if not document_id:
            continue

        if index >= len(files):
            continue

        file = files[index]

        if not file or file.filename == "":
            continue

        filename = save_uploaded_file(
            file,
            "documents",
        )

        document = ProductDocument(

            product_id=product.id,

            document_library_id=int(document_id),

            display_name=display_names[index],

            file_name=file.filename,

            file_path=filename,

            file_size=0,

            mime_type=file.mimetype,

            display_order=index,

        )

        db.session.add(document)

    # -------------------------
    # Custom Documents
    # -------------------------

    custom_types = request.form.getlist(
        "custom_document_type[]"
    )

    custom_display_names = request.form.getlist(
        "custom_document_display_name[]"
    )

    custom_files = request.files.getlist(
        "custom_document_file[]"
    )

    for index, custom_type in enumerate(custom_types):

        if not custom_type.strip():
            continue

        if index >= len(custom_files):
            continue

        file = custom_files[index]

        if not file or file.filename == "":
            continue

        filename = save_uploaded_file(
            file,
            "documents",
        )

        document = ProductDocument(

            product_id=product.id,

            custom_type=custom_type.strip(),

            display_name=custom_display_names[index],

            file_name=file.filename,

            file_path=filename,

            file_size=0,

            mime_type=file.mimetype,

            display_order=len(document_ids) + index,

        )

        db.session.add(document)

    db.session.commit()