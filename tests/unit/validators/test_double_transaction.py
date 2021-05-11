from unittest import TestCase
from src import validator
from src.models.transaction import Transaction


class TestDoubleTransactionViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = {
            'transaction': Transaction(merchant='Apple', amount=30000, time='2021-05-10T11:07:00.000Z'),
            'transactions': [
                Transaction(merchant='Apple', amount=30000, time='2021-05-10T11:07:00.000Z'),
                Transaction(merchant='Apple', amount=30000, time='2021-05-10T11:07:40.000Z')
            ]
        }
        self.input2 = {
            'transaction': Transaction(merchant='Apple', amount=30000, time='2021-05-10T11:07:00.000Z'),
            'transactions': [
                Transaction(merchant='Apple', amount=30000, time='2020-12-01T11:07:30.000Z'),
                Transaction(merchant='Samsung', amount=20000, time='2020-12-01T11:08:00.000Z')
            ]
        }

    def test_double_transaction_violation(self) -> None:
        self.assertEqual(
            'double-transaction',
            validator.double_transaction(self.input1.get('transaction'), self.input1.get('transactions'))
        )

    def test_double_transaction_no_violation(self) -> None:
        self.assertEqual(
            None,
            validator.double_transaction(self.input2.get('transaction'), self.input2.get('transactions'))
        )
