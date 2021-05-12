from src.models import Context


def account_already_initialized(context: Context) -> str or None:
    account = context.account
    if account.active_card is not None and account.available_limit is not None:
        return 'account-already-initialized'
