from unittest import TestCase

from src.models import Transaction


class TestTransactionModel(TestCase):
    def setUp(self) -> None:
        self.transaction = Transaction(merchant='King', amount=10,time='2020-12-01T11:07:00.000Z')

    def test_initialization(self):
        self.assertEqual(
            ['King', 10, '2020-12-01T11:07:00.000Z'],
            [self.transaction.merchant, self.transaction.amount, self.transaction.time]
        )
