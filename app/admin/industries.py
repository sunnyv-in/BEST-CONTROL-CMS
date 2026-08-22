import os

from flask import (
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import login_required
from slugify import slugify

from app.admin import admin_bp
from app.extensions import db
from app.forms import IndustryForm
from app.models import Industry
from app.utils.file_upload import save_uploaded_file


# ==========================================
# Generate Unique Industry Slug
# ==========================================

def generate_unique_slug(name, current_id=None):

    base_slug = slugify(name)

    if not base_slug:
        base_slug = "industry"

    slug = base_slug
    counter = 2

    while True:

        query = Industry.query.filter_by(
            slug=slug
        )

        if current_id is not None:
            query = query.filter(
                Industry.id != current_id
            )

        existing = query.first()

        if not existing:
            return slug

        slug = f"{base_slug}-{counter}"
        counter += 1


# ==========================================
# Industry List
# ==========================================

@admin_bp.route("/industries")
@login_required
def industry_list():

    industries = (
        Industry.query
        .order_by(
            Industry.display_order,
            Industry.name,
        )
        .all()
    )

    return render_template(
        "admin/industries/index.html",
        industries=industries,
    )


# ==========================================
# Create Industry
# ==========================================

@admin_bp.route(
    "/industries/create",
    methods=["GET", "POST"],
)
@login_required
def create_industry():

    form = IndustryForm()

    if form.validate_on_submit():

        # ------------------------------------------
        # Check duplicate industry name
        # ------------------------------------------

        existing_name = Industry.query.filter_by(
            name=form.name.data
        ).first()

        if existing_name:

            flash(
                "An industry with this name already exists.",
                "warning",
            )

            return render_template(
                "admin/industries/create.html",
                form=form,
            )

        # ------------------------------------------
        # Generate unique slug automatically
        # ------------------------------------------

        slug = generate_unique_slug(
            form.name.data
        )

        # ------------------------------------------
        # Save uploaded image
        # ------------------------------------------

        image_filename = None

        if form.image.data:

            image_filename = save_uploaded_file(
                form.image.data,
                "industries",
            )

        # ------------------------------------------
        # Create Industry
        # ------------------------------------------

        industry = Industry(
            name=form.name.data,
            slug=slug,
            description=form.description.data,
            image=image_filename,
            display_order=form.display_order.data or 0,
            is_active=form.is_active.data,
            meta_title=form.meta_title.data,
            meta_description=form.meta_description.data,
        )

        db.session.add(industry)
        db.session.commit()

        flash(
            "Industry created successfully.",
            "success",
        )

        return redirect(
            url_for("admin.industry_list")
        )

    return render_template(
        "admin/industries/create.html",
        form=form,
    )


# ==========================================
# Edit Industry
# ==========================================

@admin_bp.route(
    "/industries/<int:id>/edit",
    methods=["GET", "POST"],
)
@login_required
def edit_industry(id):

    industry = Industry.query.get_or_404(id)

    # IMPORTANT:
    # Do not use IndustryForm(obj=industry)
    # because image is a FileField and the database
    # contains a filename string.
    form = IndustryForm()

    # ==========================================
    # Load Existing Data on GET
    # ==========================================

    if request.method == "GET":

        form.name.data = industry.name
        form.description.data = industry.description
        form.display_order.data = industry.display_order
        form.is_active.data = industry.is_active
        form.meta_title.data = industry.meta_title
        form.meta_description.data = industry.meta_description

    # ==========================================
    # Process Form
    # ==========================================

    if form.validate_on_submit():

        # ------------------------------------------
        # Check duplicate industry name
        # ------------------------------------------

        existing_name = (
            Industry.query
            .filter(
                Industry.name == form.name.data,
                Industry.id != industry.id,
            )
            .first()
        )

        if existing_name:

            flash(
                "An industry with this name already exists.",
                "warning",
            )

            return render_template(
                "admin/industries/edit.html",
                form=form,
                industry=industry,
            )

        # ------------------------------------------
        # Update Name
        # ------------------------------------------

        industry.name = form.name.data

        # ------------------------------------------
        # Automatically Generate Slug
        # ------------------------------------------

        industry.slug = generate_unique_slug(
            form.name.data,
            current_id=industry.id,
        )

        # ------------------------------------------
        # Update Description
        # ------------------------------------------

        industry.description = (
            form.description.data
        )

        # ------------------------------------------
        # Replace Image Only If New Image Uploaded
        # ------------------------------------------

        if form.image.data:

            old_image = industry.image

            # Save new image first
            new_image = save_uploaded_file(
                form.image.data,
                "industries",
            )

            # Update database value
            industry.image = new_image

            # --------------------------------------
            # Delete Old Image
            # --------------------------------------

            if old_image:

                old_image_path = os.path.join(
                    current_app.root_path,
                    "static",
                    "uploads",
                    "industries",
                    old_image,
                )

                if os.path.isfile(old_image_path):

                    os.remove(old_image_path)

        # ------------------------------------------
        # Update Display Order
        # ------------------------------------------

        industry.display_order = (
            form.display_order.data or 0
        )

        # ------------------------------------------
        # Update Active Status
        # ------------------------------------------

        industry.is_active = (
            form.is_active.data
        )

        # ------------------------------------------
        # Update SEO
        # ------------------------------------------

        industry.meta_title = (
            form.meta_title.data
        )

        industry.meta_description = (
            form.meta_description.data
        )

        # ------------------------------------------
        # Save Changes
        # ------------------------------------------

        db.session.commit()

        flash(
            "Industry updated successfully.",
            "success",
        )

        return redirect(
            url_for("admin.industry_list")
        )

    return render_template(
        "admin/industries/edit.html",
        form=form,
        industry=industry,
    )


# ==========================================
# Delete Industry
# ==========================================

@admin_bp.route(
    "/industries/<int:id>/delete",
    methods=["POST"],
)
@login_required
def delete_industry(id):

    industry = Industry.query.get_or_404(id)

    # ------------------------------------------
    # Delete Associated Image
    # ------------------------------------------

    if industry.image:

        image_path = os.path.join(
            current_app.root_path,
            "static",
            "uploads",
            "industries",
            industry.image,
        )

        if os.path.isfile(image_path):

            os.remove(image_path)

    # ------------------------------------------
    # Delete Database Record
    # ------------------------------------------

    db.session.delete(industry)
    db.session.commit()

    flash(
        "Industry deleted successfully.",
        "success",
    )

    return redirect(
        url_for("admin.industry_list")
    )