from unittest import TestCase

import src.validators as validator
from src.models import Account, Context


class TesAccountNotInitializedViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Context(account=Account())
        self.input2 = Context(Account(active_card=True, available_limit=100))

    def test_account_not_initialized_violation(self) -> None:
        self.assertEqual('account-not-initialized', validator.account_not_initialized(self.input1))

    def test_account_not_initialized_no_violation(self) -> None:
        self.assertEqual(None, validator.account_not_initialized(self.input2, ))
