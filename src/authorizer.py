import json
import sys

from src.models import Context
from src.utils.event import event_reader
from src.utils.logger import logger
from src.validators import get_violations


def authorizer(json_file) -> None:
    """
    Authorizer function
    :param json_file: input file from stdin
    """
    context = Context()

    file_lines = [line.strip() for line in json_file]

    for line in file_lines:
        json_input = json.loads(line)
        event_type, event = event_reader(json_input)

        violations = get_violations(event_type=event_type, event=event, context=context)

        if not violations:
            if event_type == 'account':
                context.account = event
            elif event_type == 'transaction':
                context.account.withdraw(event.amount)
                context.transactions.append(event)

        info_account: dict = {'account': json.loads(f'{context.account}'), 'violations': violations}
        logger.info(json.dumps(info_account))


def main():
    try:
        json_file = sys.stdin
        authorizer(json_file)
    except Exception as err:
        logger.error(f'An error occurred reading the input file: {err}')


if __name__ == '__main__':
    main()
