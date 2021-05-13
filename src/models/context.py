from typing import Optional

from src.models import Account, Transaction


class Context:
    def __init__(
            self,
            account: Account = Account(),
            transaction: Transaction = Transaction(),
            transactions: Optional[list] = None
    ):
        """
        Context model, used to define the current context in the application
        :param account: Account object
        :type account: Account
        :param transaction: Transaction object
        :type transaction: Transaction
        :param transactions: list of transactions
        :type transactions: list
        """
        if transactions is None:
            transactions = []
        self.account = account
        self.transaction = transaction
        self.transactions = transactions
