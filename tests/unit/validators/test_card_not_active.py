from unittest import TestCase

import src.validators as validator
from src.models import Account, Context


class TestCardNotActiveViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Context(account=Account(active_card=False, available_limit=100))
        self.input2 = Context(account=Account(active_card=True, available_limit=100))

    def test_card_not_active_violation(self) -> None:
        self.assertEqual('card-not-active', validator.card_not_active(self.input1))

    def test_card_not_active_no_violation(self) -> None:
        self.assertEqual(None, validator.card_not_active(self.input2))
