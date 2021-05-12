from src.models.context import Context


def find_account(account_id: int, context_list: list[Context]) -> Context:
    for context in context_list:
        if account_id == context.account.id:
            return context
    return Context()
