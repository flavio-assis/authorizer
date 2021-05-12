import json
from dataclasses import dataclass

from src.utils.logger import logger


@dataclass
class Account:
    available_limit: int = None
    active_card: bool = None

    def withdraw(self, amount: int):
        """
        Update the available_limit in the credit card
        :param amount: Amount to be decremented
        :type amount: int
        """
        new_amount = self.available_limit - amount
        if new_amount < 0:
            msg = 'Negative amount is not permitted'
            logger.error(f'An error occurred when debit card amount: {msg}')
            raise Exception(msg)
        self.available_limit = new_amount

    def is_active(self) -> bool:
        """
        Check whether the account is active ir not
        :return: If the acount is active, returns True, if not active, returns false
        :rtype: bool
        """
        if self.active_card is not None and self.available_limit is not None:
            return True
        else:
            return False

    def __repr__(self):
        if not self.is_active():
            return '{}'
        return json.dumps({'active-card': self.active_card, 'available-limit': self.available_limit})
