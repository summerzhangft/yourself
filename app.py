from wsgiref.simple_server import make_server
import os
from urllib.parse import parse_qs
import webob

def application(environ:dict,  start_response):
    request = webob.Request(environ)
    name = request.params.get("name", 'anonymous')
    response = webob.Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response(environ, start_response)
   # params = parse_qs(environ['QUERY_STRING'])
   # name = params.get('name', ['anonymous'])[0]
   # for k, v in environ.items():
   #     if k not in os.environ.keys():
   #         print('{} => {}'.format(k,v))
    
   # start_response('200 ok',[('Content-Type', 'text/plain')])
   # return ["hello {}".format(name).encode()]

if __name__ == '__main__':
    server = make_server('0.0.0.0',8000, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
