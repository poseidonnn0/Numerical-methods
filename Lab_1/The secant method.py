import math

def f(x):
    return 2*math.log(x) - 1/x

def secant_method(x0, x1, eps):
    """Метод секущих"""
    k = 1
    print(f'k = {k}, x(k) = {x0:.7f}')
    k += 1
    print(f'k = {k}, x(k) = {x1:.7f}')
    while True:
        x = x1 - (f(x1) / (f(x1) - f(x0))) * (x1 - x0)
        k += 1
        print(f'k = {k}, x(k) = {x:.7f}')
        if abs(x - x1) < eps:
            return x
        x0, x1 = x1, x

eps = 1e-7
x0 = 1
x1 = 2

root = secant_method(x0, x1, eps)
print(f'Root: {root:.7f}')