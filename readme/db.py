# -*- coding: utf-8 -*-

"""Definition of the database models"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

from readme import conf

Base = declarative_base()
engine = create_engine('sqlite:///' + conf.DB_NAME, encoding='utf-8')
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
