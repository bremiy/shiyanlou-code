from flask import  Flask,render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('cookie_index.html')


@app.route('/setcookie', methods=['POST'])
def setcookie():
    user = request.form['name']
    resp = make_response(render_template('readcookie.html',userID=user))
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('user', user)
    return resp

@app.route('/getcookie')
def getcookie():
    user = request.cookies.get('user')
    return 'Hello {}'.format(user)
