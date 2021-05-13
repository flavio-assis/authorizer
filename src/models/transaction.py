from dataclasses import dataclass


@dataclass
class Transaction:
    """
    Transaction model used o implement an event of type transaction
    """
    merchant: str = None
    amount: int = None
    time: str = None
