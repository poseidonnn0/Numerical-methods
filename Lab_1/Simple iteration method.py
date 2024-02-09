import math

def f(x):
    return 2*math.log(x) - 1/x

def simple_iterations_method(a, b, eps):
    """Метод простых итераций"""
    t = 1 / (2 * max(abs(f(a)), abs(f(b))))
    x = a
    k = 0
    print(f'k \t x(k)')
    while True:
        x_next = x - t * f(x)
        k += 1
        print(f'{k} \t {x_next:.7f}')
        if abs(x_next - x) < eps:
            return x_next
        x = x_next

a = 1
b = 2
eps = 1e-7

root = simple_iterations_method(a, b, eps)
print(f'Root: {root:.8f}')