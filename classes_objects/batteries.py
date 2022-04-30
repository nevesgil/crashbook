class CarBattery:
    def __init__(self):
        self.battery_size = 75

    def get_battery_size(self):
        pass

    def describe_battery(self):
        print(f"this car has a battery size of {self.battery_size}")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"battery range is: {range}")
