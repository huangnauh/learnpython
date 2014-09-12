import cgitb
cgitb.enable()
import cgi
import time
import os
monthmap = {1:'January',2:'February',
            3:'March',4:'April',5:'May',
            6:'June',7:'July',8:'August',
            9:'September',10:'October',
            11:'November',12:'December'}
daymap = {0:'Monday',1:'Tuesday',2:'Wednesday',
            3:'Thursday',4:'Friday',5:'Saturday',
            6:'Sunday'}
def print_month_quiz():
    print "what month is it?<p>"
    print '<form method="POST" action="%s">' % os.environ['SCRIPT_NAME']
    for code,name in monthmap.items():
        print '<input name="month" type="radio" value="%d"> %s<br>' % \
                (code,name)
    print '<input type="submit" name="submit" value="next &gt;&gt;">'
    print "</form>"

def print_day_quiz():
    month = time.localtime()[1]
    print "what day is it?<p>"
    print "<form method='POST' action='%s'>" % os.environ['SCRIPT_NAME']
    print "<input type='hidden' name='month' value='%d'>" % month
    for code,name in daymap.items():
        print '<input name="day" type="radio" value="%d"> %s<br>' % \
            (code,name)
    print '<input type="submit" name="submit" value="next &gt;&gt;">'
    print "</form>"
    
    
def check_month_answer(answer):
    month = time.localtime()[1]
    if int(answer) == month:
        print "Yes,this is <b>%s</b>.<p>" % monthmap[month]
        return 1
    else:
        print "sorry,you're wrong. Try again:<p>"
        print_month_quiz()
        return 0
        
def check_day_answer(answer):
    day = time.localtime()[6]
    if int(answer) == day:
        print "yes,this is <b> %s</b>." % daymap[day]
        return 1
    else:
        print "sorry, you're wrong.Try again:<p>"
        print_day_quiz()
        return 0
        
print "Content-type:text/html"
print
print """<HTML>
<HEAD>
<TITLE>Sample CGI Script</TITLE>
</HEAD>
<BODY>"""
#cgi.print_environ()
form = cgi.FieldStorage()
if form.getfirst('month') == None:
    print_month_quiz()
elif form.getfirst('day') == None:
    ismonthright = check_month_answer(form.getfirst('month'))
    if ismonthright:
        print_day_quiz()
else:
    ismonthright = check_month_answer(form.getfirst('month'))
    if ismonthright:
        check_day_answer(form.getfirst('day'))
print "</BODY></HTML>"
