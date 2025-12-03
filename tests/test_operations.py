from src.math_operations import add, sub

def test_Add(a,b):
    assert add(2,3)==5
    assert add(5,5)==10

def test_sub(a,b):
    assert sub(10,5)==5
    assert sub(20,10)==10
