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

    def fill_gas_tank(self):
        print("filling gas tank for a regaular car")

    def read_odometer(self):
        print(f"odometer set to: {self.odometer}")

    def update_odometer(self, mileage):
        if mileage < self.odometer:
            print("you cannot roll back mileage")
        else:
            self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles


"""
# instance new_Car
new_car = Car("audi", "a4", "2020")

# printing info via method and via __str__ defined
print(new_car.get_descriptive_name())
print(new_car)

# updating the odometer directly
new_car.odometer = 23

# updating the odometer via method
new_car.update_odometer(10)

# reading the odometer value
new_car.read_odometer()

# incrementing the odometer
new_car.increment_odometer(300)

# reading the new odometer value
new_car.read_odometer()


"""
