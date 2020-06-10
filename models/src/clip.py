import models.base as b
import sqlalchemy as sa


class Clip(b.Model, b.Base):
    __tablename__ = 'clip'

    slug = sa.Column(sa.String())
    broadcaster = sa.Column(sa.String())
    curator = sa.Column(sa.String())
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
            'broadcaster': self.broadcaster,
            'curator': self.curator,
            'game': self.game,
            'title': self.title,
            'views': self.views,
            'duration': self.duration,
            'created_at': self.created_at.timestamp(),
            'thumbnail': self.thumbnail,
            'users': [ u.display_name for u in self.users_tier_1 ] + \
                     [ u.display_name for u in self.users_tier_2 ],
        }
