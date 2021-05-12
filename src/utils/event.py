from src.models import Account, Transaction
from src.utils.logger import logger


def event_reader(event: dict):
    if 'account' in event.keys():
        account = Account(
            id=event.get('account').get('id'),
            available_limit=event.get('account').get('available-limit'),
            active_card=event.get('account').get('active-card')
        )
        return 'account', account

    elif 'transaction' in event.keys():
        transaction = Transaction(
            merchant=event.get('transaction').get('merchant'),
            amount=event.get('transaction').get('amount'),
            time=event.get('transaction').get('time'),
            account_id=event.get('transaction').get('account-id')
        )
        return 'transaction', transaction

    else:
        msg = 'Unrecognizable event'
        logger.error(msg)
        raise Exception(msg)
