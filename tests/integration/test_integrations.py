import os
import subprocess
from unittest import TestCase

INPUTS_DIR = './tests/integration/files/inputs/'
OUTPUTS_DIR = './tests/integration/files/outputs/'


def test_output(file_name):
    with open(os.path.join(OUTPUTS_DIR, file_name)) as output_file:
        expected_output = output_file.read()

    stdout = subprocess.getoutput(
        cmd=f'python3 src/authorizer.py < {os.path.join(INPUTS_DIR, file_name)}'
    )
    assert stdout == expected_output


class TestIntegrations(TestCase):
    def test_no_violations(self) -> None:
        file_name = 'operations_no_violations'
        test_output(file_name)

    def test_account_not_initialized(self) -> None:
        file_name = 'operations_account_not_initialized'
        test_output(file_name)

    def test_account_already_initialized(self) -> None:
        file_name = 'operations_account_already_initialized'
        test_output(file_name)

    def test_card_not_active(self) -> None:
        file_name = 'operations_card_not_active'
        test_output(file_name)

    def test_double_transaction(self) -> None:
        file_name = 'operations_double_transaction'
        test_output(file_name)

    def test_high_frequency_small_interval(self) -> None:
        file_name = 'operations_high_frequency_small_interval'
        test_output(file_name)

    def test_insufficient_limit(self) -> None:
        file_name = 'operations_insufficient_limit'
        test_output(file_name)
