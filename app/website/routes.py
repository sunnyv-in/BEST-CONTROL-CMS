from flask import Blueprint, render_template

# Create the website Blueprint
website_bp = Blueprint(
    "website",
    __name__
)

@website_bp.route("/")
def home():
    """Homepage"""

    return render_template("website/index.html")