from src.db.db import Slot
from flask import Blueprint, make_response, jsonify
from src import db

slots = Blueprint('slots', __name__)


@slots.route('/slots', methods=['GET'])
def all_slots() -> list[Slot]:
    slots = db.session.execute(db.select(Slot).order_by(Slot.startTime)).scalars()
    response = make_response(jsonify({'message': 'Slots read successfully', 'slots':slots}))
    response.status_code = 200
    return response


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
@app.route('/slot/<int:slot_id>', methods=['GET'])
def slot_detail(slot_id):
    slot = db.get_or_404(Slot, slot_id)
    response = make_response(jsonify({'message': 'Slot read successfully', 'slot':slot} ))
    response.status_code = 200
    return response

# update route
@slots.route('/update/<int:slot_id>', methods=['PUT'])
def update_slot(slot_id):
    slot = db.get_or_404(Slot, slot_id)
    data = request.get_json()

    if 'startTime' in data:
        slot.startTime = data['startTime']
    if 'endTime' in data:
        slot.endTime = data['endTime']
    if 'sport' in data:
        slot.sport = data['sport']
    if 'subSection' in data:
        slot.subSection = data['subSection']

    db.session.commit()
    
    response = make_response(jsonify({'message': 'Slot updated successfully', 'slot': slot}))
    response.status_code = 200
    return response
    

# delete route
@app.route("/slot/<int:slot_id>/delete", methods=["POST"])
def slot_delete(slot_id):
    slot = db.get_or_404(Slot, slot_id)

    db.session.delete(slot)
    db.session.commit()
    response = make_response(jsonify({'message': 'Slot deleted successfully'}))
    response.status_code = 200
    return response