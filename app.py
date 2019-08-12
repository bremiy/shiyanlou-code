from flask import request
from flask import Flask
from flask import url_for
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


'''
@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)
'''


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post{}'.format(post_id)


@app.route('/courses/<name>')
def courses_index(name):
    return 'courses:{}'.format(name)


@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index', username='shixiaolou'))
    print(url_for('show_post', post_id=1, _external=True))
    print(url_for('show_post', post_id=2, q='python 03'))
    print(url_for('show_post', post_id=2, q='python??'))
    print(url_for('show_post', post_id=2, _anchor='a'))
    return 'test'


@app.route('/<username>')
def hello(username):
    if username == "shiyanlou":  # 如果访问/shiyanlou 则显示页面
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))  # 否则重新定向到主页


@app.route('/user/<username>')
def user_index(username):
    print('----------------')
    print(request.headers)
    print('----------------')
    print(request.args)
    print('----------------')
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time', request.args.get('time'))
    print('q', request.args.get('q'))
    print('Q', request.args.get('Q'))
    return 'Hello {}'.format(username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    print('method>:',request.method)
    print('name:',request.form.get('name'))
    print('password:',request.form.get('password'))
    print('hobbies:',request.form.getlist('hobbies'))
    print('age:',request.form,get('age',default=18))
    """
    if request.method == 'POST':
        print('name:', request.form.get('name'))
        print('password:', request.form.get('password'))
        print('hobbies:', request.form.getlist('hobbies'))
        print('age:', request.form.get('age', default=18))
    return 'registered successfully!'


@app.route('/httptest', methods=['GET', 'POST'])
def httptest():
    print('t:',request.form.get('t'))
    print('q:',request.form.get('q'))
    print('Q:',request.form.getlist('Q'))
    return 'It is a get request'
    
if __name__ == '__main__':
    app.run()
