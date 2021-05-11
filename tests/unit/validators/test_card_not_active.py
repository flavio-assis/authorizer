from unittest import TestCase
from src import validator
from src.models.account import Account


class TestCardNotActiveViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Account(active_card=False, available_limit=100)
        self.input2 = Account(active_card=True, available_limit=100)

    def test_card_not_active_violation(self) -> None:
        self.assertEqual('card-not-active', validator.card_not_active(self.input1))

    def test_card_not_active_no_violation(self) -> None:
        self.assertEqual(None, validator.card_not_active(self.input2))
