import lxml.html

form_string='''<html><body><form>
   Your name: <input type="text" name="name"> <br>
   Your phone: <input type="text" name="phone"> <br>
   Your favorite pets: <br>
   Dogs: <input type="checkbox" name="interest" value="dogs"> <br>
   Cats: <input type="checkbox" name="interest" value="cats"> <br>
   Llamas: <input type="checkbox" name="interest" value="llamas"> <br>
   <input type="submit"></form></body></html>'''
   
form_page = lxml.html.fromstring(form_string)
form = form_page.forms[0]
form.fields =  dict(
     name='John Smith',
     phone='555-555-3949',
     interest=set(['cats', 'llamas']))
print form
