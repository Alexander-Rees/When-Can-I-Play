from flask import Flask
from src.db.db import db


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = open('/secrets/secret_key.txt').readline()

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///when_can_i_play.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from src.slots.slots import slots

    app.register_blueprint(slots, url_prefix='/slots')

    return app
