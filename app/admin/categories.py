from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.extensions import db
from app.admin import admin_bp
from app.forms import CategoryForm
from app.models import Category
from flask import request


@admin_bp.route("/categories")
@login_required
def category_list():

    categories = Category.query.order_by(Category.name).all()

    return render_template(
        "admin/categories/index.html",
        categories=categories,
    )

@admin_bp.route("/categories/create", methods=["GET", "POST"])
@login_required
def create_category():

    form = CategoryForm()

    if form.validate_on_submit():

        existing_name = Category.query.filter_by(
            name=form.name.data
        ).first()

        if existing_name:
            flash(
                "A category with this name already exists.",
                "warning"
            )
            return render_template(
                "admin/categories/create.html",
                form=form
            )


        existing_slug = Category.query.filter_by(
            slug=form.slug.data
        ).first()

        if existing_slug:
            flash(
                "This slug already exists.",
                "warning"
            )
            return render_template(
                "admin/categories/create.html",
                form=form
            )


        category = Category(
            name=form.name.data,
            slug=form.slug.data,
            description=form.description.data,
            is_active=form.is_active.data,
        )

        db.session.add(category)
        db.session.commit()

        flash("Category created successfully.", "success")

        return redirect(url_for("admin.category_list"))

    return render_template(
        "admin/categories/create.html",
        form=form,
    )

@admin_bp.route("/categories/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_category(id):

    category = Category.query.get_or_404(id)

    form = CategoryForm(obj=category)
    print("Form Name:", form.name.data)
    print("Form Slug:", form.slug.data)
    print("Form Description:", form.description.data)

    if form.validate_on_submit():

        category.name = form.name.data
        category.slug = form.slug.data
        category.description = form.description.data
        category.is_active = form.is_active.data

        db.session.commit()

        flash("Category updated successfully.", "success")

        return redirect(url_for("admin.category_list"))

    return render_template(
        "admin/categories/edit.html",
        form=form,
        category=category,
    )

@admin_bp.route("/categories/<int:id>/delete", methods=["POST"])
@login_required
def delete_category(id):

    category = Category.query.get_or_404(id)

    if category.products:

        flash(
            "Cannot delete a category that contains products.",
            "danger"
        )

        return redirect(
            url_for("admin.category_list")
        )

    db.session.delete(category)
    db.session.commit()

    flash(
        "Category deleted successfully.",
        "success"
    )

    return redirect(
        url_for("admin.category_list")
    )