from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 2) == -1
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(1, 2) == 0.5
    assert divide(10, 5) == 2


    # fixing error with desired behavior
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)