from src.db.db import Slot
from flask import Blueprint, make_response, jsonify, request, Response
from src.db.db import db
import pandas as pd
from src.slots.sheet_parser import data_table

slots = Blueprint('slots', __name__)


def jsonify_response(data, status_code) -> tuple[Response, int]:
    response = make_response(jsonify(data))
    response.status_code = status_code
    return response


@slots.route('/slots', methods=['GET'])
def all_slots() -> tuple[Response, int]:
    slots = db.session.execute(db.select(Slot).order_by(Slot.startTime))
    slots_list = []
    for row in slots:
        print(dict(row))
        slots_list.append(dict(row))
    # slots_list = [dict(slot) for slot in slots]
    data = {'message': 'Slots read successfully', 'slots': slots_list}
    return jsonify_response(data, 200)


@slots.route('/import', methods=['POST'])
def import_slot() -> tuple[Response, int]:
    data = data_table
    slots=[]
    for item in data_table:
        slot = Slot(startTime=item['Start Time'], endTime=item['End Time'], sport=item['Sport'], subSection=item['Site'])
        db.session.add(slot)
        db.session.commit()

        inserted_slot = {
            'slotID': slot.slotID,
            'startTime': slot.startTime.isoformat(),
            'endTime': slot.endTime.isoformat(),
            'sport': slot.sport,
            'subSection': slot.subSection,
            'createdAt': slot.createdAt.isoformat(),
            'updatedAt': slot.updatedAt.isoformat(),
        }

        slots.append(inserted_slot)

    data = {"message": "Slots imported successfully", "slots": slots}
    return jsonify_response(data, 201)


@slots.route('/slot/<int:slot_id>', methods=['GET'])
def slot_detail(slot_id) -> tuple[Response, int]:
    slot = db.get_or_404(Slot, slot_id)
    data = {'message': 'Slot read successfully', 'slot': slot}
    return jsonify_response(data, 200)


@slots.route('/update/<int:slot_id>', methods=['PUT'])
def update_slot(slot_id) -> tuple[Response, int]:
    slot = db.get_or_404(Slot, slot_id)
    data = request.get_json()

    for field in ['startTime', 'endTime', 'sport', 'subSection']:
        if field in data:
            setattr(slot, field, data[field])

    db.session.commit()

    data = {'message': 'Slot updated successfully', 'slot': slot}
    return jsonify_response(data, 200)


@slots.route("/slot/<int:slot_id>/delete", methods=["POST"])
def slot_delete(slot_id) -> tuple[Response, int]:
    slot = db.get_or_404(Slot, slot_id)

    db.session.delete(slot)
    db.session.commit()

    data = {'message': 'Slot deleted successfully'}
    return jsonify_response(data, 200)
