from dataclasses import dataclass


@dataclass(frozen=True)
class Bid:
    order_id: str
    price: float
    created_at: float


def best_bid(bids: list[Bid]) -> Bid:
    if not bids:
        raise ValueError("At least one bid is required")
    return min(bids, key=lambda bid: bid.created_at)
