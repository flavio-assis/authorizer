import os
from logging import getLogger, StreamHandler

from typing import List

from src.models.account import Account
from src.models.transaction import Transaction
from src.utils.datetime_utils import get_difftime

logger = getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))
logger.addHandler(StreamHandler())


def account_already_initialized(account: Account) -> str or None:
    if account.active_card is not None and account.available_limit is not None:
        return 'account-already-initialized'


def account_not_initialized(account: Account) -> str or None:
    if account.active_card is None and account.available_limit is None:
        return 'account-not-initialized'


def card_not_active(account: Account) -> str or None:
    if not account.active_card:
        return 'card-not-active'


def insufficient_limit(account: Account, transaction: Transaction) -> str or None:
    if account.available_limit - transaction.amount < 0:
        return 'insufficient-limit'


def high_frequency_small_interval(transaction: Transaction, transactions: List[Transaction]) -> str or None:
    if not transactions:
        return None

    counter = 0
    for item in range(len(transactions)):
        if get_difftime(transaction.time, transactions[item].time).seconds < 180:
            counter += 1
            if counter == 3:
                return 'high-frequency-small-interval'


def double_transaction(transaction: Transaction, transactions: List[Transaction]) -> str or None:
    if not transactions:
        return None

    for item in range(len(transactions)):
        if transaction.merchant == transactions[item].merchant:
            if transaction.amount == transactions[item].amount:
                if get_difftime(transaction.time, transactions[item].time).seconds < 120:
                    return 'double-transaction'


class Validator:
    def __init__(self, func=None):
        if func is not None:
            self.execute = func
        else:
            logger.error(f'execution method must be implemented by the strategy')

    def execute(self) -> None:
        pass
