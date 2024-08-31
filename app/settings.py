""" Application Settings Module
"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string(asyncMode: bool = False) -> str:
    """Get the connection string for the database

    Returns:
        string: The connection string
    """
    engine = os.environ.get("DB_ENGINE")
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT", 5432)
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    name = os.environ.get("DB_NAME")
    connection_string = f"{engine}://{username}:{password}@{host}:{port}/{name}"
    return connection_string

# Database Setting
SQLALCHEMY_DATABASE_URL = get_connection_string()
SQLALCHEMY_DATABASE_URL_ASYNC = get_connection_string(asyncMode=True)

ADMIN_DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")

# JWT Setting
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")