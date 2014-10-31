from readme import conf
from readme.db import Base

from sqlalchemy import Column, String, Integer, Text


class Recommendation(Base):

    __tablename__ = conf.DB_TABLE

    id = Column('id', Integer, primary_key=True)  # implicit auto-increment
    book_title = Column('book_title', String(length=200))
    author = Column('author', String(length=200))
    category = Column('category', String(length=100))
    description = Column('description', Text())
