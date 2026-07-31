from flask import render_template
from flask_login import login_required

from app.admin import admin_bp
from app.models import Category, Product


@admin_bp.route("/")
@login_required
def dashboard():

    stats = {
        "products": Product.query.count(),
        "categories": Category.query.count(),
        "gallery": 0,
        "messages": 0,
    }

    return render_template(
        "admin/dashboard/index.html",
        stats=stats,
    )