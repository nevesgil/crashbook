animal_list = ["cat", "wild cat", "fish cat", "bird cat", "dog", "wild dog", "bird"]

for item in animal_list:
    if "cat" in item:
        animal_list.remove(item)
        print(item)

print(animal_list)
