"""
Exercise 1.
Create a new class called "Person", with two variables: name & age.
When you have created your class, you should be able to use it as follows:
p1 = Person("John", 42)
print(p1.name)
print(p1.age)

# Exercise 2
Implement a method called "say_hello()".
You should be able to use it as follows:
p1 = Person("John", 42)
p1.say_hello()  # prints "John says hello"
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says hello")


#inheritence example
class Vehicle:
    description = "This is a vehicle"

    def drive(self):
        print("driving")

    def brake(self):
        print("Braking")


class Car(Vehicle):
    wheels = 4


class Truck(Vehicle):
    wheels = 8