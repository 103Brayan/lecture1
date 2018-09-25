from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hola Mundo!'

@app.route('/brayan')
def brayan():
    return 'Holaa Brayan!'

@app.route('/<string:name>')
def hello(name):
    return "<h1> "+name.upper()+" </h1>"

@app.route('/index')
def index():
    return render_template("hello.html")

@app.route('/link')
def link():
    return render_template("link.html")
