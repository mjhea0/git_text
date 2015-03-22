import os.path

from flask import url_for
from sqlalchemy import Column, Integer, String, DateTime

from git_text import app
from database import Base, engine, session

class Commit(Base):
	__tablename__ = "commits"

	id = Column(Integer, primary_key=True)
	date = Column(DateTime)

	def as_dictionary(self):
		return {
			"id": self.id,
			"date": self.date
		}

