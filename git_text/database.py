from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
fom sqlalchemy.ext.decalrative import declarative_base

from git_text import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
sesion = Session()