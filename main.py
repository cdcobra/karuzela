from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from cgi import parse_header, parse_multipart
import html 

class handler(BaseHTTPRequestHandler):
    def header(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = html.htmlHead() + html.htmlCarousel() + html.htmlOptions() 
        self.wfile.write(bytes(message, "utf8"))
    def do_GET(self):
        if self.path == "/default.xlsx":
            self.send_response(200)
            self.send_header('Content-type', 'application/vnd.ms-excel')
            self.end_headers()
            with open("default.xlsx", 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == "/promocje.xlsx":
            self.send_response(200)
            self.send_header('Content-type', 'application/vnd.ms-excel')
            self.end_headers()
            with open("promocje.xlsx", 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.header()
    def do_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")        
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
            with open('promocje.xlsx', 'wb') as output_file:
                output_file.write(postvars['formFile'][0])

        self.header()
        # self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()



        # file_length = int(self.headers['Content-Length'])
        # data = self.rfile.read(file_length)
        
        # self.send_response(201, 'Created')
        # self.end_headers()
        # reply_body = 'Zapisane'
        # self.wfile.write(reply_body.encode('utf-8'))

with HTTPServer(('', 80), handler) as server:
    server.serve_forever()