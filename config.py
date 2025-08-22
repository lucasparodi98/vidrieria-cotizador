import os
from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'dF4LVhK)60^p'


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = os.path.join(BASE_DIR, "instance", "vidrieria.sqlite")

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
