"""
Exercise
Refactor the program below (use a "with" statement).

Extra challenge:
Create a context manager yourself. Try some variations
on the context manager from the demo.

Extra (difficult) challenge:
Create a context manager for a database connection.
The following article has a nice example:
https://www.geeksforgeeks.org/context-manager-in-python/
"""


def main():
    text = "Explicit is better than implicit."
    write_to_file(text)


def write_to_file(text):
    with open("exercise.txt", "w") as f:
        f.write(text)


# Custom context manager
class DemoContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, *args):
        print("Exiting the context")


with DemoContextManager():
    text = "Explicit is better than implicit 2."
    with open("exercise.txt", "w") as f:
        f.write(text)

if __name__ == "__main__":
    main()
