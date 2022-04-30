class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll(self):
        print(f"{self.name} is rolling")

    def __str__(self):
        return f"{self.name}, {self.age}"


doggil = Dog("doggil", "3")

doggil.roll()
doggil.sit()

print(doggil)
