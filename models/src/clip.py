import models.base as b
import sqlalchemy as sa
import sqlalchemy.orm as so


class Clip(b.Model, b.Base):
    __tablename__ = 'clip'

    slug = sa.Column(sa.String())
    broadcaster_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    broadcaster = so.relationship('User', foreign_keys=[broadcaster_id])
    curator_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    curator = so.relationship('User', foreign_keys=[curator_id])
    game = sa.Column(sa.String())
    title = sa.Column(sa.String())
    views = sa.Column(sa.Integer)
    duration = sa.Column(sa.Float)
    created_at = sa.Column(sa.DateTime)
    thumbnail = sa.Column(sa.String())
