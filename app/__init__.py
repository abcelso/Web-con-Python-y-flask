
from flask import Flask
from .views import page
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap()

def create_app(config):
    app.config.from_object(config) #Agrego archivo de configuración
    
    bootstrap.init_app(app) #Agrego Bootstrap a mi app

    app.register_blueprint(page)
    
    return app



