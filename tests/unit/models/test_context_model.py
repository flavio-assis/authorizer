from unittest import TestCase

from src.models import Context, Account, Transaction


class TestContextModel(TestCase):
    def setUp(self) -> None:
        self.account = Account(active_card=True, available_limit=1000)
        self.transaction = Transaction(merchant='King', amount=10,time='2020-12-01T11:07:00.000Z')
        self.context = Context(account=self.account, transaction=self.transaction, transactions=[])

    def test_initialization(self):
        self.assertEqual(
            [self.account, self.transaction, []],
            [self.context.account, self.context.transaction, self.context.transactions]
        )
