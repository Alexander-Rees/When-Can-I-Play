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

# update route

# delete route
