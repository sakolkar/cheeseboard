import models.base as b
import sqlalchemy as sa


class User(b.Model, b.Base):
    __tablename__ = 'user'

    twitch_id = sa.Column(sa.Integer)
    display_name = sa.Column(sa.String())
    logo = sa.Column(sa.String())
