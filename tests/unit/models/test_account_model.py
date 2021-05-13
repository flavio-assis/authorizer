from unittest import TestCase

from src.models.account import Account


class TestAccountModel(TestCase):
    def setUp(self) -> None:
        self.id = 1
        self.active_card = True
        self.available_limit = 100

    def test_repr_account_initialized_with_params(self) -> None:
        account = Account(id=self.id, active_card=self.active_card, available_limit=self.available_limit)

        self.assertEqual(f'{account}', '{"id": 1, "active-card": true, "available-limit": 100}')

    def test_repr_account_initialized_without_paramsI(self) -> None:
        account = Account()

        self.assertEqual(f'{account}', '{}')

    def test_withdraw(self) -> None:
        account = Account(active_card=self.active_card, available_limit=self.available_limit)
        account.withdraw(20)

        self.assertEqual(80, account.available_limit)

    def test_account_is_active(self) -> None:
        account = Account(active_card=self.active_card, available_limit=self.available_limit)

        self.assertEqual(True, account.is_active())

    def test_account_is_not_active(self) -> None:
        account = Account()

        self.assertEqual(False, account.is_active())
