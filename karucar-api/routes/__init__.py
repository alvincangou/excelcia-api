from flask import Blueprint

main = Blueprint('main', __name__)

from .car_routes import *
from .customer_routes import *
from .rental_routes import *