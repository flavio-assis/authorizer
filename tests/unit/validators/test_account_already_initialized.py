from unittest import TestCase

import src.validators as validator
from src.models import Account, Context


class TesAccountAlreadyInitializedViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Context(account=Account(active_card=True, available_limit=100))
        self.input2 = Context(account=Account())

    def test_account_already_initialized_violation(self) -> None:
        self.assertEqual('account-already-initialized', validator.account_already_initialized(self.input1))

    def test_account_already_initialized_no_violation(self) -> None:
        self.assertEqual(None, validator.account_already_initialized(self.input2))
