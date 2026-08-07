from app.extensions import db
from app.models import ProductDocument
from app.utils.file_upload import save_uploaded_file



def save_product_documents(product, request):
    """
    Handles both:
        - Creating new documents
        - Updating existing documents
    Existing PDFs remain unless a new file is uploaded.
    """


    # ============================================================
    # LIBRARY DOCUMENTS
    # ============================================================

    product_document_ids = request.form.getlist(
        "product_document_id[]"
    )

    document_library_ids = request.form.getlist(
        "document_library_id[]"
    )

    display_names = request.form.getlist(
        "document_display_name[]"
    )

    files = request.files.getlist(
        "document_file[]"
    )

    delete_flags = request.form.getlist(
    "delete_document[]"
    )

    for index, library_id in enumerate(document_library_ids):

        if not library_id:
            continue

        existing = None

        if (
            index < len(product_document_ids)
            and product_document_ids[index]
        ):

            existing = ProductDocument.query.get(
                int(product_document_ids[index])
            )

        # -------------------------
        # Delete Existing Document
        # -------------------------

        if (
            existing
            and index < len(delete_flags)
            and delete_flags[index] == "1"
        ):

            db.session.delete(existing)

            continue

        if existing:

            existing.document_library_id = int(library_id)

            existing.display_name = (
                display_names[index]
                if index < len(display_names)
                else existing.display_name
            )

            existing.display_order = index

            # Only replace PDF if user selected one
            if (
                index < len(files)
                and files[index]
                and files[index].filename != ""
            ):

                filename = save_uploaded_file(
                    files[index],
                    "documents",
                )

                existing.file_path = filename
                existing.file_name = files[index].filename
                existing.mime_type = files[index].mimetype

            # IMPORTANT
            db.session.add(existing)

            continue

        else:

            if (
                index >= len(files)
                or not files[index]
                or files[index].filename == ""
            ):
                continue

            filename = save_uploaded_file(
                files[index],
                "documents",
            )

            db.session.add(
                ProductDocument(
                    product_id=product.id,
                    document_library_id=int(library_id),
                    display_name=display_names[index]
                    if index < len(display_names)
                    else "",
                    file_name=files[index].filename,
                    file_path=filename,
                    file_size=0,
                    mime_type=files[index].mimetype,
                    display_order=index,
                )
            )

    # ============================================================
    # CUSTOM DOCUMENTS
    # ============================================================

    custom_document_ids = request.form.getlist(
        "custom_product_document_id[]"
    )

    custom_types = request.form.getlist(
        "custom_document_type[]"
    )

    custom_display_names = request.form.getlist(
        "custom_document_display_name[]"
    )

    custom_files = request.files.getlist(
        "custom_document_file[]"
    )

    offset = len(document_library_ids)

    for index, custom_type in enumerate(custom_types):

        if not custom_type.strip():
            continue

        existing = None

        # -------------------------
        # Delete Existing Document
        # -------------------------

        if (
            existing
            and index < len(delete_flags)
            and delete_flags[index] == "1"
        ):

            db.session.delete(existing)

            continue

        if (
            index < len(custom_document_ids)
            and custom_document_ids[index]
        ):
            existing = ProductDocument.query.get(
                int(custom_document_ids[index])
            )

        if existing:

            existing.custom_type = custom_type.strip()

            existing.display_name = (
                custom_display_names[index]
                if index < len(custom_display_names)
                else existing.display_name
            )

            existing.display_order = offset + index

            # Only replace PDF if a new one is uploaded
            if (
                index < len(custom_files)
                and custom_files[index]
                and custom_files[index].filename != ""
            ):

                filename = save_uploaded_file(
                    custom_files[index],
                    "documents",
                )

                existing.file_path = filename
                existing.file_name = custom_files[index].filename
                existing.mime_type = custom_files[index].mimetype

            db.session.add(existing)

            continue

        else:

            if (
                index >= len(custom_files)
                or not custom_files[index]
                or custom_files[index].filename == ""
            ):
                continue

            filename = save_uploaded_file(
                custom_files[index],
                "documents",
            )

            db.session.add(
                ProductDocument(
                    product_id=product.id,
                    custom_type=custom_type.strip(),
                    display_name=custom_display_names[index]
                    if index < len(custom_display_names)
                    else "",
                    file_name=custom_files[index].filename,
                    file_path=filename,
                    file_size=0,
                    mime_type=custom_files[index].mimetype,
                    display_order=offset + index,
                )
            )

    db.session.commit()