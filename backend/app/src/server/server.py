from flask import Flask
from src.db.db import db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'rust_is_the_best_language-ferris_the_crab'

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///when_can_i_play.db"

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    from src.slots.slots import slots

    app.register_blueprint(slots, url_prefix='/slots')

    return app
