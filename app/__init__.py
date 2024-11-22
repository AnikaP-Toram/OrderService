from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        from app import models  # Import models here
        db.create_all()
    
    # Register blueprints
    from .routes import orders
    app.register_blueprint(orders.bp)

    return app
