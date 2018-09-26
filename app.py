from flask import Flask , render_template
import datetime

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
    return render_template("index.html",hola="HOLA!")

@app.route('/link')
def link():
    return render_template("link.html")

@app.route('/new_year')
def new_year():
    gg = datetime.datetime.now()
    ny = gg.month == 1 and gg.day == 1

    return render_template("index.html",new_year=ny,headline = "IS IT NEW YEAR?")

@app.route('/loop')
def loop():
    lista = ["brayan0","brayan1","brayan2"]
    return render_template("index.html",names = lista)

@app.route('/hijo1')
def hijo1():
    return render_template("hijo1.html")

@app.route('/hijo2')
def hijo2():
    return render_template("hijo2.html")
