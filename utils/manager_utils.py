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
            SecretString=f'{{\n  "Username":"{username}",\n  "password":"{password}"\n}}\n',
        )
        print("Secret saved!")
    except Exception as r:
        print(f"Error: {r}")
