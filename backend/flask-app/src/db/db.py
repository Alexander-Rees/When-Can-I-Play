from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Slot(db.Model):
    __tablename__ = 'slots'

    slotID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    sport = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    subSection = db.Column(db.String(255), nullable=False)

    def __init__(self, startTime, endTime, sport, subSection):
        self.startTime = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        self.endTime = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        self.sport = sport
        self.subSection = subSection
