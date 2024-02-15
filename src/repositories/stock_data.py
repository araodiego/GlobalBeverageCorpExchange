import pandas as pd
from src.models.stock import Stock
from src.enums.stock_type import StockType

class StockData:
  def __init__(self):
    """
    Initializes a new instance of the StockData repository with a Pandas DataFrame.
    """
    data = {
      'stock_symbol': ['TEA', 'POP', 'ALE', 'GIN', 'JOE'],
      'type': [StockType.COMMON, StockType.COMMON, StockType.COMMON, StockType.PREFERRED, StockType.COMMON],
      'last_dividend': [0, 8, 23, 8, 13],
      'fixed_dividend': [None, None, None, 2, None],  # 2% as decimal
      'par_value': [100, 100, 60, 100, 250]
    }
    self.stocks = pd.DataFrame(data)

  def get_stock(self, stock_symbol):
    """
    Retrieve a Stock instance by its symbol.

    :param stock_symbol: The symbol of the stock to retrieve.
    :return: A Stock instance created from the DataFrame row.
    :raises ValueError: If the stock symbol is not found in the repository.
    """
    stock_data = self.stocks.query("stock_symbol == @stock_symbol")
    if not stock_data.empty:
      row = stock_data.iloc[0]
      return Stock(row['stock_symbol'], row['type'], row['last_dividend'], row['fixed_dividend'], row['par_value'])
    else:
      raise ValueError(f"Stock with symbol '{stock_symbol}' not found.")


  def add_stock(self, stock:Stock):
    """
    Add a new Stock instance to the repository.

    :param stock: The Stock instance to add.
    :raises ValueError: If a stock with the same symbol already exists.
    """
    if stock.symbol in self.stocks['stock_symbol'].values:
      raise ValueError(f"Stock with symbol '{stock.symbol}' already exists.")

    new_row = pd.Series({
        'stock_symbol': stock.symbol,
        'type': stock.stock_type,
        'last_dividend': stock.last_dividend,
        'fixed_dividend': stock.fixed_dividend_percent,
        'par_value': stock.par_value
    })
    self.stocks = self.stocks.append(new_row, ignore_index=True)

  def remove_stock(self, stock_symbol):
    """
    Remove a Stock instance from the repository by its symbol.

    :param symbol: The symbol of the stock to remove.
    :raises ValueError: If the stock symbol is not found in the repository.
    """
    if stock_symbol not in self.stocks['stock_symbol'].values:
      raise ValueError(f"Stock with symbol '{stock_symbol}' not found.")

    self.stocks = self.stocks[self.stocks['stock_symbol'] != stock_symbol]

  def list_stocks(self):
    """
    List all Stock instances in the repository.

    :return: A list of Stock instances.
    """
    stocks = []
    for _, row in self.stocks.iterrows():
      stocks.append(Stock(row['stock_symbol'], row['type'], row['last_dividend'], row['fixed_dividend'], row['par_value']))
    return stocks