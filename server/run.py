from server.src.app import start_server
from server.src.utils.logger import init_logger

if __name__ == '__main__':
    # init logger
    init_logger()

    # start the server
    start_server()
