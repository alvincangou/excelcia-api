from . import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=False, nullable=False)
    file = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'