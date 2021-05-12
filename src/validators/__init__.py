from src.validators.account_validators import *
from src.validators.transactions_validators import *

VALIDATORS_MAPPER = {
    'account': [account_already_initialized],
    'transaction': [
        account_not_initialized,
        card_not_active,
        insufficient_limit,
        high_frequency_small_interval,
        double_transaction
    ]
}
