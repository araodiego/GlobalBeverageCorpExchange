from datetime import datetime
from src.enums.trade_type import TradeType
from src.repositories.stock_data import StockData


class Trade:
    def __init__(self, stock_symbol, quantity, trade_type: TradeType, price):
        self.stock_symbol = stock_symbol
        self.timestamp = datetime.now()
        self.quantity = quantity
        self.trade_type = trade_type  # Type is now an instance of TradeType Enum
        self.price = price

    def to_dict(self):
        return {
            'stock_symbol': self.stock_symbol,
            'timestamp': self.timestamp,
            'quantity': self.quantity,
            'trade_type': self.trade_type.value,
            'price': self.price
        }

    def __repr__(self):
        return (f"Trade(stock_symbol={self.stock_symbol}, timestamp={self.timestamp}, "
                f"quantity={self.quantity}, trade_type={self.trade_type.value}, price={self.price})")
