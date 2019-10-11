import socket
import logging
from functools import wraps


logger = logging.getLogger(__name__)


class ThirdRail:
    def __init__(self):
        self.routes = {}

    def consist(self, route):
        @wraps(route)
        def decorated(*args, **kwargs):
            self.routes[route] = args[0]
        return decorated

    def start(self, port):
        logger.info(f'Listening on port {port}...')
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), port))
        serversocket.listen(5)
