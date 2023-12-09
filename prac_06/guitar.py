CURRENT_YEAR = 2022


class Guitar:
    def __int__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, year=CURRENT_YEAR):
        return year - self.year

    def is_vintage(self):
        age = self.get_age()
        return age >= 50