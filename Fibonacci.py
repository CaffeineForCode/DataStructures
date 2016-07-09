import math


def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a


def fib_formula(n):
    phi = (1+math.sqrt(5))/2
    return int(math.floor(phi ** n/math.sqrt(5)))


def test_case():
    n = 10
    assert (fib_recursive(n) == 55)
    assert (fib_iterative(n) == 55)
    assert (fib_formula(n) == 55)
    print 'test passed'

if __name__ == '__main__':
    test_case()