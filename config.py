import os
from dotenv import load_dotenv

# Load enviromental variables from the .env file

load_dotenv()

class Config:
    """ Base configuration for the BEST CONTRIL CMS """

    # Secret key used for sessions and security 
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
    
    # SQLite database 
    SQLALCHEMY_DATABASE_URI = "sqlite:///bestcontrol.db"

    # Disable modification tracking to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False