from src.models import Context


def account_already_initialized(context: Context) -> str or None:
    account = context.account
    if account.is_active():
        return 'account-already-initialized'
