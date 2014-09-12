from flask import Flask,url_for,request,abort,redirect,session
from flask import render_template,make_response,escape
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return redirect(url_for('hello_world'))


def test11():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    if name is None:
        name = "visiter"
    value = name + ", you are not logged in"
    if 'username' in session:
        value =  session['username']
    resp = make_response(render_template('hello.html',name=value))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %s" % post_id

@app.route('/projects/')
def projects():
    return 'The project page'
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

def test1():
    with app.test_request_context('/test', method='GET'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'GET'


def test():
    app.run()
    
    
if __name__ == '__main__':
    app.run(debug=True)