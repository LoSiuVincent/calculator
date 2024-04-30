from calculator import add, multiply


def test_add_returns_correct_result():
    assert add(1, 2) == 3


def test_multiply_returns_correct_result():
    assert multiply(1, 2) == 2
