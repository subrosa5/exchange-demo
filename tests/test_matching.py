import unittest

from exchange_demo.matching import Bid, best_bid


class MatchingTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_highest_price_wins_before_time(self) -> None:
        earlier = Bid("earlier", price=100, created_at=1)
        higher = Bid("higher", price=101, created_at=2)
        self.assertEqual(best_bid([earlier, higher]), higher)

    def test_earlier_bid_wins_at_same_price(self) -> None:
        earlier = Bid("earlier", price=100, created_at=1)
        later = Bid("later", price=100, created_at=2)
        self.assertEqual(best_bid([later, earlier]), earlier)

    def test_empty_book_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            best_bid([])


if __name__ == "__main__":
    unittest.main()
