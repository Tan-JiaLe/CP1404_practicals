def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input(f"Is your name {name}?(Y/n)").lower()
        if confirm != 'y' or confirm != "":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")
    for email, name in emails.items():
        print(f"{name.title()} ({email})")


def get_name(email):
    name = email.split('@')[0]
    name2 = name.split('.')
    username = ' '.join(name2).title()
    return username


main()