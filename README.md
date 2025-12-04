Fullstack Developer Assessment — Python API

This repository contains my submission for the Fullstack Developer Assessment.
The assignment includes two parts:

Task 1: Understanding the given data and explaining the structure and findings
Task 2: Building a Python API using FastAPI (you can add Task 2 later once you finish)

Task 1 — Data Understanding & Findings
1. Menu Table
The menu table contains all restaurant items.
Some items have multiple sizes such as Small and Large, and their prices are listed separately.
A few items come with only one standard price because they do not have size variations.

2. Order History Table
The order history table represents individual items within an order.
One row means one item.
If an order contains multiple items, the same order_id appears multiple times.
Each row includes:
item_id
size
price
quantity
total amount for that item
The full order total can be calculated by adding up all item totals for the same order ID.

3. Payments Table
The payments table stores payment details for each order.
Some orders have multiple payment records, indicating split payments (such as cash plus card).
Each payment entry includes:
payment type
total paid
tips
due
discount
payment status
The payment totals match the totals of the items in the order.

4. Table Relationships
The Menu table defines all available items.
The OrderItems table stores items placed in each order.
The Payments table stores payment information for each order.
These tables connect through item_id and order_id.

5. Findings & Observations
The order history table is well-structured, with one row per ordered item.
Payments allow multiple methods for the same order.
Some items have blank size values, indicating they are fixed-price items.
Order totals can be calculated instead of manually stored to avoid mismatches.
Adding foreign key constraints would help improve data integrity.
Overall, the dataset is structured well for relational databases and works smoothly with SQLAlchemy and FastAPI.

Task 2 — Python API Using FastAPI

1. Overview

In Task 2, I created a REST API using FastAPI that returns complete order details by combining data from the Menu, Order History, and Payments tables.
The API has one main endpoint:   GET /orders
This endpoint returns all orders along with:
The items included in each order
Menu information such as item names
All payment records linked to that order

2. How It Works

The data is stored in a SQLite database using SQLAlchemy models.
The endpoint groups order items by order_id.
For each order, it fetches the related items and payment details.
The response is structured so each order contains its items and payment information in a single JSON object.

3. Example Endpoint Implementation

*Code omitted as per user request.*

4. Example Response
[
  {
    "order_id": 10,
    "order_date": "01 Oct 2025",
    "items": [
      {
        "item_id": 2,
        "item_name": "Item2",
        "size": null,
        "price": 2.5,
        "qty": 1,
        "total": 2.5
      }
    ],
    "payments": [
      {
        "payment_type": "Card",
        "total_paid": 9.25,
        "payment_status": "Completed"
      }
    ]
  }
]

5. Project Setup
1. Clone the repository
git clone <your-repo-link>
cd restaurant-api

2. Create and activate virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create database tables
python create_db.py

5. Insert sample data
python seed_data.py

6. Run the server
uvicorn main:app --reload

API will be available at:

http://127.0.0.1:8000/orders

API documentation:

http://127.0.0.1:8000/docs

Project Structure
restaurant-api/
│── main.py
│── create_db.py
│── seed_data.py
│── db.sqlite3
│── requirements.txt
│── venv/
└── README.md
