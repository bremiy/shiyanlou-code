from flask import  Flask,render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('cookie_index.html')


@app.route('/setcookie',methods = ['GET','POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
    resp = make_response(render_template(readcookie.html,userID=user))
    return resp

@app.route('/getcookie')
def getcookie():
    userID = request.cookies.get(userID)
    return 'Hello {}'.format(userID)