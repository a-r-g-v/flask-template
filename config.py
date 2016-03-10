import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING = True

class DevelopConfig(Config):
    DEBUG = True

class MasterConfig(Config):
    DEBUG = False


config = {
        "default": MasterConfig,
        "develop": DevelopConfig,
        "testing": TestingConfig,
        "master": MasterConfig,
        "ci": TestingConfig
        }
