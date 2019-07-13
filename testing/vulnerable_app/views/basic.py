"""
Basic, straight forward endpoints for MVP testing.
"""
from flask_restplus import Resource

from ..core.extensions import api
from ..models.basic import session_model
from ..util import get_name


ns = api.namespace(
    get_name(__name__),
    url_prefix='/{}'.format(get_name(__name__)),
)


@ns.route('/')
class NoInputsRequired(Resource):
    @api.marshal_with(session_model.format)
    def get(self):
        return session_model.output()
