from app import app
from werkzeug.wrappers import Request

def handler(event, context):
    request = Request(event)
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query_string.decode('utf-8'),
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.input': request.body,
        'wsgi.errors': None,
        'wsgi.version': (1, 0),
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    with app.request_context(environ):
        response = app.full_dispatch_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }