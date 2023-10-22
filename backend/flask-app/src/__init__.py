from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()


def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = open('/secrets/secret_key.txt').readline()

    # connect the DB object to MySQL.
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'When_Can_I_Play_DB'

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Import the various routes
    from src.slots.slots import slots

    # Register the routes that we just imported, so they can be properly handled
    app.register_blueprint(slots, url_prefix='/slots')

    return app
