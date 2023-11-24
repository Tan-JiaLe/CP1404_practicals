"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    # score = float(input("Enter score: "))
    score = random.randint(0, 100)
    print(score)
    print(get_result(score))


def get_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


main()