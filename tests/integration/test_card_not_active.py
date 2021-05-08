import subprocess
from unittest import TestCase


class TestCardNotActive(TestCase):
    def setUp(self):
        with open('./tests/integration/files/outputs/operations_card_not_active', 'r') as expected_output:
            self.expected_output = expected_output.read()

    def test_account_initialized(self):
        stdout = subprocess.getoutput(
            cmd='python3 src/authorize.py ./tests/integration/files/inputs/operations_card_not_active'
        )
        self.assertEqual(self.expected_output, stdout)