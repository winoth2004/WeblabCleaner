from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        
    def do_POST(self):
       self._set_headers()
       data = json.loads("{\"crURL\": \"http:\/\/www.amazon.in\/\"}");                                                                                                                                                  
       response = json.dumps(data)
       self.wfile.write(response)
       print 'everything ok'
       return
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
