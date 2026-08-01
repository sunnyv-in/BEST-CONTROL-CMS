from flask import (
    render_template,
    redirect,
    url_for,
    flash,
)

from flask_login import login_required

from app.admin import admin_bp
from app.extensions import db
from app.forms import SpecificationLibraryForm
from app.models import SpecificationLibrary


@admin_bp.route("/specifications")
@login_required
def specification_list():

    specifications = SpecificationLibrary.query.order_by(
        SpecificationLibrary.group,
        SpecificationLibrary.display_order,
        SpecificationLibrary.name,
    ).all()

    return render_template(
        "admin/specification_library/index.html",
        specifications=specifications,
    )


@admin_bp.route(
    "/specifications/create",
    methods=["GET", "POST"],
)
@login_required
def create_specification_library():

    form = SpecificationLibraryForm()

    if form.validate_on_submit():

        specification = SpecificationLibrary(
            name=form.name.data,
            group=form.group.data,
            data_type=form.data_type.data,
            unit=form.unit.data,
            is_required=form.is_required.data,
            is_filterable=form.is_filterable.data,
            display_order=form.display_order.data,
            is_active=form.is_active.data,
        )

        db.session.add(specification)
        db.session.commit()

        flash(
            "Specification created successfully.",
            "success",
        )

        return redirect(
            url_for("admin.specification_list")
        )

    return render_template(
        "admin/specification_library/create.html",
        form=form,
    )


@admin_bp.route(
    "/specifications/<int:id>/edit",
    methods=["GET", "POST"],
)
@login_required
def edit_specification_library(id):

    specification = SpecificationLibrary.query.get_or_404(id)

    form = SpecificationLibraryForm(obj=specification)

    if form.validate_on_submit():

        form.populate_obj(specification)

        db.session.commit()

        flash(
            "Specification updated successfully.",
            "success",
        )

        return redirect(
            url_for("admin.specification_list")
        )

    return render_template(
        "admin/specification_library/edit.html",
        form=form,
        specification=specification,
    )


@admin_bp.route(
    "/specifications/<int:id>/delete",
    methods=["POST"],
)
@login_required
def delete_specification_library(id):

    specification = SpecificationLibrary.query.get_or_404(id)

    db.session.delete(specification)

    db.session.commit()

    flash(
        "Specification deleted successfully.",
        "success",
    )

    return redirect(
        url_for("admin.specification_list")
    )