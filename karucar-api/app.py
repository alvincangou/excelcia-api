from flask import Flask
from config import Config
from models import db
from routes import main

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(main)

if __name__ == '__app__':
    with app.app_context():
        db.create_all()  # Initialize database
    port = int(8080)
    app.run(host='0.0.0.0', port=port, debug=True)