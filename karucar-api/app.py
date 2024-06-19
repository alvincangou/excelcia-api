from flask import Flask, request, jsonify
from config import Config
from models import db
from routes import main
from pub import publish


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(main)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Initialize database
    port = int(8080)
    app.run(host='0.0.0.0', port=port, debug=True)