from src.models.account import Account
from src.models.context import Context
from src.models.transaction import Transaction


class Validator:
    def __init__(
            self,
            event_type: str,
            event: Account or Transaction,
            context: Context
    ):
        self.event = event
        self.context = context
        self.event_type = event_type
        self.violations = []
        self._update_context()

    def _update_context(self) -> None:
        if self.event_type == 'transaction':
            self.context.transaction = self.event

    def execute(self, validators: dict) -> list[str]:
        for validator in validators.get(self.event_type):
            violation = validator(self.context)
            if violation == 'account-not-initialized':
                return [violation]

            self.violations.append(violation) if violation is not None else []
        return self.violations
