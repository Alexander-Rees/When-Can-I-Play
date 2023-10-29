from src.db.db import Slot
from flask import Blueprint, make_response, jsonify
from src import db

slots = Blueprint('slots', __name__)


@slots.route('/slots', methods=['GET'])
def all_slots() -> list[Slot]:
    slots = db.session.execute(db.select(Slot).order_by(Slot.startTime)).scalars()
    return make_response(jsonify(slots), 200)


# create route

# read route

# update route
@slots.route('/update/<int:slotID>', methods=['PUT']) #might need to be slotID instead slot_id
def update_slot(slotID):
    data = request.get_json()

    # Update the slot in the database
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE slots SET column1 = ?, column2 = ? WHERE id = ?', (data['value1'], data['value2'], slotID))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Slot updated successfully'}))
    response.status_code = 200
    return response

# delete route
