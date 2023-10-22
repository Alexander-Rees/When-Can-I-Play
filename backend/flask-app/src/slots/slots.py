from flask import Blueprint

slots = Blueprint('slots', __name__)


@slots.route('/all', methods=['GET'])
def all_slots() -> list:
    return []
