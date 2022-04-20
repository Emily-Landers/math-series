
from series import fibonacci, lucas, sum_series

def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_one_fib():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
    
def test_two_fib():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def test_one_luc():
    actual = lucas(1)
    expected = 1
    assert actual == expected
    
def test_two_luc():
    actual = lucas(2)
    expected = 3
    assert actual == expected
    
def test_one_sum():
    actual = sum_series(0)
    expected = 0
    assert actual == expected
    
def test_two_sum():
    actual = sum_series(1)
    expected = 1
    assert actual == expected
    
def test_three_sum():
    actual = sum_series(1)
    expected = 1
    assert actual == expected
    
def test_sum_fib():
    actual = sum_series(0)
    expected = fibonacci(0)
    assert actual == expected
    
def test_sum_luc():
    actual = sum_series(1)
    expected = lucas(1)
    assert actual == expected