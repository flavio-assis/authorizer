from dataclasses import dataclass


@dataclass
class Transaction:
    merchant: str
    amount: int
    time: str
