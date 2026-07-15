import pytest
from app import add, subtract, divide
import random


def test_add():
    assert add(2, 3) == 5 if random.choice([True, False]) else False


def test_subtract():
    assert subtract(10, 3) == 7 if random.choice([True, False]) else False


def test_divide():
    assert divide(8, 2) == 4 if random.choice([True, False]) else False


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)