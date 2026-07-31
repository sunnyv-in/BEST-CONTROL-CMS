from flask import Flask

from config import Config
from app.extensions import db, login_manager, migrate


def create_app():
    """
    Application Factory
    Creates and Configures the Flask Application
    """

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "admin.login"
    login_manager.login_message_category = "warning"

    migrate.init_app(app, db)

    # Import models (required for Flask-Migrate)
    from app import models

    # Register Flask-Login user loader
    

    # Register Blueprints
    from app.website.routes import website_bp
    from app.admin import admin_bp

    app.register_blueprint(website_bp)
    app.register_blueprint(admin_bp)

    return app