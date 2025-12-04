from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import Menu, OrderItem, Payment

engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()


# ---------------- MENU DATA ----------------
menu_rows = [
    (1,"Item1",1,1,"Small,Large","1.50,2.50"),
    (2,"Item2",1,1,"","3"),
    (3,"Item3",2,2,"","2.5"),
    (4,"Item4",2,2,"","1.5"),
    (5,"Item5",2,1,"","1"),
    (6,"Item6",3,1,"Small,Large","2.50,3.60"),
    (7,"Item7",3,1,"","2.5"),
    (8,"Item8",4,2,"Small,Large","3.75,6.50"),
    (9,"Item9",4,2,"","1.5"),
    (10,"Item10",5,2,"","2"),
]

for r in menu_rows:
    session.add(Menu(
        item_id=r[0], item_name=r[1], cat_id=r[2],
        menu_id=r[3], sizes=r[4], prices=r[5]
    ))


# ---------------- ORDER HISTORY DATA ----------------
order_rows = [
    (1,"01 Oct 2025",10,2,None,2.5,1,"Completed",2.5),
    (2,"01 Oct 2025",10,3,None,1.5,2,"Completed",3.0),
    (3,"01 Oct 2025",10,1,"Small",3.75,1,"Completed",3.75),
]

for r in order_rows:
    session.add(OrderItem(
        id=r[0], order_date=r[1], order_id=r[2], item_id=r[3],
        size=r[4], price=r[5], qty=r[6], order_status=r[7], total=r[8]
    ))


# ---------------- PAYMENTS DATA ----------------
payment_rows = [
    (1,"01 Oct 2025",100,10,9.25,0,0,9.25,"Card","Completed"),
]

for r in payment_rows:
    session.add(Payment(
        id=r[0], payment_date=r[1], payment_id=r[2], order_id=r[3],
        amount=r[4], due=r[5], tips=r[6], discount=0,
        total_paid=r[7], payment_type=r[8], payment_status=r[9]
    ))


session.commit()
session.close()

print("Sample data inserted successfully!")
