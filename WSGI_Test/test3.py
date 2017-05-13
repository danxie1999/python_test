from flask import Flask,url_for,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/login')
def login():
	pass


@app.route('/user/<username>/')
def hello_world(username):
    pass



with app.test_request_context():
	url_for('index')
#	print(url_for('login'))
#	print(url_for('login',next='/'))
#	print(url_for('hello_world',username='Dan Xie'))
#	print(url_for('static',filename='style.css'))
