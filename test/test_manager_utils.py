from utils.manager_utils import get_user_choice, entry
import pytest
from unittest.mock import patch, Mock
import boto3
from moto import mock_aws
import os


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


class TestGetUserChoice:

    @pytest.mark.parametrize("user_input", ["l", "e", "r", "d", "x"])
    def test_function_returns_choice_for_valid_choice(self, user_input):
        with patch("builtins.input", return_value=user_input):
            result = get_user_choice()
            assert result == user_input

    @pytest.mark.parametrize("user_input", ["a", "t", "!", " ", "X"])
    def test_function_returns_invalid_for_invalid_choice(self, user_input, capsys):
        with patch("builtins.input", return_value=user_input):
            result = get_user_choice()
            captured = capsys.readouterr()
            assert captured.out == "invalid input.\n"
            assert result == "invalid"


class TestEntry:

    @mock_aws
    def test_entry_uploads_secret_to_secretsmanager(self, capsys):
        with patch(
            "builtins.input", side_effect=["Missile_Launch_Codes", "bidenj", "Pa55word"]
        ):
            client = boto3.client("secretsmanager")
            entry(client)
            response = client.get_secret_value(SecretId="Missile_Launch_Codes")
            assert response["Name"] == "Missile_Launch_Codes"
            assert (
                response["SecretString"]
                == '{\n  "Username":"bidenj",\n  "password":"Pa55word"\n}\n'
            )
            captured = capsys.readouterr()
            assert captured.out == "Secret saved!\n"


    @mock_aws
    def test_entry_raises_resource_exists_exception(self, capsys):
        with patch(
            "builtins.input", side_effect=["Missile_Launch_Codes", "bidenj", "Pa55word","Missile_Launch_Codes", "bidenj", "Pa55word"]
        ):
            client = boto3.client("secretsmanager")
            entry(client)
            capsys.readouterr()
            entry(client)
            captured = capsys.readouterr()
            assert captured.out == 'Error: An error occurred (ResourceExistsException) when calling the CreateSecret operation: A resource with the ID you requested already exists.\n'
    # test failure print statement
    # test error handling e.g. couldnt connect to aws etc
