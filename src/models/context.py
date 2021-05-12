from src.models.account import Account
from src.models.transaction import Transaction


class Context:
    def __init__(
            self,
            account: Account = Account(),
            transaction: Transaction = Transaction(),
            transactions=None
    ):
        if transactions is None:
            transactions = []
        self.account = account
        self.transaction = transaction
        self.transactions = transactions
