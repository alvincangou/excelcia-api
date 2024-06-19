from flask import request, jsonify
from . import main
from models import db
from models.car import Car
from pub import publish

@main.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    new_car = Car(make=data['make'], model=data['model'], year=data['year'])
    db.session.add(new_car)
    db.session.commit()
    file_url = data["file_url"]
    future = publish(file_url, new_car.id)
    
    return jsonify({"message": f"Car added successfully with id {new_car.id}"}), 201

@main.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year, 'available': car.available} for car in cars])

@main.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = Car.query.get_or_404(id)
    return jsonify({'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year, 'available': car.available})

@main.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.get_json()
    car = Car.query.get_or_404(id)
    car.make = data['make']
    car.model = data['model']
    car.year = data['year']
    car.available = data['available']
    db.session.commit()
    return jsonify({"message": "Car updated successfully!"})

@main.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({"message": "Car deleted successfully!"})
