from . import base
from . import clip
from . import user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def db(connection):
    return create_engine(connection)


def session(db):
    return scoped_session(sessionmaker(bind=db, autoflush=False, autocommit=False))

