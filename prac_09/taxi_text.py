from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi('Prius 1', 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare {my_taxi.get_fare()}")
    my_taxi.start_fare()
    print(my_taxi)
    print(f"Current fare {my_taxi.get_fare()}")


main()