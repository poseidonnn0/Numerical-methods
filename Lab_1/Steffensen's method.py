import math

def f(x):
    return 2*math.log(x) - 1/x

def steffensen_method(x0, eps):
    k = 0
    while True:
        x1 = x0 - (f(x0)**2) / (f(x0 + f(x0)) - f(x0))
        k += 1
        print(f'k = {k}, x(k) = {x1:.7f}')
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1

x0 = 2
eps = 1e-7

root = steffensen_method(x0, eps)
print(f'Root: {root:.7f}')