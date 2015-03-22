import os

class DevelopmentConfig(object):
	DATABASE_URI = "postgresql://localhost:5432/git_text"
	DEBUG = True
	#SECRET_KEY = os.environ.get("SECRET_KEY", "")

class TestingConfig(object):
    DATABASE_URI = "postgresql://localhost:5432/git_text_test"
    DEBUG = True
    TESTING = True