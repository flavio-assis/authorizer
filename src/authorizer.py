import json
from sys import argv

from src.models.account import Account
from src.models.transaction import Transaction
from src.utils.logger import logger
from src.validator import (
    Validator,
    account_already_initialized,
    account_not_initialized,
    card_not_active,
    insufficient_limit,
    high_frequency_small_interval,
    double_transaction
)


def authorizer(json_file_path):
    account = Account()
    transactions = []

    file_lines = [line.strip() for line in open(json_file_path)]

    for line in file_lines:
        json_input = json.loads(line)
        violations = []

        if json_input.get('account'):
            violation_account_already_initialized = Validator(func=account_already_initialized)
            v0 = violation_account_already_initialized.execute(account)
            if v0 is not None:
                violations.append(v0)
            else:
                account = Account(
                    available_limit=json_input.get('account').get('available-limit'),
                    active_card=json_input.get('account').get('active-card')
                )

        elif json_input.get('transaction'):
            violation_account_not_initialized = Validator(func=account_not_initialized)
            v1 = violation_account_not_initialized.execute(account)
            if v1 is not None:
                violations.append(v1)
            else:
                transaction = Transaction(
                    merchant=json_input.get('transaction').get('merchant'),
                    amount=json_input.get('transaction').get('amount'),
                    time=json_input.get('transaction').get('time')
                )

                violation_inactive_card = Validator(func=card_not_active)
                v2 = violation_inactive_card.execute(account)
                violations.append(v2) if v2 is not None else []

                violation_limit = Validator(func=insufficient_limit)
                v3 = violation_limit.execute(account, transaction)
                violations.append(v3) if v3 is not None else []

                violation_double_transaction = Validator(func=double_transaction)
                v4 = violation_double_transaction.execute(transaction, transactions)
                violations.append(v4) if v4 is not None else []

                violation_high_frequency = Validator(func=high_frequency_small_interval)
                v5 = violation_high_frequency.execute(transaction, transactions)
                violations.append(v5) if v5 is not None else []

                if not violations:
                    account.withdraw(transaction.amount)
                    transactions.append(transaction)
        info_account: dict = {'account': json.loads(f'{account}'), 'violations': violations}
        logger.info(json.dumps(info_account))


def main():
    json_file_path = argv[1]
    authorizer(json_file_path)


if __name__ == '__main__':
    main()
