import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/sample"
    PERMANENT_SESSION_LIFETIME = 7200
    SECRET_KEY = "_5#y2LF4Q8znxec]/"
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_NAME='backendCookie'

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}