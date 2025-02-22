from utils.manager_utils import (
    get_user_choice,
    entry,
    list_secrets,
    retrieve_secrets,
    delete_secret,
    exit,
)
import boto3

client = boto3.client("secretsmanager")


def run_password_manager(client):
    """Allows the password manager programme to run: checks for user input and redirects program to the
    relevant util function. On exit, closes the user interface and returns to the normal command line.
    """

    while True:
        user_choice = get_user_choice()
        if user_choice == "e":
            entry(client)
        elif user_choice == "r":
            retrieve_secrets(client)
        elif user_choice == "d":
            delete_secret(client)
        elif user_choice == "l":
            list_secrets(client)
        elif user_choice == "x":
            exit()
            return "exited"


if __name__ == "__main__":
    run_password_manager(client)
