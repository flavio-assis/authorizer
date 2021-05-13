from src.models import Validator
from src.validators.account_validators import *
from src.validators.transactions_validators import *
from collections.abc import Callable
from typing import Optional

VALIDATORS_MAPPER: dict[str, list[Callable]] = {
    'account': [account_already_initialized],
    'transaction': [
        account_not_initialized,
        card_not_active,
        insufficient_limit,
        high_frequency_small_interval,
        double_transaction
    ]
}


def get_violations(validators: Optional[dict[str, list[Callable]]] = None, **kwargs) -> list[str]:
    """
    Get violations running the validator class.
    :param validators: Mapper with the event type and callables to validate
    :type validators: dict[str, list[Callable]]
    :param kwargs: Validators params
    :return: List of violations
    :rtype: list[str]
    """
    if not validators:
        validators = VALIDATORS_MAPPER
    validator = Validator(**kwargs)
    violations = validator.execute(validators)
    return violations
