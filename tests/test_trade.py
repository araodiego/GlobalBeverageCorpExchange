import unittest
from src.models.trade import Trade
from src.enums.trade_type import TradeType


class TestTrade(unittest.TestCase):
    def setUp(self):
        self.trade = Trade('TEA', 100, TradeType.BUY, 120)

    def test_trade_creation(self):
        self.assertEqual(self.trade.stock_symbol, 'TEA')
        self.assertEqual(self.trade.quantity, 100)
        self.assertEqual(self.trade.trade_type, TradeType.BUY)
        self.assertEqual(self.trade.price, 120)


if __name__ == '__main__':
    unittest.main()
