from src.models import Context
from src.utils.datetime_utils import get_difftime


def account_not_initialized(context: Context) -> str or None:
    account = context.account
    if account.active_card is None and account.available_limit is None:
        return 'account-not-initialized'


def card_not_active(context: Context) -> str or None:
    account = context.account
    if not account.active_card:
        return 'card-not-active'


def insufficient_limit(context: Context) -> str or None:
    account = context.account
    transaction = context.transaction
    if account.available_limit - transaction.amount < 0:
        return 'insufficient-limit'


def high_frequency_small_interval(context: Context) -> str or None:
    transaction = context.transaction
    transactions = context.transactions
    if not transactions:
        return None
    counter = 0
    for item in range(len(transactions)):
        if get_difftime(transaction.time, transactions[item].time).seconds < 180:
            counter += 1
            if counter == 3:
                return 'high-frequency-small-interval'


def double_transaction(context: Context) -> str or None:
    transaction = context.transaction
    transactions = context.transactions
    if not transactions:
        return None
    for item in range(len(transactions)):
        if transaction.merchant == transactions[item].merchant:
            if transaction.amount == transactions[item].amount:
                if get_difftime(transaction.time, transactions[item].time).seconds < 120:
                    return 'double-transaction'
