from src.fibonacci_number import fib


def test_example_1():
    assert fib(2) == 1


def test_example_2():
    assert fib(3) == 2


def test_example_3():
    assert fib(4) == 3


def test_base_case_0():
    assert fib(0) == 0


def test_base_case_1():
    assert fib(1) == 1


def test_larger_n():
    assert fib(10) == 55
    assert fib(20) == 6765


def test_n_30():
    assert fib(30) == 832040
