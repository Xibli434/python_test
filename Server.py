from http.server import BaseHTTPRequestHandler,HTTPServer
import time
hostName="localhost"
serverPort=8088
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content type","text/html.")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>MyWebsite</title></head>","utf-8"))
        self.wfile.write(bytes("<p>Request: %s<p>"%self.path,"utf-8"))
        self.wfile.write(bytes("<body>","utf-8"))
        self.wfile.write(bytes("<p>This is a very boring sentence.</p>"",""utf-8"))
        self.wfile.write(bytes("</body></html>","utf-8"))

if __name__=="__main__":
    webServer=HTTPServer((hostName,serverPort),Myserver)
    print("Server Started http://%s:%s"%(hostName,serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server Closed")
