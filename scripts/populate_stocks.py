from infrastructure.postgres.models.stock_model import Stock
from infrastructure.postgres.utils.connection import Connection
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    conn = Connection(os.getenv("DB_URL"))
    session = conn.get_session()

    population = [
        Stock('AAPL','Apple Inc.',100),
        Stock('MSFT','Microsoft Inc.',200),
        Stock('NVDA','NVIDIA Inc.',158.9),
    ]

    for stock in population:
        session.add(stock)

    session.commit()

if __name__ == '__main__':
    main()