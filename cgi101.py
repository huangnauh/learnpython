#!E:/python34/python.exe
import cgi
form = cgi.FieldStorage()  
print("Content-type: text/html\n")
print('<html><body>')
print("<title>Reply Page</title>")
if "username" not in form:  
    print("<h1>Who are you?</h1>")
else:  
    print("<h1>Hello <i>%s</i>!</h1>" % cgi.escape(form['username'].value))
colors = form.getlist('color')
print("The colors list:",colors)
for color in colors:
    print('<p>',cgi.escape(color),'</p>')
print('</body></html>')
