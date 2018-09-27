from flask import Flask , render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def main():
    return 'Hola Mundo!'

@app.route('/brayan')
def brayan():
    return 'Holaa Brayan!'



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

@app.route('/hello',methods=["GET","POST"])
def hello_form():
    #POST METHOD
    nombre = request.form.get("nombre_input")
    ape = request.form.get("apellido_input")
    # GET METHOD
    # nombre = request.args.get("nombre_input")
    # ape = request.args.get("apellido_input")
    return render_template("hello.html",name = nombre,apellido = ape)


@app.route('/notas',methods=["GET","POST"])
def notas():
    if session.get("notes") is None:
            session["notes"] = []

    if request.method=="POST":
        notta = request.form.get("nota_input")
        session["notes"].append(notta)
        return render_template("notas.html",notes = session["notes"])

    return render_template("notas.html",notes = session["notes"])
