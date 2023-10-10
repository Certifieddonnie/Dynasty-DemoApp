"""
Configuration File
"""
import os
from datetime import timedelta

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


class Config(object):
    """App config object"""

    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv("ACCESS_TOKEN_EXPIRES")
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = False


class ProductionConfig(Config):
    """Production Config Object"""

    DATABASE_URI = os.getenv("DB_URI")


class DevelopmentConfig(Config):
    """Development Config Object"""

    sql_lite = "sqlite:///development.db"
    DATABASE_URI = os.getenv("DB_URI", default=sql_lite)


class TestConfig(Config):
    """Testing Config Object"""

    sql_lite = "sqlite:///test.db"
    DATABASE_URI = sql_lite


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestConfig,
}
