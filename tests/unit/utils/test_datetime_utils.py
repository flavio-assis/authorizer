from datetime import datetime, timedelta, timezone
from unittest import TestCase

from src.utils.datetime_utils import get_datetime, get_difftime


class TestDateTimeUtils(TestCase):
    def setUp(self) -> None:
        self.datetime_str1 = '2020-12-01T11:07:00.000Z'
        self.datetime_str2 = '2020-12-01T11:08:00.000Z'

    def test_get_datetime(self):
        expeted_datetime = datetime(year=2020, month=12, day=1, hour=11, minute=7, tzinfo=timezone.utc)
        self.assertEqual(expeted_datetime, get_datetime(self.datetime_str1))

    def test_get_difftime(self):
        expected_difftime = timedelta(seconds=60)
        self.assertEqual(expected_difftime, get_difftime(self.datetime_str2, self.datetime_str1))
