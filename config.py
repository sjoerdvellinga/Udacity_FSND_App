import os


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
    AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")
    AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
    API_AUDIENCE = os.environ.get("API_AUDIENCE")
    ALGORITHMS = os.environ.get("ALGORITHMS")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # to-do: add other production-specific configuration options


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_TEST")
    TESTING = True
    # to-do: ther testing-specific configuration options
