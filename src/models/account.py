import json
from dataclasses import dataclass

from src.utils.logger import logger


@dataclass
class Account:
    available_limit: int = None
    active_card: bool = None

    def withdraw(self, amount):
        new_amount = self.available_limit - amount
        if new_amount < 0:
            msg = 'Negative amount is not permitted'
            logger.error(f'An error occurred when debit card amount: {msg}')
            raise Exception(msg)
        self.available_limit = new_amount

    def __repr__(self):
        if self.active_card is None and self.available_limit is None:
            return '{}'
        return json.dumps({'active-card': self.active_card, 'available-limit': self.available_limit})
