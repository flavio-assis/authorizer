import json
import os
from logging import getLogger, StreamHandler
from sys import argv

from models.account import Account
from models.transaction import Transaction
from validador import (
    Validador,
    card_not_active,
    insufficient_limit,
    high_frequency_small_interval,
    double_transaction
)

logger = getLogger(__name__)
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))
logger.addHandler(StreamHandler())


def authorize():
    with open(argv[1]) as file:
        account = {}
        transactions = []
        for line in file:
            violations = []
            json_input = json.loads(line)

            if json_input.get('account'):
                if account == {}:
                    account = Account(
                        available_limit=json_input.get('account').get('available-limit'),
                        active_card=json_input.get('account').get('active-card')
                    )
                else:
                    violations.append('account-already-initialized')

            elif json_input.get('transaction'):
                if account == {}:
                    violations.append('account-not-initialized')
                else:
                    transaction = Transaction(
                        merchant=json_input.get('transaction').get('merchant'),
                        amount=json_input.get('transaction').get('amount'),
                        time=json_input.get('transaction').get('time')
                    )

                    violation_inactive_card = Validador(func=card_not_active)
                    v0 = violation_inactive_card.execute(account)
                    violations.append(v0) if v0 is not None else []

                    violation_limit = Validador(func=insufficient_limit)
                    v1 = violation_limit.execute(account, transaction)
                    violations.append(v1) if v1 is not None else []

                    violation_double_transaction = Validador(func=double_transaction)
                    v2 = violation_double_transaction.execute(transaction, transactions)
                    violations.append(v2) if v2 is not None else []

                    violation_high_frequency = Validador(func=high_frequency_small_interval)
                    v3 = violation_high_frequency.execute(transaction, transactions)
                    violations.append(v3) if v3 is not None else []

                    if not violations:
                        account.withdraw(transaction.amount)
                        transactions.append(transaction)

            info_account: dict = {'account': json.loads(f'{account}'), 'violations': violations}
            logger.info(json.dumps(info_account))


if __name__ == '__main__':
    authorize()