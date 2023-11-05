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
    slot = Slot(
        startTime = data['startTime'], 
        endTime = data['endTime'],
        sport = data['sport'],
        subSection = data['subSection']
    )
    db.session.add(slot)
    db.session.commit()
    return make_response(201)
    
# read route

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

# update route
@slots.route('/update/<int:slotID>', methods=['PUT']) #might need to be slotID instead slot_id
def update_slot(slotID):


    # Update the slot in the database
    cursor = db.get_db().cursor()
insert()




    cursor.execute('UPDATE slots SET column1 = ?, column2 = ? WHERE id = ?', (data['value1'], data['value2'], slotID))
    db.get_db().commit()

    response = make_response(jsonify({'message': 'Slot updated successfully'}))
    response.status_code = 200
    return response

# delete route
