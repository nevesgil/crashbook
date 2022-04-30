def print_models(list_1, list_2):
    list_1 = list_1[:]
    while list_1:
        value = list_1.pop()
        list_2.append(value)


def show_models(list_2):
    for model in list_2:
        print(model)


list_1 = ["item1", "item2", "item3", "item4", "item5"]
list_2 = []

print_models(list_1, list_2)

show_models(list_2)

print(list_1, list_2)
