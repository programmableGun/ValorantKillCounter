#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from motorTest import ShootGun, SpinMotor
import logging
stop = True         # set to false when  done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write('<html><head>    <title>CatTreatDispenser</title>      <script>var buttonCounter = 0;function httpGet(theUrl){var xmlHttp = new XMLHttpRequest();xmlHttp.open( "POST", theUrl);xmlHttp.send("death");console.log(xmlHttp.responseText);}function myFunction(){buttonCounter++;document.getElementById("counter1").style.visibility = "visible";document.getElementById("counter1").textContent = "You have triggered the cat "+ buttonCounter + " times!";httpGet("192.168.0.39:42069");document.getElementById("audio").play();}</script></head><body><h1>Snipers Cat Treat Dispensor</h1><h2></h2><button type="button" onclick="myFunction();" id="counter1" >Dispense Treats</button></body></html>'.encode('utf-8'))
       #SpinMotor(0.001,-150)
       #SpinMotor(0.001,500) #will run twice for some reason
       #ShootGun(1);
        

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        if(post_data.decode('utf-8') == "death"):
            ShootGun(1);
        elif(post_data.decode('utf-8') == "stop"):
            stop = True
            logging.info('Stopping httpd...\n')
        else:
            print(post_data.decode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=42069):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    ShootGun(1)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt or stop:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


