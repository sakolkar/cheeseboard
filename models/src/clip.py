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

    @property
    def is_tier_1(self):
        if any(self.users_tier_1):
            return True
        return False

    @property
    def is_tier_2(self):
        if not any(self.users_tier_1) and any(self.users_tier_2):
            return True
        return False

    @property
    def as_dict(self):
        return {
            'slug': self.slug,
            'broadcaster': self.broadcaster.display_name,
            'curator': self.curator.display_name,
            'game': self.game,
            'title': self.title,
            'views': self.views,
            'duration': self.duration,
            'created_at': self.created_at.timestamp(),
            'thumbnail': self.thumbnail
        }
