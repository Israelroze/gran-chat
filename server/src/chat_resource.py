from flask_restful import Resource, request
from logging import getLogger

logger = getLogger('app-log')
_message = list()


class Messages(Resource):
    def get(self):
        logger.info(_message)
        return _message

    def post(self):
        msg = request.json

        logger.info('got message' + str(msg))

        # check if username provided
        if 'username' in msg and msg['username'] != "":
            _message.append(request.json)
            return 'message added', 201
        else:
            return 'username required', 400

