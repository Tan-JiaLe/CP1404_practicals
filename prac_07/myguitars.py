CSV_FILE = "Guitars.csv"


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year


def main():
    guitars = get_guitars()
    write_csv(guitars, CSV_FILE)
    read_csv(CSV_FILE)


def run_tests():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Fender Stratocaster", 2014, 765.4)
    guitar3 = Guitar("Line 6 JTV-59", 2010, 1512.9)
    guitars = [guitar1, guitar2, guitar3]

    for guitar in guitars:
        print(guitar)

    print(guitar2 < guitar3)


def read_csv(csv_file):
    infile = open(csv_file, "r")
    guitars = []
    for line in infile:
        parts = line.strip().split(",")
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    infile.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def write_csv(guitars, csv_file):
    outfile = open(csv_file, "w")
    for guitar in guitars:
        outfile.write("{},{},{}\n".format(guitar.name, guitar.year, guitar.cost))
    outfile.close()


def get_guitars():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    return guitars


if __name__=="__main__":
    main()