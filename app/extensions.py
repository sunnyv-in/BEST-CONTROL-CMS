from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Database Instance
db = SQLAlchemy()

# Login manager instance
login_manager = LoginManager()

# Database migration instance
migrate = Migrate()