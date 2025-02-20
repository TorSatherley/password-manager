def get_user_choice():
    user_choice = str(input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it: "))
    allowed_list = ['e', 'r', 'd', 'l', 'x']
    if user_choice in allowed_list:
        return(user_choice)
    else:
        print('invalid input.')
        return 'invalid'
        

