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
            return Clip(
                slug = response.json()['slug'],
                broadcaster = response.json()['broadcaster']['display_name'],
                curator = response.json()['curator']['display_name'],
                game = response.json()['game'],
                title = response.json()['title'],
                views = response.json()['views'],
                duration = response.json()['duration'],
                created_at = response.json()['created_at'],
                thumbnail = response.json()['thumbnails']['medium']
            )

        return None
