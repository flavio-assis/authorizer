from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    merchant: str
    amount: int
    time: datetime
