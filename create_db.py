from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Base class for SQLAlchemy models
Base = declarative_base()

# SQLite Database
engine = create_engine("sqlite:///db.sqlite3", echo=True)

SessionLocal = sessionmaker(bind=engine)


# MENU TABLE
class Menu(Base):
    __tablename__ = "menu"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    cat_id = Column(Integer)
    menu_id = Column(Integer)
    sizes = Column(String)
    prices = Column(String)


# ORDER ITEMS TABLE
class OrderItem(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    order_date = Column(String)
    order_id = Column(Integer)
    item_id = Column(Integer)
    size = Column(String)
    price = Column(Float)
    qty = Column(Integer)
    order_status = Column(String)
    total = Column(Float)


# PAYMENTS TABLE
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    payment_date = Column(String)
    payment_id = Column(Integer)
    order_id = Column(Integer)
    amount = Column(Float)
    due = Column(Float)
    tips = Column(Float)
    discount = Column(Float)
    total_paid = Column(Float)
    payment_type = Column(String)
    payment_status = Column(String)


def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()
