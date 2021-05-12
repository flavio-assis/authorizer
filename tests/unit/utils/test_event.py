from unittest import TestCase

from src.models import Account, Transaction
from src.utils.event import event_reader


class TestEventUtils(TestCase):
    def setUp(self) -> None:
        self.account_dict = {
            "account": {
                "active-card": True,
                "available-limit": 225
            }
        }
        self.transaction_dict = {
            "transaction": {
                "merchant": "Uber Eats",
                "amount": 25,
                "time": "2020-12-01T11:07:00.000Z"
            }
        }

    def test_event_reader_account(self):
        expected_event_type = 'account'
        expected_event = Account(
            active_card=True,
            available_limit=225
        )
        self.assertEqual((expected_event_type, expected_event), event_reader(self.account_dict))

    def test_event_reader_transaction(self):
        expected_event_type = 'transaction'
        expected_event = Transaction(
            merchant='Uber Eats',
            amount=25,
            time='2020-12-01T11:07:00.000Z'
        )
        self.assertEqual((expected_event_type, expected_event), event_reader(self.transaction_dict))
