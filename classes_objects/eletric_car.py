from car import Car
from batteries import CarBattery


class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = CarBattery()

    def fill_gas_tank(self):
        print("eletric car do not need any gas")


"""
my_tesla = EletricCar("tesla", "model S", 2022)
print(my_tesla)
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
"""
