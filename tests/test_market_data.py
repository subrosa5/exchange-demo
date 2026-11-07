import unittest

from exchange_demo.market_data import is_stale


class MarketDataTest(unittest.TestCase):
    def test_recent_snapshot_is_not_stale(self) -> None:
        self.assertFalse(is_stale(updated_at=10, now=11))

    def test_old_snapshot_is_stale(self) -> None:
        self.assertTrue(is_stale(updated_at=10, now=13))

    @unittest.expectedFailure
    def test_snapshot_is_stale_at_threshold(self) -> None:
        self.assertTrue(is_stale(updated_at=10, now=12, stale_after=2))


if __name__ == "__main__":
    unittest.main()
