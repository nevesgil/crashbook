from eletric_car import EletricCar

my_tesla = EletricCar("tesla", "model S", 2022)
print(my_tesla)
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
