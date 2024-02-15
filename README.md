# Global Beverage Corporation Exchange System

The Global Beverage Corporation Exchange System is an object-oriented platform designed to simulate stock market trading for beverage companies. This system allows for recording trades, calculating various metrics such as dividend yield and P/E ratio, volume-weighted stock price, and the geometric all-share index.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python installed on your system. This project requires Python 3.6 or newer. Additionally, you will need `pandas` and `scipy` libraries. You can install these dependencies using `pip`:

```bash
pip install pandas scipy
```

### Navigate to the project directory:

#### Using the MarketService
The MarketService class is your entry point to the trading functionalities. Here's how to use it:

Initialize the service:

```bash
python
from src.services.market_service import MarketService

market_service = MarketService()
```

### Record a trade:
```bash
from src.enums.trade_type import TradeType

market_service.record_trade('TEA', 100, TradeType.BUY, 150)
```

### Calculate Dividend Yield:

```bash
dividend_yield = market_service.calculate_dividend_yield('POP', 90)
print(dividend_yield)
```` 
### Calculate P/E Ratio:
```bash
pe_ratio = market_service.calculate_pe_ratio('ALE', 60)
print(pe_ratio)
```` 

### Calculate Volume Weighted Stock Price:
```bash
vwsp = market_service.calculate_volume_weighted_stock_price('ALE')
print(vwsp)
```

#### Calculate Geometric All Share Index:
```bash
all_share_index = market_service.calculate_geometric_all_share_index()
print(all_share_index)
```

## Running the Tests
This project uses unittest for testing its functionalities. Here's how to run the tests:

#### Navigate to the project root directory.

### Run the tests using:

```bash
python -m unittest discover -s tests
```







