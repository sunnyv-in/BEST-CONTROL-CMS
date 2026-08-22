from flask import Blueprint, render_template


# Create the website Blueprint
website_bp = Blueprint(
    "website",
    __name__
)


# ==========================================
# Homepage
# ==========================================

@website_bp.route("/")
def home():
    """Homepage"""

    return render_template(
        "website/index.html"
    )


# ==========================================
# About
# ==========================================

@website_bp.route("/about")
def about():
    """About BEST CONTROL"""

    return render_template(
        "website/about.html"
    )