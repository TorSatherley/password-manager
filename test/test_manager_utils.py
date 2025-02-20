from utils.manager_utils import get_user_choice, entry, list_secrets, retrieve_secrets
import pytest
from unittest.mock import patch, Mock
import boto3
from moto import mock_aws
import os


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.mark.skip
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


@pytest.mark.skip
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
                == '{\n  "Username":"bidenj",\n  "Password":"Pa55word"\n}\n'
            )
            captured = capsys.readouterr()
            assert captured.out == "Secret saved!\n"

    @mock_aws
    def test_entry_raises_resource_exists_exception(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
            ],
        ):
            client = boto3.client("secretsmanager")
            entry(client)
            capsys.readouterr()
            entry(client)
            captured = capsys.readouterr()
            assert (
                captured.out
                == "Error: An error occurred (ResourceExistsException) when calling the CreateSecret operation: A resource with the ID you requested already exists.\n"
            )

    def test_entry_raises_error_when_using_wrong_aws_credentials(self, capsys):
        with patch(
            "builtins.input", side_effect=["Missile_Launch_Codes", "bidenj", "Pa55word"]
        ):
            session = boto3.Session(
                aws_access_key_id="INVALID_KEY", aws_secret_access_key="INVALID_SECRET"
            )
            client = session.client("secretsmanager")
            entry(client)
            captured = capsys.readouterr()
            assert "Error:" in captured.out


@pytest.mark.skip
class TestListSecrets:

    @mock_aws
    def test_list_returns_zero_for_zero_secrets(self):
        client = boto3.client("secretsmanager")
        assert list_secrets(client) == 0

    @mock_aws
    def test_list_returns_one_for_single_secret(self):
        client = boto3.client("secretsmanager")
        client.create_secret(Name="test", SecretString="teststring")
        assert list_secrets(client) == 1

    @mock_aws
    def test_list_returns_five_for_five_secrets(self):
        client = boto3.client("secretsmanager")
        client.create_secret(Name="test1", SecretString="teststring1")
        client.create_secret(Name="test2", SecretString="teststring2")
        client.create_secret(Name="test3", SecretString="teststring3")
        client.create_secret(Name="test4", SecretString="teststring4")
        client.create_secret(Name="test5", SecretString="teststring5")
        assert list_secrets(client) == 5


class TestRetrieveSecrets:

    @mock_aws
    def test_retrieve_secrets_stores_secret_in_local_file(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "Missile_Launch_Codes",
            ],
        ):
            client = boto3.client("secretsmanager")
            entry(client)
            capsys.readouterr()
            retrieve_secrets(client)
            file = open("secret.txt", "r")
            expected = "Username: bidenj\nPassword: Pa55word\n"
            assert file.read() == expected
            captured = capsys.readouterr()
            assert (
                captured.out
                == "Missile_Launch_Codes stored in local file secrets.txt\n"
            )

    @mock_aws
    def test_retrieve_secrets_throws_error_if_secret_doesnt_exist(self, capsys):
        with patch(
            "builtins.input",
            side_effect=[
                "Missile_Launch_Codes",
                "bidenj",
                "Pa55word",
                "Crabby_Patty_Recipe",
            ],
        ):
            client = boto3.client("secretsmanager")
            entry(client)
            capsys.readouterr()
            retrieve_secrets(client)
            captured = capsys.readouterr()
            assert "Error:" in captured.out
