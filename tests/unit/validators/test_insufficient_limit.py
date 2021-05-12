from unittest import TestCase

import src.validators as validator
from src.models import Account, Context
from src.models.transaction import Transaction


class TestInsufficientLimitViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Context(
            account=Account(active_card=True, available_limit=100),
            transaction=Transaction(merchant='Outback', amount=300, time='2021-05-10T11:07:00.000Z')
        )
        self.input2 = Context(
            account=Account(active_card=True, available_limit=400),
            transaction=Transaction(merchant='Outback', amount=300, time='2021-05-10T11:07:00.000Z')
        )

    def test_insufficient_limit_violation(self) -> None:
        self.assertEqual(
            'insufficient-limit',
            validator.insufficient_limit(self.input1)
        )

    def test_insufficient_limit_no_violation(self) -> None:
        self.assertEqual(
            None,
            validator.insufficient_limit(self.input2)
        )
