from unittest import TestCase

from src.models import Context, Account, Transaction
from src.validators import get_violations


def foo(*argv) -> None:
    return 'foo-violation'


class TestGetViolations(TestCase):
    def setUp(self) -> None:
        self.event_type = 'account'
        self.validators = {
            'account': [foo]
        }
        self.event = Account(active_card=True, available_limit=100)
        self.context = Context(account=Account(), transaction=Transaction(), transactions=[])

    def test_get_violations(self):
        violations = get_violations(
            validators=self.validators,
            event_type=self.event_type,
            event=self.event,
            context=self.context
        )
        self.assertEqual(['foo-violation'], violations)
