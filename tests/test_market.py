import unittest

from src.enums.trade_type import TradeType
from src.services.market_service import MarketService


class TestMarket(unittest.TestCase):
    def setUp(self):
        self.market = MarketService()

    def test_record_trade(self):
        self.market.record_trade('TEA', 100, TradeType.BUY, 150)
        self.assertEqual(len(self.market.trades), 1)

    def test_record_trade_no_symbol(self):
        with self.assertRaises(ValueError):
            self.market.record_trade('AAPL', 100, TradeType.BUY, 150)

    def test_calculate_dividend_yield_common(self):
        div_yield = self.market.calculate_dividend_yield("POP", 90)
        self.assertAlmostEqual(div_yield, 0.08889, places=4)

    def test_calculate_dividend_yield_preferred(self):
        div_yield = self.market.calculate_dividend_yield("GIN", 80)
        self.assertAlmostEqual(div_yield, 0.025, places=3)

    def test_calculate_dividend_yield_no_symbol(self):
        with self.assertRaises(ValueError):
            self.market.calculate_dividend_yield('AAPL', 100)

    def test_calculate_pe_ratio(self):
        pe_ratio = self.market.calculate_pe_ratio('ALE', 60)
        self.assertAlmostEqual(pe_ratio, 2.6087, places=4, msg='P/E ratio calculation did not match expected value')

    def test_calculate_volume_weighted_stock_price_valid_symbol(self):
        self.market.record_trade('ALE', 100, TradeType.BUY, 100)
        self.market.record_trade('ALE', 100, TradeType.SELL, 120)
        result_vwsp = self.market.calculate_volume_weighted_stock_price('ALE')

        # The expected VWSP is calculated manually based on the sample data
        expected_vwsp = (100 * 100 + 120 * 100 ) / (100 + 100)

        self.assertEqual(result_vwsp, expected_vwsp, msg='VWSP calculation did not match expected value')

    def test_calculate_geometric_all_share_index(self):
        self.market.record_trade('ALE', 100, TradeType.BUY, 100)
        self.market.record_trade('ALE', 100, TradeType.SELL, 120)
        self.market.record_trade('POP', 100, TradeType.BUY, 100)
        self.market.record_trade('GIN', 100, TradeType.SELL, 120)

        # Calculate VWSP for each stock symbol manually
        vwsp_ale = ((100 * 100 + 120 * 100 ) / (100 + 100))
        vwsp_pop = ((100 * 100) / (100))
        vwsp_gin= ((120 * 100) / (100))

        # Calculate the expected geometric mean of VWSPs manually
        expected_index = (vwsp_ale * vwsp_pop * vwsp_gin) ** (1 / 3)
        print('Expected Index: ', round(expected_index, 4))

        geomean = self.market.calculate_geometric_all_share_index()
        print('Real Index: ', round(geomean, 4))

        self.assertEqual(round(geomean, 4), round(expected_index, 4), msg='Geometric all share index is incorrect')

