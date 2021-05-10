import os
from logging import getLogger, StreamHandler

from src.utils.datetime_utils import get_difftime

logger = getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))
logger.addHandler(StreamHandler())


def account_already_initialized(account):
    if account != {}:
        return 'account-already-initialized'

def account_not_initialized(account):
    if account == {}:
        return 'account-not-initialized'


def card_not_active(account):
    if not account.active_card:
        return 'card-not-active'
    return None


def insufficient_limit(account, transaction):
    if account.available_limit - transaction.amount < 0:
        return 'insufficient-limit'
    return None


def high_frequency_small_interval(transaction, transactions):
    if not transactions:
        return None

    counter = 0
    for item in range(len(transactions)):
        if get_difftime(transaction.time, transactions[item].time).seconds < 180:
            counter += 1
            if counter == 3:
                return 'high-frequency-small-interval'

    return None


def double_transaction(transaction, transactions):
    if not transactions:
        return None

    for item in range(len(transactions)):
        if transaction.merchant == transactions[item].merchant:
            if transaction.amount == transactions[item].amount:
                if get_difftime(transaction.time, transactions[item].time).seconds < 120:
                    return 'double-transaction'
    return None


class Validator:
    def __init__(self, func=None):
        if func is not None:
            self.execute = func
            self.name = f'{self.__class__.__name__}_{func.__name__}'
        else:
            self.name = f'{self.__class__.__name__}_default'

    def execute(self):
        logger.info(f'Default method: {self.name}')
