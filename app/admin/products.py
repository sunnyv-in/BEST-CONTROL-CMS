from flask import (
    render_template,
    redirect,
    url_for,
    flash,
)
from app.services.product_service import create_product as create_product_service
from flask_login import login_required

from app.admin import admin_bp
from app.extensions import db

from app.forms import ProductForm

from app.models import (
    Product,
    Category,
)

from app.models import (
    Product,
    Category,
    ProductSpecification,
    SpecificationLibrary,
)

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from app.utils.file_upload import save_uploaded_file

from app.services.specification_service import (
    get_active_specifications,
)

@admin_bp.route("/products")
@login_required
def product_list():

    products = Product.query.order_by(Product.name).all()

    return render_template(
        "admin/products/index.html",
        products=products,
    )
@admin_bp.route("/products/new", methods=["GET"])
@login_required
def new_product():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    specifications = get_active_specifications()

    return render_template(
    "admin/products/editor.html",
    form=form,
    specifications=specifications,
)

@admin_bp.route("/products/create", methods=["POST"])
@login_required
def create_product():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    if not form.validate_on_submit():

        flash(
            "Please correct the errors in the form.",
            "danger",
        )

        return render_template(
            "admin/products/editor.html",
            form=form,
        )

    create_product_service(
    form,
    request,
    )

    flash(
        "Product created successfully.",
        "success",
    )

    return redirect(
        url_for("admin.product_list")
    )


@admin_bp.route("/products/<int:id>/delete", methods=["POST"])
@login_required
def delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    flash("Product deleted successfully.", "success")

    return redirect(url_for("admin.product_list"))

