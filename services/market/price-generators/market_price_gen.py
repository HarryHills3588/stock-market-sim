from price_generator import StockGenerator
from infrastructure.postgres.models.stock_model import Stock
from infrastructure.postgres.utils.connection import Connection
import threading

from dotenv import load_dotenv
import os 
import logging

def main():
    try:
        logger = logging.getLogger(__name__)
        load_dotenv()
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        db = os.getenv("POSTGRES_DB")
        bootstrap_server = os.getenv("BOOTSTRAP_SERVER")

        connection = Connection(f"postgresql://{user}:{password}@localhost:5432/{db}")
        session = connection.get_session()
        logger.info("session created")

        ## query the DB
        result = session.query(Stock).all()
        logger.debug(f"queried stocks, result {result}")
        
        for stock in result:
            generator = StockGenerator(stock.ticker, bootstrap_servers=bootstrap_server)
            thread = threading.Thread(target=generator.start, daemon=True)
            thread.start()
            logger.debug(f"Thread started for {stock.ticker}")

        thread.join()

    finally:
        logger.info(f"Cleaning up")
        connection.shutdown()

if __name__ == "__main__":
    main()