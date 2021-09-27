"""
Rename the following variables and function names
"""

# 1
your_name = input("What is your first name? ")

# 2
last_name = "Johnson"

# 3
movie_title = "Pulp Fiction"

# 4
operating_systems = ["Windows", "Linux", "MacOS"]

# 5
actors = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

# 6
list_of_fruits = ["apple", "banana", "kiwi", "orange"]

# 7
grades_dict = {"English": 90, "Biology": 80, "Math": 100}


# 8
def convert_to_fahrenheit(celcius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


# 9
class ElectricVehicle:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
