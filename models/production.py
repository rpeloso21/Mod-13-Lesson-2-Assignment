from database import db, Base
import datetime
from sqlalchemy.orm import Mapped, mapped_column


class Production(Base):
    __tablename__ = 'production'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id')) 
    quantity_produced: Mapped[int] = mapped_column(db.Integer, nullable=False)
    date_produced: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    employee_id: Mapped[int] = mapped_column(db.ForeignKey('employees.id'))
