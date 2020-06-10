from flask import Blueprint, jsonify, make_response, request, g, abort
from http import HTTPStatus
from models.user import User
from models.clip import Clip
from api.logic import Logic


class Api(Blueprint):
    def __init__(self, logger):
        super().__init__('api', __name__, url_prefix='/api')
        self.add_url_rule('/', None, self.get_root, strict_slashes=False)
        self.add_url_rule('/submit', None, self.post_submit, methods=['POST'], strict_slashes=False)
        self.add_url_rule('/tier1', None, self.get_tier_1, strict_slashes=False)
        self.add_url_rule('/tier2', None, self.get_tier_2, strict_slashes=False)
        self.add_url_rule('/users', None, self.get_users, strict_slashes=False)
        self.logger = logger

    def get_root(self):
        return jsonify({'asdf': 'qwer'})

    def post_submit(self):
        data = request.json
        channel = data['channel_name']

        user = g.db_session.query(User).filter_by(twitch_id=data['user']['twitch_id']).first()
        if user is None:
            user = Logic.load_twitch_user(twitch_id=data['user']['twitch_id'])
            if user is None:
                abort(400, 'Twitch user id bad')
            g.db_session.add(user)
            g.db_session.commit()

        # if only one clip submitted and user's second clip is unset
        # set second clip
        if (
            data['user'][f'slug_1'] and not data['user'][f'slug_2']
            and user.clip_1 is not None and user.clip_2 is None
        ):
            data['user'][f'slug_2'] = data['user'][f'slug_1']
            data['user'][f'slug_1'] = None

        for num in [1, 2]:
            if data['user'][f'slug_{num}'] is None:
                continue
            clip = g.db_session.query(Clip).filter_by(slug=data['user'][f'slug_{num}']).first()
            if clip is None:
                clip = Logic.load_twitch_clip(slug=data['user'][f'slug_{num}'])
                if clip is None:
                    abort(400, 'Clip {num} slug is bad.')
                g.db_session.add(clip)
            setattr(user, f'clip_{num}', clip)
            g.db_session.commit()

        return make_response(jsonify({}), HTTPStatus.CREATED)

    def get_tier_1(self):
        clips = []
        for clip in g.db_session.query(Clip).order_by(Clip.created_at).all():
            if clip.is_tier_1:
                clips.append(clip.as_dict)
        return jsonify(clips)

    def get_tier_2(self):
        clips = []
        for clip in g.db_session.query(Clip).order_by(Clip.created_at).all():
            if clip.is_tier_2:
                clips.append(clip.as_dict)
        return jsonify(clips)

    def get_users(self):
        users = []
        for user in g.db_session.query(User).order_by(User.display_name).all():
            users.append(user.as_dict)
        return jsonify(users)
