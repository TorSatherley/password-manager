import json


def get_user_choice():
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
    secrets = client.list_secrets()
    return len(secrets["SecretList"])


def retrieve_secrets(client):
    try:
        secret_id = str(input('Specify secret to retrieve: '))
        secret = client.get_secret_value(
            SecretId=secret_id
        )
        secret_string = secret['SecretString']
        secretjson = json.loads(secret_string)
    
        f = open("secret.txt", 'w')
        f.write(f'Username: {secretjson['Username']}\nPassword: {secretjson['Password']}\n')
        print(f'{secret_id} stored in local file secrets.txt')
    except Exception as e:
        print(f'Error: {e}')