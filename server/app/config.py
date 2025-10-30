import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Config:
    """Base configuration"""

    # Base paths
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'uploads')
    
    # BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
    # INSTANCE_DIR = os.path.join(BASE_DIR, '..', 'instance')
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'static', 'uploads')

    # Database
    # SQLALCHEMY_DATABASE_URI = os.getenv("postgresql://greenlens_db2_user:coM6K760W43QzIZ1kEVmm7bQctjYa3J8@dpg-d41ek4jipnbc73fanj4g-a.oregon-postgres.render.com/greenlens_db2",
    #     "DATABASE_URI",
    #     'sqlite:///' + os.path.join(INSTANCE_DIR, 'greenlens.db')
    # )
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    _database_url = os.environ.get("DATABASE_URL")
    if _database_url and _database_url.startswith("postgres://"):
        _database_url = _database_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _database_url or f"sqlite:///{os.path.join(INSTANCE_DIR, 'greenlens.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")

    # JWT Configuration
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    # Uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # AI Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4-turbo")
    GPT_TEMPERATURE = float(os.getenv("GPT_TEMPERATURE", "0.7"))
    GPT_MAX_TOKENS = int(os.getenv("GPT_MAX_TOKENS", "500"))

    # CORS Configuration
    FRONTEND_URL = os.getenv("FRONTEND_URL", "https://earthlens-opal.vercel.app/")
    CORS_ORIGINS = [FRONTEND_URL, "https://earthlens-opal.vercel.app/"]

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # App Info
    APP_NAME = "EarthLens API"
    VERSION = "1.0.0"


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    database_url = os.environ.get("DATABASE_URL", f"sqlite:///{os.path.join(Config.INSTANCE_DIR, 'greenlens.db')}")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = database_url
    LOG_LEVEL = "WARNING"


def get_config(config_name):
    """Get configuration class by name"""
    config_map = {
        "production": ProductionConfig,
    }
    return config_map.get(config_name.lower(), Config)
