import traceback
from flask import Flask
from cheroot.wsgi import Server
from src.routes import routes

app = Flask(__name__)
HOST = '127.0.0.1'  # TODO: change to 0.0.0.0
PORT = 5000

app.register_blueprint(routes)

def start_server():
    """
    Main server init
    """
    server = Server((HOST, PORT), app)
    try:
        server.prepare()
        server.serve()

    except KeyboardInterrupt:
        server.stop()

    except Exception:
        print(traceback)
