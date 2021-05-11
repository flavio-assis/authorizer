from unittest import TestCase

from src.models.account import Account


class TestAccountRepr(TestCase):
    def setUp(self) -> None:
        self.active_card = True
        self.available_limit = 100

    def test_repr_account_initialized_with_params(self) -> None:
        account = Account(active_card=self.active_card, available_limit=self.available_limit)

        self.assertEqual(f'{account}', '{"active-card": true, "available-limit": 100}')

    def test_repr_account_initialized_without_paramsI(self) -> None:
        account = Account()
        self.assertEqual(f'{account}', '{}')

    def test_withdraw(self) -> None:
        account = Account(active_card=self.active_card, available_limit=self.available_limit)
        account.withdraw(20)
        self.assertEqual(80, account.available_limit)
