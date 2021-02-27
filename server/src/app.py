import traceback
from flask import Flask
from cheroot.wsgi import Server
from server.src.routes import routes
from logging import getLogger
from flask_restful import Api
from server.src.chat_resource import Messages

app = Flask(__name__)


HOST = '127.0.0.1'  # TODO: change to 0.0.0.0
PORT = 5000

app.register_blueprint(routes)
api = Api(app)
api.add_resource(Messages, '/chat')

logger = getLogger('app-log')
def start_server():
    """
    Main server init
    """
    server = Server((HOST, PORT), app)
    try:
        server.prepare()
        server.serve()

    except KeyboardInterrupt:
        logger.info('server stopping')
        server.stop()

    except Exception:
        logger.critical(traceback.print_stack())