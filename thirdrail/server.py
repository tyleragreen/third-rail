import socket
from functools import wraps


class ThirdRail:
    def __init__(self):
        self.routes = {}

    def route(self, route):
        @wraps(route)
        def decorated(*args, **kwargs):
            self.routes[route] = args[0]
        return decorated

    # The __call__ method implements the WSGI application interface
    # described in PEP 333.
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            body, status = self.routes[path]()
        else:
            status, body = '404 Not Found', ''

        response_headers = [('Content-Type', 'application/json')]
        start_response(status, response_headers)

        if not isinstance(body, bytes):
            body = body.encode('utf-8')
        return [body]
