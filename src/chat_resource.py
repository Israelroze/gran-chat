from flask_restful import Resource, request
from logging import getLogger

logger = getLogger('app-log')
_message = list()


class Messages(Resource):
    def get(self):
        logger.info(_message)
        return _message

    def post(self):
        msg = request.get_json()
        logger.info('got message' + str(msg))
        _message.append(msg)
        return 'message added', 201
