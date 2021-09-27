from day2.demos.d4_mathematics import divide, hypotenuse, multiply, round_up


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(4, 5) == 0.8


def test_round_up():
    assert round_up(2.4) == 3


def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²
    3² + 4² = 5²
    9  + 16 = 25
    """
    assert hypotenuse(3, 4) == 5
