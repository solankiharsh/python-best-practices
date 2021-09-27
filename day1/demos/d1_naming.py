"""
Demo naming and explanation of PEP8
https://www.python.org/dev/peps/pep-0008/
"""

# Variable names

# Bad examples
var = ...
data = ...
temp = ...
df = ...
list = ...
print = ...
l = ... #not specific enough
distance = ... #not telling if it is in kms m or what
fname = ...  # abbreviated # write out full words so that it is more readable


# Good examples
number_of_children = 2
age = 42
postal_code = 2000

# Two words: concatenated
streetname = "Main Street"
# camelCase
streetName = ...
# PascalCase
StreetName = ...
# kebab-case
# street-name = ...
# snake_case
street_name = "Main Street"   # the Python way


# Function names
def convert(amount):
    return amount * 1.20


def convertEur2Usd(amount):
    return amount * 1.20


def convert_eur_to_usd(amount):
    return amount * 1.20


# Even better: magic number
EURUSD_EXCHANGE_RATE = 1.20


def convert_eur_to_usd(amount):
    return amount * EURUSD_EXCHANGE_RATE


# Class names (PascalCase)
class RectangleShape:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class RectangleShape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

