def method_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello world!\n']


class class_app:

    def __init__(self, environ, start_response):
        self.environ = environ
        print('environ', environ['PATH_INFO'])
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'application/json')]
        self.start(status, response_headers)
        yield b"Hello world!\n"


class CallApp:

    def __call__(self, environ, start_response):
        print('environ', environ['PATH_INFO'])
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b'Hello world!\n']

call_app = CallApp()
