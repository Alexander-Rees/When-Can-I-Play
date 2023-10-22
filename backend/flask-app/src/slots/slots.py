from flask import Blueprint, make_response, jsonify, request
from src import db

slots = Blueprint('slots', __name__)


@slots.route('/all', methods=['GET'])
def all_slots() -> list:
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM slots')
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# create route

# read route

app = Flask(__name__)

# Assuming you have a database named 'mydatabase.db'
DATABASE = 'mydatabase.db'

# Function to connect to the database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Read route to retrieve information from the database
@app.route('/get_data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table WHERE id = ?', (data_id,))
    data = cursor.fetchone()
    conn.close()

    if data is None:
        return jsonify({'error': 'Data not found'}), 404

    return jsonify(dict(data))

if __name__ == '__main__':
    app.run(debug=True)

# update route

# delete route
