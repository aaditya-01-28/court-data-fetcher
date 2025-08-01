# app/__init__.py
from flask import Flask
from .database import init_db

def create_app():
    app = Flask(__name__)
    
    # Initialize the database
    with app.app_context():
        init_db()

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app