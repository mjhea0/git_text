import os

SECRET_KEY = "change me!"
ADDRESS = os.environ["address"]
PASSWORD = os.environ["password"]
PHONE_NUMBER = os.environ["phone_number"]
USER_NAME = "kyle8285"


class BaseConfig(object):
    DEBUG = False


class DevelopmentConfig(object):
    DEBUG = True


class TestingConfig(object):
    DEBUG = False
    TESTING = True
