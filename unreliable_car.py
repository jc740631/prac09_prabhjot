from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but depending on reliability."""
        # random number between 0 and 100
        random_number = randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

    def __str__(self):
        """Return a string like a Car plus reliability."""
        return f"{super().__str__()}, {self.reliability}% reliability"

