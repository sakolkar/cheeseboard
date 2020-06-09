from flask import g
from models.user import User
from models.clip import Clip
import requests
from http import HTTPStatus
import re
import os


class Logic:

    @staticmethod
    def new_user(id=None, _id=None, display_name=None, logo=None, **kwargs):
        return User(
            twitch_id = id if id is not None else _id,
            display_name = display_name,
            logo = logo,
        )

    @staticmethod
    def load_twitch_user(twitch_id=None, **kwargs):
        try:
            t = int(twitch_id)
        except ValueError:
            return None

        response = requests.get(
            f'https://api.twitch.tv/kraken/users/{twitch_id}',
            headers={
                'Client-Id': os.environ['TWITCH_CLIENT_ID'],
                'Accept': 'application/vnd.twitchtv.v5+json'
            })

        if response.status_code == HTTPStatus.OK:
            return Logic.new_user(**response.json())
        return None

    @staticmethod
    def load_twitch_clip(slug=None, **kwargs):
        if not re.match(r"^[a-zA-Z0-9]*$", slug):
            return None

        response = requests.get(
            f'https://api.twitch.tv/kraken/clips/{slug}',
            headers={
                'Client-Id': os.environ['TWITCH_CLIENT_ID'],
                'Accept': 'application/vnd.twitchtv.v5+json'
            })

        if response.status_code == HTTPStatus.OK:
            broadcaster = g.db_session.query(User).filter_by(twitch_id=response.json()['broadcaster']['id']).first()
            if broadcaster is None:
                broadcaster = Logic.new_user(**response.json()['broadcaster'])
                g.db_session.add(broadcaster)

            curator = g.db_session.query(User).filter_by(twitch_id=response.json()['curator']['id']).first()
            if curator is None:
                curator = Logic.new_user(**response.json()['curator'])
                g.db_session.add(curator)

            return Clip(
                slug = response.json()['slug'],
                broadcaster = broadcaster,
                curator = curator,
                game = response.json()['game'],
                title = response.json()['title'],
                views = response.json()['views'],
                duration = response.json()['duration'],
                created_at = response.json()['created_at'],
                thumbnail = response.json()['thumbnails']['medium']
            )

        return None
