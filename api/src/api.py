from flask import Blueprint, jsonify


class Api(Blueprint):
    def __init__(self):
        super().__init__('api', __name__, url_prefix='/api')
        self.add_url_rule('/', None, self.get_root, strict_slashes=False)

    def get_root(self):
        return jsonify({'asdf': 'qwer'})
