from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from base import Base

class User(Base):
	__tablename__ = "user"

	id = Column("id", Integer, primary_key=True)
	first_name = Column("first_name", String, unique=True)
	last_name = Column("last_name", String, unique=True)

	def __init__(self, user):
		self.id = user["id"]
		self.first_name = user["first_name"]
		self.last_name = user["last_name"]