#!E:/python34/python.exe
import http.server
httpd = http.server.HTTPServer(('127.0.0.1',8888),http.server.CGIHTTPRequestHandler)
sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    httpd.server_close()
    sys.exit(0)