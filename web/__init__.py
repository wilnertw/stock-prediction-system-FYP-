from flask import Flask
from flask_login import LoginManager


app = Flask("web")
login_manager = LoginManager(app)

def create_app():
    from web.config.Database import myDatabase as db
    from web.controllers import views
    
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'controllers.views.login'
    

    return app

from web.controllers import *
