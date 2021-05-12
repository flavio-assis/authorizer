from unittest import TestCase

from src.models import Validator, Transaction, Context


def foo(context):
    return 'executed'


class TestValidatorModel(TestCase):
    def setUp(self) -> None:
        self.event_type = 'transaction'
        self.event = Transaction(
            merchant='Rappi',
            amount=10,
            time='2020-12-01T11:07:00.000Z'
        )
        self.context = Context()

    def test_update_context(self):
        validator = Validator(self.event_type, self.event, Context())
        self.assertEqual(self.event, validator.context.transaction)

    def test_execute_validator(self):
        validator = Validator(self.event_type, self.event, Context())
        violations = validator.execute({'transaction': [foo]})

        self.assertEqual(violations, ['executed'])
