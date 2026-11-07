from dataclasses import dataclass

MAX_ORDER_NOTIONAL = 1_000_000


@dataclass(frozen=True)
class Order:
    order_id: str
    price: float
    quantity: float


def validate_order(order: Order) -> None:
    if order.price <= 0:
        raise ValueError("Price must be positive")
    if order.quantity <= 0:
        raise ValueError("Quantity must be positive")
    if order.price * order.quantity >= MAX_ORDER_NOTIONAL:
        raise ValueError("Order notional exceeds the maximum")
