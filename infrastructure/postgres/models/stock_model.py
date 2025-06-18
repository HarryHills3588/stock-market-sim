from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'Stocks'

    ticker = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    closing_price = Column(Float, nullable=False)

    def __init__(self, ticker:str, name:str, closing_price:float):
        self.ticker = ticker
        self.name = name
        self.closing_price = closing_price
