from flask import request, jsonify
from . import bp
from ..models import Order, db
from ..services import product_service, payment_service
import uuid
from datetime import datetime
from flask import jsonify
from sqlalchemy.sql import text

@bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    product_ids = data.get('product_ids')
    quantities = data.get('product_quantities')
    user_id = data.get('user_id')

    # Interact with Product Service
    if not product_service.check_availability(product_ids, quantities):
        return jsonify({"error": "One or more products are not available"}), 400

    total_price = product_service.get_total_price(product_ids, quantities)

    # Update inventory
    product_service.update_inventory(product_ids, quantities)

    # Generate transaction ID
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    transaction_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{user_id}-{product_ids}-{timestamp}"))

    # Save order to DB
    new_order = Order(
        product_ids=product_ids,
        product_quantities=quantities,
        user_id=user_id,
        total_price=total_price,
        transaction_id=transaction_id
    )
    db.session.add(new_order)
    db.session.commit()

    order_id = new_order.id
    # Notify Payment Service
    payment_service.process_payment(transaction_id, total_price, order_id, user_id)

    return jsonify({"message": "Order created successfully", "transaction_id": transaction_id}), 201

@bp.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return jsonify([
        {
            "id": order.id,
            "product_ids": order.product_ids,
            "product_quantities": order.product_quantities,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "transaction_id": order.transaction_id
        } for order in orders
    ]), 200

@bp.route('/orders/user/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    result = [
        {
            "id": order.id,
            "product_ids": order.product_ids,
            "product_quantities": order.product_quantities,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "transaction_id": order.transaction_id
        } for order in orders
    ]
    return jsonify(result), 200

@bp.route('/orders/product/<int:product_id>', methods=['GET'])
def get_orders_by_product(product_id):
    query = text(f"""
        SELECT *
        FROM public."order"
        WHERE product_ids::jsonb @> '{product_id}'::jsonb;
    """)
    # Pass the product_id as a parameter
    results = db.session.execute(query).fetchall()

    # Transform the result into a JSON-compatible format
    orders = [
        {
            "id": row.id,
            "product_ids": row.product_ids,
            "product_quantities": row.product_quantities,
            "user_id": row.user_id,
            "total_price": row.total_price,
            "transaction_id": row.transaction_id
        }
        for row in results
    ]

    return jsonify(orders)
