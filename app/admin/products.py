from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from flask_login import login_required

from app.admin import admin_bp
from app.extensions import db

from app.forms import ProductForm

from app.models import (
    Product,
    Category,
    DocumentLibrary,
    ProductSpecification,
    ProductDocument,
    ProductImage,
)

from app.services.product_service import (
    create_product as create_product_service,  update_product,
)

from app.services.specification_service import (
    get_active_specifications,
)


# ==========================================
# Product List
# ==========================================

@admin_bp.route("/products")
@login_required
def product_list():

    products = Product.query.order_by(
        Product.name
    ).all()

    return render_template(
        "admin/products/index.html",
        products=products,
    )


# ==========================================
# New Product
# ==========================================

@admin_bp.route("/products/new", methods=["GET"])
@login_required
def new_product():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    specifications = get_active_specifications()

    documents = DocumentLibrary.query.order_by(
        DocumentLibrary.display_order
    ).all()

    return render_template(
        "admin/products/editor.html",
        form=form,
        specifications=specifications,
        documents=documents,
    )


# ==========================================
# Create Product
# ==========================================

@admin_bp.route("/products/create", methods=["POST"])
@login_required
def create_product():

    form = ProductForm()

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    specifications = get_active_specifications()

    documents = DocumentLibrary.query.order_by(
        DocumentLibrary.display_order
    ).all()

    if not form.validate_on_submit():

        flash(
            "Please correct the errors in the form.",
            "danger",
        )

        return render_template(
            "admin/products/editor.html",
            form=form,
            specifications=specifications,
            documents=documents,
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

# ==========================================
# Edit Product
# ==========================================

@admin_bp.route("/products/<int:id>/edit", methods=["GET"])
@login_required
def edit_product(id):

    product = Product.query.get_or_404(id)

    form = ProductForm(obj=product)

    form.category_id.choices = [
        (category.id, category.name)
        for category in Category.query.order_by(Category.name)
    ]

    specifications = get_active_specifications()

    documents = DocumentLibrary.query.order_by(
        DocumentLibrary.display_order
    ).all()

    return render_template(
        "admin/products/editor.html",
        form=form,
        product=product,
        specifications=specifications,
        documents=documents,
        edit_mode=True,
    )

@admin_bp.route(
    "/products/<int:id>/update",
    methods=["POST"],
)
@login_required
def update_product_route(id):

    product = Product.query.get_or_404(id)

    form = ProductForm()

    form.category_id.choices = [
        (c.id, c.name)
        for c in Category.query.order_by(Category.name)
    ]

    if not form.validate_on_submit():

        flash(
            "Please correct the errors.",
            "danger",
        )

        specifications = get_active_specifications()

        documents = DocumentLibrary.query.order_by(
            DocumentLibrary.display_order
        ).all()

        return render_template(
            "admin/products/editor.html",
            form=form,
            product=product,
            specifications=specifications,
            documents=documents,
            edit_mode=True,
        )

    update_product(
        product,
        form,
        request,
    )

    flash(
        "Product updated successfully.",
        "success",
    )

    return redirect(
        url_for("admin.product_list")
    )


# ==========================================
# Delete Product
# ==========================================

@admin_bp.route("/products/<int:id>/delete", methods=["POST"])
@login_required
def delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)

    db.session.commit()

    flash(
        "Product deleted successfully.",
        "success",
    )

    return redirect(
        url_for("admin.product_list")
    )

# =====================================================
# Product Gallery
# =====================================================

@admin_bp.route("/gallery")
@login_required
def gallery():

    products = (
        Product.query
        .join(ProductImage)
        .distinct()
        .order_by(Product.name)
        .all()
    )

    return render_template(
        "admin/gallery/index.html",
        products=products,
    )