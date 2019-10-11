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

    # The __call__ method implements WSGI described in PEP-333.
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            body, status = self.routes[path]()
        else:
            status = '404 Not Found'
            body = ''

        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)

        if not isinstance(body, bytes):
            body = body.encode('utf-8')
        return [body]
