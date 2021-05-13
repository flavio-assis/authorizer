from datetime import datetime, timedelta


def get_datetime(date_str: str) -> datetime:
    """
    Conversor for date strings with suffix Z
    :param date_str: date string
    :type date_str: str
    :return: datetime for string input
    :rtype: datetime
    """
    return datetime.fromisoformat(date_str.replace('Z', '+00:00'))


def get_difftime(date_str1: str, date_str2: str) -> timedelta:
    """
    Get difference between two date strings
    :param date_str1: first date string
    :param date_str2: second date string
    :return: difference between first and second date strings in timedelta
    :rtype: timedelta
    """
    datetime1 = get_datetime(date_str1)
    datetime2 = get_datetime(date_str2)

    return datetime1 - datetime2
