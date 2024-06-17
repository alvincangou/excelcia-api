from flask import request, jsonify
from . import main
from models import db
from models.car import Car
from models.customer import Customer
from models.rental import Rental
from datetime import datetime

@main.route('/rentals', methods=['POST'])
def add_rental():
    data = request.get_json()
    car = Car.query.get_or_404(data['car_id'])
    customer = Customer.query.get_or_404(data['customer_id'])
    if not car.available:
        return jsonify({"message": "Car not available for rental"}), 400
    new_rental = Rental(car_id=data['car_id'], customer_id=data['customer_id'], rental_date=datetime.strptime(data['rental_date'], '%Y-%m-%d'))
    car.available = False
    db.session.add(new_rental)
    db.session.commit()
    return jsonify({"message": "Rental added successfully!"}), 201

@main.route('/rentals', methods=['GET'])
def get_rentals():
    rentals = Rental.query.all()
    return jsonify([{'id': rental.id, 'car_id': rental.car_id, 'customer_id': rental.customer_id, 'rental_date': rental.rental_date, 'return_date': rental.return_date} for rental in rentals])

@main.route('/rentals/<int:id>', methods=['GET'])
def get_rental(id):
    rental = Rental.query.get_or_404(id)
    return jsonify({'id': rental.id, 'car_id': rental.car_id, 'customer_id': rental.customer_id, 'rental_date': rental.rental_date, 'return_date': rental.return_date})

@main.route('/rentals/<int:id>/return', methods=['PUT'])
def return_rental(id):
    rental = Rental.query.get_or_404(id)
    if rental.return_date:
        return jsonify({"message": "Car already returned"}), 400
    rental.return_date = datetime.now()
    car = Car.query.get_or_404(rental.car_id)
    car.available = True
    db.session.commit()
    return jsonify({"message": "Car returned successfully!"})