from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import random
import json
import logging

class StockGenerator():
    def __init__(self, asset_ticker: str, bootstrap_servers: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            key_serializer = lambda x: json.dumps(x).encode('utf-8'),
            value_serializer = lambda x: json.dumps(x).encode('utf-8')
        )
        self.ticker = asset_ticker
        self.price = 100
        self.volatility = 0.2
        self.logger = logging.getLogger(__name__)

        self.logger.info(f"Stock Generator for ticker {self.ticker} initialized correctly")
        self.logger.info(f"Generating stock price data")

    def start(self):
        while True:
            self.generate_new_price()

            self.producer.send('test-topic-1', key=self.ticker, value= {
                'ticker': self.ticker,
                'price': self.price
            })
            time.sleep(1)

    def generate_new_price(self):
        self.price = self.price + random.gauss(0, self.volatility)