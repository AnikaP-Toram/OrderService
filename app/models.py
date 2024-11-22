from . import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_ids = db.Column(db.JSON, nullable=False)
    product_quantities = db.Column(db.JSON, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    transaction_id = db.Column(db.String, unique=True, nullable=False)