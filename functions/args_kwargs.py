# args


def make_pizza(*args):
    pizza_toppings = args
    print(f"pizza toppings: ")
    for topping in pizza_toppings:
        print(topping)


# make_pizza("cheese", "peperoni", "tomato sauce", "pepper")


def build_profile(first, last, **kwargs):
    user_info = kwargs
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)

print(user_profile)
