import json
import logging

#from thirdrail import ThirdRail

from functools import wraps
class ThirdRail:
    def __init__(self):
        self.routes = {}

    def consist(self, route):
        @wraps(route)
        def decorated(*args, **kwargs):
            self.routes[route] = args[0]
        return decorated

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


app = ThirdRail()


@app.consist('/ping')
def get_ping():
    return json.dumps({'status': 'ok'}), '200 OK'


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s')
    app.start(port=5050)
