
from flask import Blueprint #clase blueprint
from flask import render_template, request # funcion render_template
from form import LoginForm

page = Blueprint("page", __name__)

@page.app_errorhandler(404) #Maneja pagina de error 404 
def page_not_found(error):
    return render_template("errors/404.html"), 404

@page.route("/") # pagina index
def index():
    return render_template("index.html", title="Index")


@page.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        print(form.username.data)
        print(form.password.data)
        print("Nueva sesión creada!")
    return render_template("auth/login.html", title="Login", form = form)
