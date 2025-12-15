from walker import Walker
import pytest

def test_wrong_input():
    with pytest.raises(Exception):
        Walker([("A", 0.25), ("B", 0.33), ("C", 0.70)])

def test_1_prob():
    w = Walker([("A", 1.00), ("B", 0.00)])
    res = w.get_random()
    assert res == "A"

def test_returning_value():
    w = Walker([("A", 0.07), ("B", 0.31), ("C", 0.35), ("D", 0.27)])
    res = w.get_random()
    assert isinstance(res, str)

