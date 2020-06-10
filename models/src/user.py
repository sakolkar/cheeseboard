import models.base as b
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(b.Model, b.Base):
    __tablename__ = 'user'

    twitch_id = sa.Column(sa.Integer)
    display_name = sa.Column(sa.String())
    logo = sa.Column(sa.String())
    clip_1_id = sa.Column(sa.Integer, sa.ForeignKey('clip.id'))
    clip_1 = so.relationship('Clip', foreign_keys=[clip_1_id], backref='users_tier_1')
    clip_2_id = sa.Column(sa.Integer, sa.ForeignKey('clip.id'))
    clip_2 = so.relationship('Clip', foreign_keys=[clip_2_id], backref='users_tier_2')

    @property
    def as_dict(self):
        return {
            'twitch_id': self.twitch_id,
            'display_name': self.display_name,
            'logo': self.logo,
        }
