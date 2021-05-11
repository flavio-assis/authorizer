from unittest import TestCase
from src import validator
from src.models.account import Account


class TesAccountNotInitializedViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Account()
        self.input2 = Account(active_card=True, available_limit=100)

    def test_account_not_initialized_violation(self) -> None:
        self.assertEqual('account-not-initialized', validator.account_not_initialized(self.input1))

    def test_account_not_initialized_no_violation(self) -> None:
        self.assertEqual(None, validator.account_not_initialized(self.input2, ))
