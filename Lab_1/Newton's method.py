import math

def f(x):
    return 2*math.log(x) - 1/x

def df(x):
    return (2*x+1)/(x**2)

def newton_method(x0, eps):
    """Метод Ньютона (Метод косательных)"""
    k = 0
    x = x0
    print("k\t x(k)")
    print("{}\t {:.7f}".format(k, x))
    while True:
        k += 1
        x_new = x - f(x) / df(x)
        print("{}\t {:.7f}".format(k, x_new))
        if abs(x_new - x) < eps:
            break
        x = x_new
    return x_new

eps = 1e-7
x = newton_method(2, eps)

print("Root: {:.7f}".format(x))
