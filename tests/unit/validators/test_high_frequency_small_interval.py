from unittest import TestCase

import src.validators as validator
from src.models import Transaction, Context


class TestHighFrequencySmallIntervalViolation(TestCase):
    def setUp(self) -> None:
        self.input1 = Context(
            transaction=Transaction(merchant='Americanas', amount=1000, time='2021-05-10T13:09:00.000Z'),
            transactions=[
                Transaction(merchant='Submarino', amount=300, time='2021-05-10T11:07:00.000Z'),
                Transaction(merchant='Magalu', amount=450, time='2021-05-10T13:07:00.000Z'),
                Transaction(merchant='Kalunga', amount=32, time='2021-05-10T13:07:40.000Z'),
                Transaction(merchant='Shoptime', amount=980, time='2021-05-10T13:08:40.000Z')
            ]
        )
        self.input2 = Context(
            transaction=Transaction(merchant='Americanas', amount=1000, time='2021-05-10T15:09:00.000Z'),
            transactions=[
                Transaction(merchant='Submarino', amount=300, time='2021-05-10T11:07:00.000Z'),
                Transaction(merchant='Magalu', amount=450, time='2021-05-10T13:07:00.000Z'),
                Transaction(merchant='Kalunga', amount=32, time='2021-05-10T13:07:40.000Z'),
                Transaction(merchant='Shoptime', amount=980, time='2021-05-10T13:08:40.000Z')
            ]
        )

    def test_high_frequency_small_interval_violation(self) -> None:
        self.assertEqual(
            'high-frequency-small-interval',
            validator.high_frequency_small_interval(self.input1)
        )

    def test_high_frequency_small_interval_no_violation(self) -> None:
        self.assertEqual(
            None,
            validator.high_frequency_small_interval(self.input2)
        )
