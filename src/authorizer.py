import json
from sys import argv

from src.models.context import Context
from src.utils.event import event_reader
from src.utils.logger import logger
from src.validators import get_violations
from src.utils.find_account import find_account


def authorizer(json_file_path):
    context_list = []

    file_lines = [line.strip() for line in open(json_file_path)]

    for line in file_lines:
        json_input = json.loads(line)
        event_type, event = event_reader(json_input)

        account_id = event.id if event_type == 'account' else event.account_id

        context = find_account(account_id, context_list)

        violations = get_violations(event_type=event_type, event=event, context=context)

        if not violations:
            if event_type == 'account':
                context.account = event
            elif event_type == 'transaction':
                context.account.withdraw(event.amount)
                context.transactions.append(event)

            context_list.append(context)

        info_account: dict = {'account': json.loads(f'{context.account}'), 'violations': violations}
        logger.info(json.dumps(info_account))


def main():
    json_file_path = argv[1]
    authorizer(json_file_path)


if __name__ == '__main__':
    main()
