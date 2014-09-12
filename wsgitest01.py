#E:/python34/python.exe
from wsgiref.simple_server import make_server
import cgi
html1 = """
<html>
<body>
   <form enctype="multipart/form-data" method="post" action="">
        <p>File:<input type='file' name='file'></p>
        <input type="submit" name="submit" value="upload"/>  
   </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
</body>
</html>"""
html = """
<html>
<body>
   <form method="get" action="">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>"""
def application(environ,start_response):
    d = cgi.parse_qs(environ['QUERY_STRING'])
    print("in application")
    print(environ['QUERY_STRING'])
    age = d.get('age',[''])[0]
    hobbies = d.get('hobbies',[])
    age = cgi.escape(age)
    hobbies = [cgi.escape(hobby) for hobby in hobbies]
    response_body = html % (age or 'Empty',
                    ','.join(hobbies or ['no hobbies'])
                    )
    status = '200 OK'
    response_headers = [('Content-Type','text/html'),
                ('Content-Length',str(len(response_body)))
                ]
    start_response(status,response_headers)
    #response_body = response_body.encode('ascii')
    return [response_body]
    
http = make_server(
    'localhost',
    8051,
    application
    )
http.serve_forever()