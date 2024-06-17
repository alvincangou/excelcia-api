from . import db

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    rental_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)

    car = db.relationship('Car', backref=db.backref('rentals', lazy=True))

    def __repr__(self):
        return f'<Rental {self.customer.name} {self.rental_date}>'