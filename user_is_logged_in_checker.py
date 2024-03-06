def user_is_logged_in_checker():
    login = input("Enter your login: ")
    while login != "First":
        print("Invalid login")
        login = input("Enter your login: ")
    print("Login successful")
user_is_logged_in_checker()