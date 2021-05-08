import json
from dataclasses import dataclass


@dataclass
class Account:
    available_limit: int
    active_card: bool

    def withdraw(self, amount):
        self.available_limit = self.available_limit - amount

    def __repr__(self):
        return json.dumps({'active-card': self.active_card, 'available-limit': self.available_limit})
