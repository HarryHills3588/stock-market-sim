from price_generator import StockGenerator
from infrastructure.postgres.models.stock_model import Stock
from infrastructure.postgres.utils.connection import Connection

from dotenv import load_dotenv
import os 
import logging

def main():
    logger = logging.getLogger(__name__)
    load_dotenv()
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")

    connection = Connection(f"postgresql://{user}:{password}@localhost:5432/{db}")
    session = connection.get_session()

    ## query the DB
    ## get results from query
    ## initialize market through threads
    
    logger.info("session created")

