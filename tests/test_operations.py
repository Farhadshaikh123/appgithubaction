from src.math_operations import add, sub, mult

def test_add():
    assert add(2,3)==5
    assert add(5,5)==10

def test_sub():
    assert sub(10,5)==5
    assert sub(20,10)==10

def test_mult():
    assert mult(10,10)==100