import unittest
from src.models.stock import Stock, StockType  # Adjust 'src.models' to match your project structure


class TestStock(unittest.TestCase):

    def test_init_common_stock(self):
        stock = Stock('TEA', StockType.COMMON, 8, None, 100)
        self.assertEqual(stock.symbol, 'TEA')
        self.assertEqual(stock.stock_type, StockType.COMMON)
        self.assertEqual(stock.last_dividend, 8)
        self.assertEqual(stock.fixed_dividend_percent, 0)
        self.assertEqual(stock.par_value, 100)

    def test_init_preferred_stock(self):
        stock = Stock('GIN', StockType.PREFERRED, 0, 2, 100)
        self.assertEqual(stock.symbol, 'GIN')
        self.assertEqual(stock.stock_type, StockType.PREFERRED)
        self.assertEqual(stock.last_dividend, 0)
        self.assertEqual(stock.fixed_dividend_percent,  0.02)
        self.assertEqual(stock.par_value, 100)

    def test_dividend_yield_common(self):
        stock = Stock('POP', StockType.COMMON, 8, None, 100)
        div_yield = stock.calculate_dividend_yield(90)
        self.assertAlmostEqual(div_yield, 0.08889, places=4)

    def test_dividend_yield_preferred(self):
        stock = Stock('GIN', StockType.PREFERRED, 8, 2,100)
        div_yield = stock.calculate_dividend_yield(80)
        self.assertAlmostEqual(div_yield, 0.025, places=3)

    def test_pe_ratio(self):
        stock = Stock('ALE', StockType.COMMON, 23, None, 60)
        pe_ratio = stock.calculate_pe_ratio(60)
        self.assertAlmostEqual(pe_ratio, 2.6087, places=4)

    # Add more tests as needed,  like handling edge cases (divide by zero, etc.)


if __name__ == '__main__':
    unittest.main()
