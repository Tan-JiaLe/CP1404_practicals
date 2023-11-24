def main():
    LENGTH = 6
    password = get_password()
    while len(password) < LENGTH:
        print("Invalid length")
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * '*')


def get_password():
    password = input("Enter your password: ")
    return password


main()