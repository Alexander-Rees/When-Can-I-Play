from src.db.db import Slot
from flask import Blueprint, make_response, jsonify
from src import db

slots = Blueprint('slots', __name__)


@slots.route('/slots', methods=['GET'])
def all_slots() -> list[Slot]:
    slots = db.session.execute(db.select(Slot).order_by(Slot.startTime)).scalars()
    return make_response(jsonify(slots), 200)


# create route
@slots.route('/create', methods=['POST'])
def create_slot():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = 'INSERT INTO slots (column1, column2) VALUES (%s, %s)'
    cursor.execute(query, (data['field1'], data['field2']))
    db.get_db().commit()
    response = make_response(jsonify({"message": "Slot created successfully"}), 201)
    return response
    
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
