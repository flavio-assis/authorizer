from unittest import TestCase

from src.models.account import Account


class TestAccountRepr(TestCase):
    def setUp(self) -> None:
        self.active_card = True
        self.available_limit = 100

    def test_repr(self):
        account = Account(active_card=self.active_card, available_limit=self.available_limit)

        self.assertEqual(f'{account}', '{"active-card": true, "available-limit": 100}')
