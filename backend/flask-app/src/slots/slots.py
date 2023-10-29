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

# update route

# delete route
