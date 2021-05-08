from datetime import datetime


def get_datetime(date_str: str):
    return datetime.fromisoformat(date_str.replace('Z', '+00:00'))


def get_difftime(date_str1: str, date_str2: str):
    datetime1 = get_datetime(date_str1)
    datetime2 = get_datetime(date_str2)

    return datetime1 - datetime2
