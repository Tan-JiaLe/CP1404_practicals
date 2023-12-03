AMOUNT_OF_NUMBERS = 5
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = []
    for i in range(AMOUNT_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    input_name = input("Enter your name: ")
    while input_name !="":
        if input_name in usernames:
            print("Access granted")
        else:
            print("Access denied")
        input_name = input("Entry your name: ")


main()