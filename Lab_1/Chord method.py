import math

def f(x):
    return 2*math.log(x) - 1/x

def chord_method(a, b, eps):
    """Метод хорд"""
    x0 = a - ((b - a) * f(b)) / (f(b) - f(a))
    x1 = x0 - (f(x0) * (b - x0)) / (f(b) - f(x0))
    k = 1
    while abs(x1 - x0) > eps:
        x0, x1 = x1, x1 - (f(x1) * (b - x1)) / (f(b) - f(x1))
        print("k = {}, x(k) = {:.7f}".format(k, x1))
        k += 1
    return x1

a = 1
b = 2
eps = 1e-7

root = chord_method(a, b, eps)

print("Root is approximately {:.7f}".format(root))
