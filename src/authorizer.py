import json
from sys import argv

from src.models import Validator, Context
from src.utils.event import event_reader
from src.utils.logger import logger
from src.validators import VALIDATORS_MAPPER


def authorizer(json_file_path):
    context = Context()

    file_lines = [line.strip() for line in open(json_file_path)]

    for line in file_lines:
        json_input = json.loads(line)
        event_type, event = event_reader(json_input)

        validator = Validator(event_type, event, context)
        violations = validator.execute(VALIDATORS_MAPPER)

        if not violations:
            if event_type == 'account':
                context.account = event
            elif event_type == 'transaction':
                context.account.withdraw(event.amount)
                context.transactions.append(event)

        info_account: dict = {'account': json.loads(f'{context.account}'), 'violations': violations}
        logger.info(json.dumps(info_account))


def main():
    json_file_path = argv[1]
    authorizer(json_file_path)


if __name__ == '__main__':
    main()