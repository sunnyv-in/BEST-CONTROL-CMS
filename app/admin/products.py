from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    current_app,
)

from app.forms import (
    ProductForm,
    ProductSpecificationForm,
)

from flask_login import login_required

from app.admin import admin_bp
from app.extensions import db
from app.models import (
    Product,
    Category,
    ProductSpecification,
)

from app.utils.file_upload import save_uploaded_file

@admin_bp.route("/products")
@login_required
def product_list():

    products = Product.query.order_by(Product.name).all()

    return render_template(
        "admin/products/index.html",
        products=products,
    )

@admin_bp.route("/products/editor", methods=["GET"])
@login_required
def product_editor():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    return render_template(
        "admin/products/editor.html",
        form=form,
    )


@admin_bp.route("/products/<int:id>")
@login_required
def view_product(id):

    product = Product.query.get_or_404(id)

    specification_form = ProductSpecificationForm()

    return render_template(
        "admin/products/view.html",
        product=product,
        specification_form=specification_form,
    )


@admin_bp.route("/products/create", methods=["GET", "POST"])
@login_required
def create_product():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    if form.validate_on_submit():

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
        )

        db.session.add(product)
        db.session.commit()

        flash("Product created successfully.", "success")

        return redirect(url_for("admin.product_list"))

    return render_template(
        "admin/products/create.html",
        form=form,
    )

@admin_bp.route("/products/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_product(id):

    product = Product.query.get_or_404(id)

    form = ProductForm(obj=product)

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    if form.validate_on_submit():

        product.category_id = form.category_id.data
        product.name = form.name.data
        product.slug = form.slug.data
        product.model_number = form.model_number.data
        product.short_description = form.short_description.data
        product.description = form.description.data
        product.featured = form.featured.data
        product.published = form.published.data

        db.session.commit()

        flash("Product updated successfully.", "success")

        return redirect(url_for("admin.product_list"))

    return render_template(
        "admin/products/edit.html",
        form=form,
        product=product,
    )

@admin_bp.route("/products/<int:id>/delete", methods=["POST"])
@login_required
def delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    flash("Product deleted successfully.", "success")

    return redirect(url_for("admin.product_list"))

