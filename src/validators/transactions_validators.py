from src.models import Context
from src.utils.datetime_utils import get_difftime


def account_not_initialized(context: Context) -> str or None:
    """
    Validate if account has not already been initialized.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    account = context.account
    if not account.is_active():
        return 'account-not-initialized'


def card_not_active(context: Context) -> str or None:
    """
    Validate if account has an active card.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    account = context.account
    if not account.active_card and account.is_active():
        return 'card-not-active'


def insufficient_limit(context: Context) -> str or None:
    """
    Validate if account has sufficient limit to approve the transaction.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    account = context.account
    transaction = context.transaction

    if account.is_active() and (account.available_limit - transaction.amount < 0):
        return 'insufficient-limit'


def high_frequency_small_interval(context: Context) -> str or None:
    """
    Validate if the transaction has a reasonable time difference to prevent frauds.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    transaction = context.transaction
    transactions = context.transactions
    if not transactions:
        return None
    counter = 0
    for item in range(len(transactions)):
        time_diff_in_seconds = get_difftime(transaction.time, transactions[item].time).seconds
        if time_diff_in_seconds < 180:
            counter += 1
            if counter == 3:
                return 'high-frequency-small-interval'


def double_transaction(context: Context) -> str or None:
    """
    Validate if transaction has already been processed.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    transaction = context.transaction
    transactions = context.transactions
    if not transactions:
        return None
    for item in range(len(transactions)):
        if transaction.merchant == transactions[item].merchant:
            if transaction.amount == transactions[item].amount:
                time_diff_in_seconds = get_difftime(transaction.time, transactions[item].time).seconds
                if time_diff_in_seconds < 120:
                    return 'double-transaction'
