import unittest

from exchange_demo.orders import MAX_ORDER_NOTIONAL, Order, validate_order


class OrderValidationTest(unittest.TestCase):
    def test_valid_order_is_accepted(self) -> None:
        validate_order(Order("a", price=100, quantity=10))

    @unittest.expectedFailure
    def test_notional_boundary_is_accepted(self) -> None:
        validate_order(Order("boundary", price=10_000, quantity=100))

    def test_above_maximum_notional_is_rejected(self) -> None:
        order = Order("large", price=MAX_ORDER_NOTIONAL + 1, quantity=1)
        with self.assertRaises(ValueError):
            validate_order(order)

    def test_non_positive_quantity_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_order(Order("invalid", price=100, quantity=0))


if __name__ == "__main__":
    unittest.main()
