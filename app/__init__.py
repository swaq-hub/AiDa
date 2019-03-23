
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)


    # set config
    # os.environ['DEBUG'] = '1'
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    #app.run(ssl_context='adhoc')

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    from app.api.aida_api import aida_blueprint
    app.register_blueprint(aida_blueprint)


    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
