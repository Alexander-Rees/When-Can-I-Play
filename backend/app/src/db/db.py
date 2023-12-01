from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, DateTime, String
from typing import Union

db = SQLAlchemy()


class Slot(db.Model):
    __tablename__ = 'slots'

    slotID: int = db.Column(Integer, primary_key=True, autoincrement=True)
    startTime: datetime = db.Column(DateTime, nullable=False)
    endTime: datetime = db.Column(DateTime, nullable=False)
    sport: str = db.Column(String(255), nullable=False)
    createdAt: datetime = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    updatedAt: datetime = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    subSection: str = db.Column(String(255), nullable=False)

    def __init__(self, startTime: str, endTime: str, sport: str, subSection: str) -> None:
        self.startTime = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        self.endTime = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        self.sport = sport
        self.subSection = subSection


def serialize_slot(slot: Slot) -> dict[str, Union[int, str]]:
    return {
        'slotID': slot.slotID,
        'startTime': slot.startTime.strftime('%Y-%m-%d %H:%M:%S'),
        'endTime': slot.endTime.strftime('%Y-%m-%d %H:%M:%S'),
        'sport': slot.sport,
        'createdAt': slot.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
        'updatedAt': slot.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
        'subSection': slot.subSection,
    }
