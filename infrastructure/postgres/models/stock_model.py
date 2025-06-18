from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'Stocks'

    ticker = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    closing_price = Column(Float, nullable=False)