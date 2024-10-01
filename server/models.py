from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize SQLAlchemy
db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"
    
    # Define the columns for the Earthquake model
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)  # Magnitude of the earthquake
    location = db.Column(db.String, nullable=False)   # Location of the earthquake
    year = db.Column(db.Integer, nullable=False)      # Year of the earthquake

    def __repr__(self):
        # Format the representation string
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
