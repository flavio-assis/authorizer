from collections.abc import Callable

from src.models.account import Account
from src.models.context import Context
from src.models.transaction import Transaction


class Validator:
    def __init__(self, event_type: str, event: Account or Transaction, context: Context):
        """
        Validator Model
        :param event_type: Event type, must be `account` or ``transaction`
        :type event_type: str
        :param event: Account or Transaction object, must match the event_type
        :type event: Account or Transaction
        :param context: Context object of the session
        :type context: Context
        """
        self.event = event
        self.context = context
        self.event_type = event_type
        self.violations = []
        self._update_context()

    def _update_context(self) -> None:
        if self.event_type == 'transaction':
            self.context.transaction = self.event

    def execute(self, validators: dict[str, list[Callable]]) -> list[str]:
        """
        Execute the validators passed on the input
        :param validators: must be a dict representing which validators to run for each event_type
            Example:
                {
                    'account': [account_already_initialized],
                    'transaction': [account_not_initialized]
                }
        :type validators: dict[str, list[Callable]]
        :return: List of violations
        :rtype: list[str]
        """
        for validator in validators.get(self.event_type):
            violation = validator(self.context)
            self.violations.append(violation) if violation is not None else []
        return self.violations
