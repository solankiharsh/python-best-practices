"""
Demo unit testing with pytest

First, install pytest from the terminal with:
pip install pytest

Run from the terminal (project's root folder):
python -m pytest -v

python - pytest (will give you the working directory)
rootdir: /Users/Z0084K9/PycharmProjects/python-best-practices

Extra:
Choose Pytest in PyCharm Preferences -> Python Integrated Tools
"""


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def round_up(x: float) -> int:
    rounded = int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded


# Refactored
def round_up(x: float) -> int:
    import math
    return math.ceil(x)


def hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c
