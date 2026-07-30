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

    # Initialize extensions
    db.init_app(app)
    # login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.website.routes import website_bp
    app.register_blueprint(website_bp)

    return app
