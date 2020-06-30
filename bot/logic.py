import re
import requests
from http import HTTPStatus
import os
import random


class Logic:

    @staticmethod
    def randchar():
        return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


    @staticmethod
    def randstr(length=4):
        return ''.join([Logic.randchar() for _ in range(length)])


    @staticmethod
    def get_slug(clip_string):
        match = re.match(r"^https:\/\/www.twitch.tv\/(?P<channel>.*)\/clip\/(?P<slug>[a-zA-Z0-9]*)", clip_string)
        if match:
            return match.group('slug')

        match = re.match(r"^https:\/\/clips.twitch.tv\/(?P<slug>[a-zA-Z0-9]*)", clip_string)
        if match:
            return match.group('slug')

        match = re.match(r"^(?P<slug>[a-zA-Z0-9]*)", clip_string)
        if match:
            return match.group('slug')

        return None


    @staticmethod
    def check_slug(slug):
        if slug is None:
            return False

        response = requests.get(
            f'https://api.twitch.tv/kraken/clips/{slug}',
            headers={
                'Client-Id': os.environ['TWITCH_CLIENT_ID'],
                'Accept': 'application/vnd.twitchtv.v5+json'
            })

        if response.status_code == HTTPStatus.OK:
            return True
        return False


    @staticmethod
    def submit_to_api(data, logger):
        try:
            response = requests.post(
                f'{os.environ["API_URL"]}/submit',
                json=data
            )
        except:
            logger.exception('API Submission failed.', exc_info=True)
            return False
        if response.status_code == HTTPStatus.CREATED:
            return True
        return False


    @staticmethod
    def submission(message, logger):
        parts = message.content.split(' ')
        if len(parts) >= 1:
            command = parts[0]
            t1_slug = None
            t2_slug = None
        if len(parts) >= 2:
            t1_slug = Logic.get_slug(parts[1])
        if len(parts) == 3:
            t2_slug = Logic.get_slug(parts[2])
        if len(parts) > 3:
            logger.warning('Too many parts in the submission')
            return False

        if not Logic.check_slug(t1_slug) or (t2_slug and not Logic.check_slug(t2_slug)):
            return False

        data = dict(
            channel_name = message.channel.name,
            user = dict(
                twitch_id = message.author.id,
                display_name = message.author.tags['display-name'],
                slug_1 = t1_slug,
                slug_2 = t2_slug,
            ),
        )
        return Logic.submit_to_api(data, logger)
