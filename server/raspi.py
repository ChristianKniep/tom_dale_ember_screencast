import os, thread, md5
import restlite
from pprint import pprint
import json
import datetime
import re


pin_list = [
    {
        'id': 1,
        'pin_nr': "1",
        'name': "TestPin1",
        'changedAt': json.dumps(datetime.datetime.now().isoformat()),
        'status': '0',
    },
       {
        'id': 2,
        'pin_nr': "2",
        'name': "TestPin2",
        'changedAt': json.dumps(datetime.datetime.now().isoformat()),
        'status': '0',
    },
]

pin_json = {
  "pin": {
    'id': 1,
    'pin_nr': "1",
    'name': "TestPin1",
    'changedAt': json.dumps(datetime.datetime.now().isoformat()),
    'status': '0',
  }
}
# The resource to list all the file information under path relative to the top-level directory

@restlite.resource
def pins():
    def GET(request):
        mat = re.match('/(\d+)', request['PATH_INFO'])
        if mat:
            print mat.group(1)
            return request.response(pin_json)
        return request.response({'pins': pin_list})
    return locals()

# download a given file from the path under top-level directory

def pin(env, start_response):
    print env, start_response
    return [result]


# all the routes

routes = [
    (r'GET,PUT,POST /(?P<type>((xml)|(plain)))/(?P<path>.*)', 'GET,PUT,POST /%(path)s', 'ACCEPT=text/%(type)s'),
    (r'GET,PUT,POST /(?P<type>((json)))/(?P<path>.*)', 'GET,PUT,POST /%(path)s', 'ACCEPT=application/%(type)s'),
    (r'GET /pins', pins),
    (r'GET /pin', pin),
]        

# launch the server on port 8000
    
if __name__ == '__main__':
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8082, restlite.router(routes))
    
    try: httpd.serve_forever()
    except KeyboardInterrupt: pass
