from typing import List
import datetime
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key= True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id')) 
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    total_price:Mapped[float] = mapped_column(db.Float, nullable=False)
