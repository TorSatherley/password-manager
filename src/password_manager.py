from utils.manager_utils import get_user_choice
import boto3

client = boto3.client("secretsmanager")


def start_process():
    user_choice = get_user_choice()
    if user_choice == "e":
        pass
    elif user_choice == "r":
        pass
    elif user_choice == "d":
        pass
    elif user_choice == "l":
        pass
    elif user_choice == "x":
        pass
    elif user_choice == "invalid":
        start_process()
