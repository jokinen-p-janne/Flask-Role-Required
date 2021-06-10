from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    login.init_app(app)
    login.login_view = 'login'

    from project.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from project.blueprints.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from project.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
