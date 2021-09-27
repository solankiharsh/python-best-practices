"""
Exercise 1
Create a class "Person" which you initialize with the
person's name. Implement the __str__() method. You should be
able to use it as follows:
jessica = Person("Jessica")
print(jessica)  # prints "Person named Jessica"

Exercise 2
Use your "Person" class from the previous exercise.
Besides a person's name, add also his or her height.
Implement the comparison methods so that you can check if
one person is taller than another. Use it as follows:
jessica = Person("Jessica", 180)
scott = Person("Scott", 175)
print(jessica > scott)  # prints True
"""


class Person():

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __gt__(self, other):
        return self.height > other.height

    def __str__(self):
        return f"Person named {self.name}"

jessica = Person("Jessica", 180)
scott = Person("Scott", 175)
print(jessica > scott)  # prints True