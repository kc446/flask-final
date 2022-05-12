"""A simple Flask web app."""

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_cors import CORS
#from flask_mail import Mail #pretty sure we don't actually need the mail stuff but i'll leave it in anyway
from flask_wtf.csrf import CSRFProtect

import flask_login
from app.auth import auth
from app.cli import create_database
from app.context_processors import utility_text_processors
from app.db import database
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con
from app.simple_pages import simple_pages


#mail = Mail()
login_manager = flask_login.LoginManager()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    #trying something here to see if it's the port for some reason
    #if __name__ == "__main__":
        #port = int(os.environ.get("PORT", 5000))
        #app.run(host='0.0.0.0', port=port)

    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")
    #app.mail = Mail(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    csrf.exempt(auth)
    bootstrap = Bootstrap5(app)

    # apply the blueprints to the app
    app.register_blueprint(auth)
    app.register_blueprint(database)
    app.register_blueprint(simple_pages)

    # these load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)

    app.context_processor(utility_text_processors)

    # add command function to cli commands
    app.cli.add_command(create_database)
    db.init_app(app)

    api_v1_cors_config = {"methods": ["OPTIONS", "GET", "POST"]}
    CORS(app, resources={"/api/*": api_v1_cors_config})

    # Run once at startup
    return app

@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
