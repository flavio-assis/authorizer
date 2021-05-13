from src.models import Context


def account_already_initialized(context: Context) -> str or None:
    """
    Validate if account has already been initialized.
    :param context: Context object for the session
    :return: violation message
    :rtype: str
    """
    account = context.account
    if account.is_active():
        return 'account-already-initialized'
