from readme import conf
from readme.db import Base

from sqlalchemy import Column, String, Integer, Text


class Recommendation(Base):

    __tablename__ = conf.DB_TABLE

    id = Column('id', Integer, primary_key=True)  # implicit auto-increment
    book_name = Column('book_name', String(length=100))
    author = Column('author', String(length=100))
    category = Column('category', String(length=100))
    description = Column('description', Text())
