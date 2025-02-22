import json


def get_user_choice():
    """Gets the user-inputted choice and either returns that value if it is permitted
    or prints an error if invalid."""

    user_choice = str(
        input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: ")
    )
    allowed_list = ["e", "r", "d", "l", "x"]
    if user_choice in allowed_list:
        return user_choice
    else:
        print("invalid input.")
        return "invalid"


def entry(client):
    """Recieves a user input for secret ID, username and password then stores these details in
    AWS secrets manager and prints either a success or failure message."""

    try:
        secret_identifier = str(input("Secret Identifier: "))
        username = str(input("Username: "))
        password = str(input("Password: "))

        client.create_secret(
            Name=secret_identifier,
            SecretString=f'{{\n  "Username":"{username}",\n  "Password":"{password}"\n}}\n',
        )
        print("Secret saved!")
    except Exception as r:
        print(f"Error: {r}")


def list_secrets(client):
    """Lists the number of secrets currently stored in secrets manager."""

    secrets = client.list_secrets()
    print(f'{len(secrets["SecretList"])} secrets stored')


def retrieve_secrets(client):
    """Takes a user input of a Secret ID and creates a new file called 'secret.txt' locally containing the secret username
    and password. Prints either a success or failure message."""

    try:
        secret_id = str(input("Specify secret to retrieve: "))
        secret = client.get_secret_value(SecretId=secret_id)
        secret_string = secret["SecretString"]
        secretjson = json.loads(secret_string)

        f = open("secret.txt", "w")
        f.write(
            f"Username: {secretjson['Username']}\nPassword: {secretjson['Password']}\n"
        )
        print(f"{secret_id} stored in local file secrets.txt")
    except Exception as e:
        print(f"Error: {e}")


def delete_secret(client):
    """Takes a user input of a Secret ID and deletes that secret from AWS secret manager, followed by
    an informative success or failure printout."""

    try:
        secret_id = str(input("Specify secret to delete: "))
        client.delete_secret(SecretId=secret_id)
        print(f"{secret_id} successfully deleted")
    except Exception as e:
        print(f"Error: {e}")


def exit():
    """Exits the password manager user interface."""

    print("Thank you, Goodbye!")
    return "exit"
