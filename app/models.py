from datetime import datetime
from app import db

class Plant(db.Model):
    """Plant model for database storage"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    water_frequency = db.Column(db.Integer, nullable=False)
    last_watered = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Plant {self.name}>'

    def days_since_watered(self):
        """Calculate days since last watered"""
        return (datetime.now().date() - self.last_watered).days

    def needs_water(self):
        """Check if plant needs water based on frequency"""
        return self.days_since_watered() >= self.water_frequency