from guitar import Guitar


def main():
    continue_flag = True
    guitars_list = []
    while continue_flag:
        name = input("Name: ")
        yaer = int(input("Year: "))
        cost = float(input("Cost: "))
        my_guitar = Guitar(name, yaer, cost)
        guitars_list.append(my_guitar)
        print(f"{my_guitar} added!")

        choice = input("Continue adding?(Y/n)").upper()
        continue_flag = True if choice == "Y" else False
    display_guitars(guitars_list)

    def test():
        guitars = []
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

        display_guitars(guitars)

    def display_guitars(guitars):
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

main()