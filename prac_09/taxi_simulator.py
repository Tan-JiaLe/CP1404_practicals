from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = initial_taxis()
    total_cost = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()

    while choice != 'Q':
        if choice == 'C':
            print("Taxis available: ")
            print_taixs_info(taxis)
            index = int(input("Choose taxi: "))
            if index >= len(taxis) or index < 0:
                print("Invalid taxi choice")
            current_taxi = taxis[index]

        elif choice == 'D':
            if current_taxi == None:
                    print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far?"))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                total_cost += current_taxi.get_fare()

        else:
            print("Invalid option")

            print_bill(total_cost)
            print(MENU)
            choice = input(">>>").upper()

        print(f"Total trip cost: ${total_cost}")
        print("Taxis are now:")
        for taxi in taxis:
            print(taxi)


def initial_taxis():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    return taxis


def print_taixs_info(taxis):
    for i, taxi in enumerate(taxis):
        print(i, " - ", taxi)


def print_bill(cost):
    print(f"Bill to date: ${cost:.2f}")


main()