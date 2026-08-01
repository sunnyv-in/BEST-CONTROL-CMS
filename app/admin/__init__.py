from flask import Blueprint

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

# Import existing route modules
from app.admin import auth
from app.admin import dashboard
from app.admin import categories
from app.admin import products
from app.admin import product_specifications
from app.admin import specification_library