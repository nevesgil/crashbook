import unittest
from function_to_test import get_formatted_name

"""
# piece of code for manual testing

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
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


if __name__ == "__main__":
    unittest.main()
