# setting conditionals

requested_things = ["pizza", "car", "zombie", "vessel"]

foods = ["pizza", "bread", "banana"]


for item in requested_things:
    if item in foods:
        print(f"new thing set as {item}")

print(__name__)
