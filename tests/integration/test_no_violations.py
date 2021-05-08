import subprocess
from unittest import TestCase


class TestNoViolations(TestCase):
    def setUp(self):
        with open('./tests/integration/files/outputs/operations_no_violations', 'r') as expected_output:
            self.expected_output = expected_output.read()

    def test_account_initialized(self):
        stdout = subprocess.getoutput(
            cmd='python3 src/authorize.py ./tests/integration/files/inputs/operations_no_violations'
        )
        self.assertEqual(self.expected_output, stdout)