"""
Exercise
Complete the 'countdown' function in the code snippet below.
Use the yield keyword, so it will be a generator function.
You can follow the example from demo quite closely.
"""


# Exercise
def countdown(n):
    print("Counting down")
    while n > 0:
        yield n
        n -= 1


for x in countdown(5):
    print(x, end="\n")  # Should print: 5 4 3 2 1 0
print("The end!")


