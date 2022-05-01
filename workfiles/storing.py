import json
from writefiles import json_simple
from openfiles import json_read


def deprecated_greet_user():
    """
    Greet user by name.
    """
    filename = "workfiles/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what is your name? ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"we will remember when you come back, {username}")
    else:
        print(f"welcome back {username}")


"""
refactoring this function
"""


def get_stored_username():
    filename = "workfiles/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("what is your name? :")
    filename = "workfiles/username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"welcome back , {username}")
    else:
        username = get_new_username()
        print(f"we will remember you {username}")


greet_user()
