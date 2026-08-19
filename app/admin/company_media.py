import os
import uuid

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
    current_app,
)

from flask_login import login_required
from werkzeug.utils import secure_filename

from app.admin import admin_bp
from app.extensions import db
from app.models import CompanyMedia


# ==========================================
# Allowed Company Media Extensions
# ==========================================

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
    "gif",
}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ==========================================
# Company Media List
# ==========================================

@admin_bp.route("/company-media")
@login_required
def company_media_list():

    media = (
        CompanyMedia.query
        .order_by(
            CompanyMedia.display_order,
            CompanyMedia.created_at.desc(),
        )
        .all()
    )

    return render_template(
        "admin/company_media/index.html",
        media=media,
    )


# ==========================================
# Create Company Media
# ==========================================

@admin_bp.route(
    "/company-media/create",
    methods=["GET", "POST"],
)
@login_required
def create_company_media():

    if request.method == "POST":

        # ------------------------------
        # Form Data
        # ------------------------------

        title = request.form.get(
            "title",
            "",
        ).strip()

        alt_text = request.form.get(
            "alt_text",
            "",
        ).strip()

        category = request.form.get(
            "category",
            "",
        ).strip()

        description = request.form.get(
            "description",
            "",
        ).strip()

        media_type = request.form.get(
            "media_type",
            "image",
        ).strip()

        featured = (
            request.form.get("featured") == "on"
        )

        display_order = request.form.get(
            "display_order",
            "0",
        )

        # ------------------------------
        # Validate Display Order
        # ------------------------------

        try:
            display_order = int(display_order)
        except (TypeError, ValueError):
            display_order = 0

        # ------------------------------
        # Validate Title
        # ------------------------------

        if not title:

            flash(
                "Title is required.",
                "danger",
            )

            return render_template(
                "admin/company_media/create.html"
            )

        # ------------------------------
        # Get Uploaded File
        # ------------------------------

        file = request.files.get("file")

        if not file or not file.filename:

            flash(
                "Please select an image.",
                "danger",
            )

            return render_template(
                "admin/company_media/create.html"
            )

        # ------------------------------
        # Validate File Type
        # ------------------------------

        if not allowed_file(file.filename):

            flash(
                "Invalid image format. "
                "Allowed formats: JPG, JPEG, PNG, WEBP and GIF.",
                "danger",
            )

            return render_template(
                "admin/company_media/create.html"
            )

        # ------------------------------
        # Create Upload Directory
        # ------------------------------

        upload_folder = os.path.join(
            current_app.static_folder,
            "uploads",
            "company_media",
        )

        os.makedirs(
            upload_folder,
            exist_ok=True,
        )

        # ------------------------------
        # Generate Safe Unique Filename
        # ------------------------------

        original_filename = secure_filename(
            file.filename
        )

        extension = (
            original_filename
            .rsplit(".", 1)[1]
            .lower()
        )

        filename = (
            f"{uuid.uuid4().hex}.{extension}"
        )

        file_path = os.path.join(
            upload_folder,
            filename,
        )

        # ------------------------------
        # Save Physical File
        # ------------------------------

        file.save(file_path)

        # ------------------------------
        # Create Database Record
        # ------------------------------

        media = CompanyMedia(
            title=title,
            description=description or None,
            media_type=media_type,
            file=filename,
            alt_text=alt_text or None,
            category=category or None,
            featured=featured,
            display_order=display_order,
        )

        db.session.add(media)
        db.session.commit()

        # ------------------------------
        # Success
        # ------------------------------

        flash(
            "Company media added successfully.",
            "success",
        )

        return redirect(
            url_for(
                "admin.company_media_list"
            )
        )

    return render_template(
        "admin/company_media/create.html"
    )

# ==========================================
# Edit Company Media
# ==========================================

@admin_bp.route("/company-media/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_company_media(id):

    media = CompanyMedia.query.get_or_404(id)

    if request.method == "POST":

        # --------------------------------------
        # Basic information
        # --------------------------------------

        media.title = request.form.get(
            "title",
            ""
        ).strip()

        media.alt_text = request.form.get(
            "alt_text",
            ""
        ).strip()

        media.category = request.form.get(
            "category",
            ""
        ).strip()

        media.description = request.form.get(
            "description",
            ""
        ).strip()

        # --------------------------------------
        # Display order
        # --------------------------------------

        try:
            media.display_order = int(
                request.form.get(
                    "display_order",
                    0
                )
            )
        except (TypeError, ValueError):
            media.display_order = 0

        # --------------------------------------
        # Featured
        # --------------------------------------

        media.featured = (
            request.form.get("featured") == "on"
        )

        # --------------------------------------
        # Optional image replacement
        # --------------------------------------

        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename:

            from werkzeug.utils import secure_filename

            filename = secure_filename(
                uploaded_file.filename
            )

            upload_folder = os.path.join(
                "app",
                "static",
                "uploads",
                "company_media",
            )

            os.makedirs(
                upload_folder,
                exist_ok=True,
            )

            # Generate a unique filename
            import uuid

            extension = os.path.splitext(
                filename
            )[1].lower()

            new_filename = (
                f"{uuid.uuid4().hex}{extension}"
            )

            new_file_path = os.path.join(
                upload_folder,
                new_filename,
            )

            # Save new image
            uploaded_file.save(
                new_file_path
            )

            # Delete old image
            if media.file:

                old_file_path = os.path.join(
                    upload_folder,
                    media.file,
                )

                if os.path.exists(
                    old_file_path
                ):
                    try:
                        os.remove(
                            old_file_path
                        )
                    except OSError:
                        pass

            # Update database
            media.file = new_filename

        # --------------------------------------
        # Save changes
        # --------------------------------------

        db.session.commit()

        flash(
            "Company media updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "admin.company_media_list"
            )
        )

    return render_template(
        "admin/company_media/edit.html",
        media=media,
    )


# ==========================================
# Delete Company Media
# ==========================================

@admin_bp.route(
    "/company-media/<int:id>/delete",
    methods=["POST"],
)
@login_required
def delete_company_media(id):

    media = CompanyMedia.query.get_or_404(id)

    # --------------------------------------
    # Delete physical image
    # --------------------------------------

    if media.file:

        upload_folder = os.path.join(
            "app",
            "static",
            "uploads",
            "company_media",
        )

        file_path = os.path.join(
            upload_folder,
            media.file,
        )

        if os.path.exists(file_path):

            try:
                os.remove(file_path)

            except OSError:
                pass

    # --------------------------------------
    # Delete database record
    # --------------------------------------

    db.session.delete(media)

    db.session.commit()

    flash(
        "Company media deleted successfully.",
        "success",
    )

    return redirect(
        url_for(
            "admin.company_media_list"
        )
    )