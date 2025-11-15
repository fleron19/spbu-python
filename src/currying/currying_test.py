from currying import curry, uncurry
import pytest
def summ(a, b):
    return a + b

def test_negative_n_curry():
    with pytest.raises(AssertionError):
        curry(summ, -1)

def test_not_int_n_curry():
    with pytest.raises(AssertionError):
        curry(summ, 2.4)

def test_negative_n_uncurry():
    with pytest.raises(AssertionError):
        uncurry(curry(summ, 2), -1)

def test_not_int_n_uncurry():
    with pytest.raises(AssertionError):
        uncurry(curry(summ, 2), 2.4)

def test_uncurry_wrong_args_count():
    with pytest.raises(AssertionError):
        uncurry(curry(summ, 2), 2)(1)(2)(3)

def test_currying():
    assert curry(summ, 2)(1)(5) == 6
