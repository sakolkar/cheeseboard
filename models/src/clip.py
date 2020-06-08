import models.base as b
import sqlalchemy as sa


class Clip(b.Model, b.Base):
    __tablename__ = 'clip'

    slug = sa.Column(sa.String())
