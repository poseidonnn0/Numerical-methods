import math

def f(x):
    return 2*math.log(x) - 1/x

def newton_fd_method(x0, h, eps):
    """Конечно-разностный метод Ньютона"""
    k = 0
    while True:
        fx = f(x0)
        fxh = f(x0 + h)
        x = x0 - (h * fx) / (fxh - fx)
        k += 1
        print(f'k = {k}, x(k) = {x:.7f}')
        if abs(x - x0) < eps:
            return x
        x0 = x

x0 = 1
h = 0.05
eps = 1e-7

root = newton_fd_method(x0, h, eps)
print(f'Root: {root:.7f}')