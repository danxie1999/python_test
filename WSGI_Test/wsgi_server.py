from wsgiref.simple_server import make_server
from wsgi_test import application

httpd=make_server('',9000,application)
print('Start HTTP on port 9000...')
httpd.serve_forever()