from dataclasses import dataclass


@dataclass
class Transaction:
    merchant: str = None
    amount: int = None
    time: str = None
