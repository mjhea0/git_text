import os

class DevelopmentConfig(object):
	#DATABASE_URI = "postgresql://localhost/git_text"
	DEBUG = True
	#SECRET_KEY = os.environ.get("SECRET_KEY", "")

class TestingConfig(object):
    #DATABASE_URI = "sqlite://"
    DEBUG = True
    TESTING = True