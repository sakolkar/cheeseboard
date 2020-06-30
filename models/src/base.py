import sqlalchemy as sa
import sqlalchemy.ext.declarative as se


Base = se.declarative_base()


class Model:
    id = sa.Column(sa.Integer, primary_key=True)

