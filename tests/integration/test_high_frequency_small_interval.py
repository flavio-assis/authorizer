import subprocess
from unittest import TestCase


class TestHighFrequencySmallInterval(TestCase):
    def setUp(self):
        with open('./tests/integration/files/outputs/operations_high_frequency_small_interval', 'r') as expected_output:
            self.expected_output = expected_output.read()

    def test_account_initialized(self):
        stdout = subprocess.getoutput(
            cmd='python3 src/authorize.py ./tests/integration/files/inputs/operations_high_frequency_small_interval'
        )
        self.assertEqual(self.expected_output, stdout)