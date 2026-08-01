from flask import (
    redirect,
    url_for,
    flash,
)

from flask_login import login_required

from app.admin import admin_bp
from app.extensions import db
from app.forms import ProductSpecificationForm
from app.models import (
    Product,
    ProductSpecification,
)

@admin_bp.route(
    "/products/<int:product_id>/specifications/create",
    methods=["POST"],
)
@login_required
def create_specification(product_id):

    product = Product.query.get_or_404(product_id)

    form = ProductSpecificationForm()

    if form.validate_on_submit():

        name = form.specification_name.data

        if name == "Other":

            name = form.custom_name.data.strip()

        specification = ProductSpecification(
            product=product,
            name=name,
            value=form.value.data,
        )

        db.session.add(specification)
        db.session.commit()

        flash(
            "Specification added successfully.",
            "success",
        )

    return redirect(
        url_for(
            "admin.view_product",
            id=product.id,
        )
    )

@admin_bp.route(
    "/product-specifications/<int:specification_id>/delete",
    methods=["POST"],
)
@login_required
def delete_specification(specification_id):

    specification = ProductSpecification.query.get_or_404(
        specification_id
    )

    product_id = specification.product_id

    db.session.delete(specification)
    db.session.commit()

    flash(
        "Specification deleted successfully.",
        "success",
    )

    return redirect(
        url_for(
            "admin.view_product",
            id=product_id,
        )
    )

