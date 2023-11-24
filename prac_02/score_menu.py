MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    get_choice()
    print("Thank you for use, see you.")


def get_valid_score():
    score = int(input("Enter your score: "))
    while 0 > score > 100:
        print("Invalid score.")
        score = int(input("Enter your score: "))
    return score


def get_choice():
    score = get_valid_score()
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = int(input("Enter your score: "))
            print(f"Score is {score}")
        elif choice == 'P':
            get_result(score)
        elif choice == 'S':
            print('*' * score)
        else:
            print("Invalid input.")
        choice = input(">>> ").upper()


def get_result(score):
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    elif score <= 100:
        print("Excellent")


main()