from src.db.db import Slot
from flask import Blueprint, make_response, jsonify, request
from src import db 

slots = Blueprint('slots', __name__)


@slots.route('/slots', methods=['GET'])
def all_slots():
    slots = db.session.execute(db.select(Slot).order_by(Slot.startTime)).fetchall()
    slots_list = [dict(slot) for slot in slots]

    response_data = {
        'message': 'Slots read successfully',
        'slots': slots_list
    }

    return jsonify(response_data), 200


# create route
@slots.route('/create', methods=['POST'])
def create_slot():
    data = request.get_json()

    slot = Slot(
        startTime=data['startTime'],
        endTime=data['endTime'],
        sport=data['sport'],
        subSection=data['subSection']
    )
    db.session.add(slot)
    db.session.commit()

    inserted_slot = {
        'slotID': slot.slotID,
        'startTime': slot.startTime.isoformat(),
        'endTime': slot.endTime.isoformat(),
        'sport': slot.sport,
        'subSection': slot.subSection,
        'createdAt': slot.createdAt.isoformat(),
        'updatedAt': slot.updatedAt.isoformat()
    }

    return jsonify({"message": "Slot created successfully", "slot": inserted_slot}), 201

# Read route to retrieve information from the database
@slots.route('/slot/<int:slot_id>', methods=['GET'])
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
@slots.route("/slot/<int:slot_id>/delete", methods=["POST"])
def slot_delete(slot_id):
    slot = db.get_or_404(Slot, slot_id)

    db.session.delete(slot)
    db.session.commit()
    response = make_response(jsonify({'message': 'Slot deleted successfully'}))
    response.status_code = 200
    return response