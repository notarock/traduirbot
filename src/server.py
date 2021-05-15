from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

PORT = 8081

def hello_world(request):
    _resp = Response()
    _resp.headerlist =  [('Content-type',"text/html; 'charset=UTF-8'")]
    html = open('src/views/page.html','rb').read()
    _resp.body = html
    return _resp

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', PORT, app)
    print("Server listening on port " + str(PORT))
    server.serve_forever()
