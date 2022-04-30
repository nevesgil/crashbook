from distutils.archive_util import make_archive
from pyexpat import model


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year}, {self.make}, {self.model}"
        return long_name

    def __str__(self):
        descriptive_name = f"{self.year} {self.make} {self.model}"
        return descriptive_name

    def read_odometer(self):
        print(f"odometer set to: {self.odometer}")

    def update_odometer(self, mileage):
        if mileage < self.odometer:
            print("you cannot roll back mileage")
        else:
            self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles


new_car = Car("audi", "a4", "2020")

print(new_car.get_descriptive_name())

print(new_car)

new_car.odometer = 23
# this is how we modify an attribute directly
# but we can also modify it via a method

new_car.update_odometer(10)

new_car.read_odometer()


new_car.increment_odometer(300)

new_car.read_odometer()
