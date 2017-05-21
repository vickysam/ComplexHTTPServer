#!/bin/env python

import socketserver
import http.server
import http.server
import sys
import os

# The absolute path of the directoy for this file:
_ROOT = os.path.abspath(os.path.dirname(__file__))

class ThreadingSimpleServer(socketserver.ThreadingMixIn,http.server.HTTPServer):
    pass

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server = ThreadingSimpleServer(('', port), http.server.SimpleHTTPRequestHandler)
print("Serving HTTP on 0.0.0.0 port",port,"...")

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")