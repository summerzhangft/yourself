from wsgiref.simple_server import make_server
from webob.dec import wsgify
import  webob
from webob import Request, Response

def hello(request: Request) -> Response:
    name = request.params.get("name", 'anonymous')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response

def index(request: Request) -> Response:
    return Response(body = 'hello world',content_type='text/plain')

class Application:
    ROUTER = {}
    @classmethod
    def register(cls,path, handler):
        cls.ROUTER[path] = handler
    def default_handler(self,request: Request) -> Response:
        return Response(body = 'not found',status = 404)
    @wsgify
    def __call__(self, request: Request) -> Response:
        return self.ROUTER.get(request.path, self.default_handler)(request)

if __name__ == '__main__':
    Application.register('/hello',hello)
    Application.register('/',index)

    server = make_server('0.0.0.0', 8000, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

