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

# update route

# delete route
