from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    pet_id = Column(Integer)
    order_date = Column(Date)
    quantity = Column(Integer)

def test_display_cart():
    engine = create_engine("mysql+pymysql://root:Atmecs!1234@localhost:3306/petstore")
    Session = sessionmaker(bind=engine)
    session = Session()

    orders = session.query(Order).all()

    for order in orders:
        print(order.order_id, order.customer_id, order.pet_id, order.order_date, order.quantity)


def test_update_cart():
    order_id = 1
    new_quantity = 3

    order = session.query(Orders).filter_by(order_id=order_id).first()
    order.quantity = new_quantity
    session.commit()

    updated_order = session.query(Orders).filter_by(order_id=order_id).first()
    assert updated_order.quantity == new_quantity


test_update_cart(order_id=1, new_quantity=5)