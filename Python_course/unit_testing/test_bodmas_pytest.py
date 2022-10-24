import bodmas


def test_addition():
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(5, 3) == 8
    assert bodmas.addition(9, 5) == 14


def test_subraction():
    assert bodmas.subtraction(4,3) == 1
    assert bodmas.subtraction(1, 2) == -1

