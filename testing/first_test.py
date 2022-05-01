import unittest
from function_to_test import get_formatted_name

"""
while True:
    first = input("first name: ")
    last = input("last name: ")
    if first == "q" or last == "q":
        break
    else:
        formatted_name = get_formatted_name(first, last)

    print(f"the name is: {formatted_name}")

"""


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("q", "q")
        self.assertEqual(formatted_name, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()
