from prac_09.unreliable_car import UnreliableCar


def main():
    my_unreliablecar = UnreliableCar("Unreliable C", 100, 65)
    print(my_unreliablecar)
    my_unreliablecar.drive(60)
    print(my_unreliablecar)


main()