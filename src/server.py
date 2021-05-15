from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import pprint
import os

PORT = 8081

def homepage(request):
    _resp = Response()
    _resp.headerlist =  [('Content-type',"text/html; 'charset=UTF-8'")]
    _resp.body = open('src/views/page.html','rb').read()
    return _resp

def traduir(request):
    request.storage.save(request.POST['meme'])

    _resp = Response()
    _resp.headerlist =  [('Content-type',"image/png; 'charset=UTF-8'")]
    _resp.body = open(meme,'rb').read()
    return _resp

settings = {
    'storage.base_path': "/tmp/traduir",
    'storage.extensions': "images+archives",
}

if __name__ == '__main__':
    with Configurator(settings=settings) as config:
        config.include('pyramid_storage')
        config.add_route('home', '/')
        config.add_route('traduir', '/traduir')
        config.add_view(homepage, route_name='home')
        config.add_view(traduir, route_name='traduir')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', PORT, app)
    print("Server listening on port " + str(PORT))
    server.serve_forever()
