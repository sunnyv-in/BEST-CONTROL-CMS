import os
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.admin import admin_bp
from app.extensions import db
from app.forms import CertificateForm
from app.models import Certificate
from app.utils.file_upload import save_uploaded_file

@admin_bp.route("/certificates")
@login_required
def certificate_list():

    certificates = Certificate.query.order_by(Certificate.display_order, Certificate.name).all()

    return render_template(
        "admin/certificates/index.html",
        certificates=certificates,
    )