from src.password_manager import run_password_manager
import pytest
from unittest.mock import patch
import os
import boto3
from moto import mock_aws


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


class TestRunProcessManager:

    @mock_aws
    def test_funct_triggers_get_user_choice_with_error_and_exits(self, capsys):
        with patch("builtins.input", side_effect=["t", "x"]):
            client = boto3.client("secretsmanager", region_name='eu-west-2')
            run_password_manager(client)
            captured = capsys.readouterr()
            assert captured.out == "invalid input.\nThank you, Goodbye!\n"

    @mock_aws
    def test_funct_doesnt_get_trapped_in_recursion(self, capsys):
        with patch("builtins.input", side_effect=["t", "t", "p", "x"]):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert (
                captured.out
                == "invalid input.\ninvalid input.\ninvalid input.\nThank you, Goodbye!\n"
            )

    @mock_aws
    def test_funct_triggers_list_secrets(self, capsys):
        with patch("builtins.input", side_effect=["l", "x"]):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert captured.out == "0 secrets stored\nThank you, Goodbye!\n"

    @mock_aws
    def test_funct_triggers_list_multiple_secrets(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "e",
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "e",
                "Secret_2",
                "starmer",
                "mypass",
                "l",
                "x",
            ],
        ):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert (
                captured.out
                == "Secret saved!\nSecret saved!\n2 secrets stored\nThank you, Goodbye!\n"
            )

    @mock_aws
    def test_funct_triggers_entry(self, capsys):
        with patch(
            "builtins.input",
            side_effect=["e", "Missile_Launch_Codes", "bidenj", "Pa55word", "x"],
        ):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert captured.out == "Secret saved!\nThank you, Goodbye!\n"

    @mock_aws
    def test_funct_triggers_retrieve(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "e",
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "r",
                "Missile_Launch_Codes",
                "x",
            ],
        ):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert (
                captured.out
                == "Secret saved!\nMissile_Launch_Codes stored in local file secrets.txt\nThank you, Goodbye!\n"
            )

    @mock_aws
    def test_funct_triggers_delete(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "e",
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "d",
                "Missile_Launch_Codes",
                "x",
            ],
        ):
            client = boto3.client("secretsmanager")
            run_password_manager(client)
            captured = capsys.readouterr()
            assert (
                captured.out
                == "Secret saved!\nMissile_Launch_Codes successfully deleted\nThank you, Goodbye!\n"
            )
