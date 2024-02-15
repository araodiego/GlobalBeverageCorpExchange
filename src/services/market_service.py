from datetime import datetime, timedelta

import pandas as pd
from scipy.stats import gmean

from src.enums.trade_type import TradeType
from src.repositories.stock_data import StockData


class MarketService:
    def __init__(self):
        self.trades = pd.DataFrame(columns=['stock_symbol', 'timestamp', 'quantity', 'trade_type', 'price'])
        self.stock_data = StockData()

    def record_trade(self, stock_symbol, quantity, trade_type: TradeType, price):
        """
        Record a trade for a given stock in the market.

        :param stock_symbol: The symbol of the stock being traded.
        :param quantity: The quantity of stocks being traded.
        :param trade_type: The type of trade (BUY or SELL).
        :param price: The price at which the trade was executed.
        """
        if stock_symbol not in self.stock_data.stocks['stock_symbol'].values:
             raise ValueError(f"Stock with symbol {stock_symbol} does not exist in the market.")
        else:
            new_trade = {
                'stock_symbol': stock_symbol,
                'timestamp': datetime.now(),
                'quantity': quantity,
                'trade_type': trade_type.value,
                'price': price
            }
            self.trades = self.trades._append(new_trade, ignore_index=True)

    def calculate_dividend_yield(self, stock_symbol, price):
        """"
            Calculate the Dividend Yield of a given stock
            :param: stock_symbol Symbol of the Stock
            :param: price that will be used to calculate the Dividend Yield
            :return: The Dividend Yield for the given Stock
        """
        if stock_symbol not in self.stock_data.stocks['stock_symbol'].values:
            raise ValueError(f"Stock with symbol {stock_symbol} does not exist in the market.")
        else:
            stock = self.stock_data.get_stock(stock_symbol)
            if stock is None:
                return None
            else:
                return stock.calculate_dividend_yield(price)

    def calculate_pe_ratio(self, stock_symbol, price):
        """"
            Calculate the P/E ratio of a gicen stock for a given price
            :param: stock_symbol: The symbol of the Stock
            :param: price of the Stock to calculate the P/E ratio for
            :return: None if there's no Stock in the market or the P/E ratio for an existing stock
        """
        if stock_symbol not in self.stock_data.stocks['stock_symbol'].values:
            raise ValueError(f"Stock with symbol {stock_symbol} does not exist in the market.")
        else:
            stock = self.stock_data.get_stock(stock_symbol)
            if  stock is None:
                return None
            else:
                return stock.calculate_pe_ratio(price)

    def calculate_volume_weighted_stock_price(self, stock_symbol):
        """
        Calculate the Volume Weighted Stock Price for a given stock based on trades in the last 5 minutes.

        :param stock_symbol: The symbol of the stock.
        :return: The Volume Weighted Stock Price or None if there are no trades.
        """
        if stock_symbol not in self.stock_data.stocks['stock_symbol'].values:
            raise ValueError(f"Stock with symbol {stock_symbol} does not exist in the market.")
        else:
            now = datetime.now()
            five_minutes_ago = now - timedelta(minutes=5)
            relevant_trades = self.trades[
                (self.trades['stock_symbol'] == stock_symbol) & (self.trades['timestamp'] >= five_minutes_ago)]

            if relevant_trades.empty:
                return None

            vwsp = (relevant_trades['price'] * relevant_trades['quantity']).sum() / relevant_trades['quantity'].sum()
            return vwsp

    def calculate_geometric_all_share_index(self):
        """
        Calculate the All Share Index using the geometric mean of the VWSP for all stocks.

        Parameters:
        df (DataFrame): Pandas DataFrame containing stock trade data.

        Returns:
        float: The geometric All Share Index.
        """
        # Calculate VWSP for each stock symbol
        vwsp_values = []
        for stock_symbol in self.trades['stock_symbol'].unique():
            vwsp = self.calculate_volume_weighted_stock_price(stock_symbol)
            if vwsp is not None:
                vwsp_values.append(vwsp)

        # Check if we have any VWSP values
        if not vwsp_values:
            return None

        # Calculate the geometric mean of the VWSP values
        all_share_index = gmean(vwsp_values)
        return all_share_index
