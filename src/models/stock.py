from datetime import datetime, timedelta

from src.enums.stock_type import StockType


class Stock:
    def __init__(self, symbol, stock_type: StockType, last_dividend, fixed_dividend_percent, par_value):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend_percent = fixed_dividend_percent / 100 if fixed_dividend_percent is not None else 0
        self.par_value = par_value
        self.trades = []

    def calculate_dividend_yield(self, price):
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if self.stock_type == StockType.COMMON:
            return self.last_dividend / price
        elif self.stock_type == StockType.PREFERRED:
            return (self.fixed_dividend_percent * self.par_value) / price

    def calculate_pe_ratio(self, price):
        dividend = self.calculate_dividend_yield(price) * price
        if dividend <= 0:
            return None
        return price / dividend

    def calculate_volume_weighted_stock_price(self):
        total_price_quantity = 0
        total_quantity = 0
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        for trade in self.trades:
            if trade.timestamp >= five_minutes_ago:
                total_price_quantity += trade.price * trade.quantity
                total_quantity += trade.quantity
        if total_quantity == 0:
            return None
        return total_price_quantity / total_quantity


