from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

db = SQLAlchemy()


class SubSection(Enum):
    ONE_A = '1A'
    ONE_B = '1B'
    TWO_A = '2A'
    TWO_B = '2B'


class Slot(db.Model):
    __tablename__ = 'slots'

    slotID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    sport = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    subSection = db.Column(db.Enum(SubSection), nullable=False)
