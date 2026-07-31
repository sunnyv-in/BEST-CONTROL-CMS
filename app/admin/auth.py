from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app.admin import admin_bp
from app.forms import LoginForm
from app.models import Admin


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():

        admin = Admin.query.filter_by(
            username=form.username.data
        ).first()

        if admin and admin.check_password(form.password.data):
            login_user(
                admin,
                remember=form.remember.data
            )

            flash("Login successful.", "success")

            return redirect(url_for("admin.dashboard"))

        flash("Invalid username or password.", "danger")

    return render_template(
        "admin/auth/login.html",
        form=form
    )


@admin_bp.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("admin.login"))