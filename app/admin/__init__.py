from flask import Blueprint

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

# Import route modules
from app.admin import auth
from app.admin import dashboard
from app.admin import categories
from app.admin import products
from app.admin import gallery
from app.admin import messages
from app.admin import settings