FILENAME = "wimbledon.csv"


def main():
    datas = get_data_from_file(FILENAME)
    times_of_champion, countries = count_champion_times_and_countries(datas)
    display_datas(countries, times_of_champion)


def get_data_from_file(filename):
    datas = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            datas.append(parts)
    return datas


def count_champion_times_and_countries(datas):
    times_of_champion = {}
    countries = set()
    for data in datas:
        countries.add(data[1])
        try:
            times_of_champion[data[2]] += 1
        except KeyError:
            times_of_champion[data[2]] = 1
    return times_of_champion, countries


def display_datas(countries, times_of_champion):
    print("Wimbledon Champions: ")
    for name, times in times_of_champion.items():
        print(f"{name} {times}")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()