import random
from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}"

    def drive(self, distance):
        number = random.randint(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven

        else:
           print("reliability error")
           return 0