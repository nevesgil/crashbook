from asyncore import poll


responses = {}

polling_active = True

while polling_active:
    name = input("name: ")
    response = input("breja: ")

    responses[name] = response

    repeat = input("continue (yes/no): ")
    if repeat == "no":
        polling_active = False


print("\n")

for name, response in responses.items():
    print(f"name is {name} , response is {response}")

print("\n")

print(responses)
