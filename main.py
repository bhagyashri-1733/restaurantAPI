from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Menu, OrderItem, Payment

app = FastAPI()

# DB Connection
engine = create_engine("sqlite:///db.sqlite3")
SessionLocal = sessionmaker(bind=engine)


@app.get("/orders")
def get_all_orders():
    session = SessionLocal()

    orders_dict = {}

    # Fetch orders
    order_rows = session.query(OrderItem).all()

    for row in order_rows:
        order_id = row.order_id

        if order_id not in orders_dict:
            orders_dict[order_id] = {
                "order_id": order_id,
                "order_date": row.order_date,
                "items": [],
                "payments": []
            }

        # Fetch item name from menu
        item = session.query(Menu).filter(Menu.item_id == row.item_id).first()

        orders_dict[order_id]["items"].append({
            "item_id": row.item_id,
            "item_name": item.item_name if item else "Unknown",
            "size": row.size,
            "price": row.price,
            "qty": row.qty,
            "total": row.total
        })

    # Fetch payments
    payment_rows = session.query(Payment).all()

    for p in payment_rows:
        if p.order_id in orders_dict:
            orders_dict[p.order_id]["payments"].append({
                "payment_id": p.payment_id,
                "payment_type": p.payment_type,
                "total_paid": p.total_paid,
                "payment_status": p.payment_status
            })

    session.close()

    return list(orders_dict.values())
