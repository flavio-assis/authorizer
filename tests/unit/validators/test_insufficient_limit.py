from unittest import TestCase
from src import validator
from src.models.transaction import Transaction
from src.models.account import Account


class TestInsufficientLimitViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = {
            'account': Account(active_card=True, available_limit=100),
            'transaction': Transaction(merchant='Outback', amount=300, time='2021-05-10T11:07:00.000Z')
        }
        self.input2 = {
            'account': Account(active_card=True, available_limit=400),
            'transaction': Transaction(merchant='Outback', amount=300, time='2021-05-10T11:07:00.000Z')
        }

    def test_insufficient_limit_violation(self) -> None:
        self.assertEqual(
            'insufficient-limit',
            validator.insufficient_limit(account=self.input1.get('account'), transaction=self.input1.get('transaction'))
        )

    def test_insufficient_limit_no_violation(self) -> None:
        self.assertEqual(
            None,
            validator.insufficient_limit(account=self.input2.get('account'), transaction=self.input2.get('transaction'))
        )
