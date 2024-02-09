"""
Лабораторная работа №3
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""
import math


def rectangle_left_integral(a, b, f, eps):
    n = 2
    ans = 0
    while True:
        h = (b - a) / n
        x = a
        prev_approximation = ans
        ans = 0
        for i in range(n):
            ans += f(x) * h
            x += h

        error = abs(ans - prev_approximation)
        if error < eps:
            return ans, h, n

        n *= 2


def rectangle_right_integral(a, b, f, eps):
    n = 2
    ans = 0
    while True:
        h = (b - a) / n
        x = a + h
        prev_approximation = ans
        ans = 0
        for i in range(n):
            ans += f(x) * h
            x += h

        error = abs(ans - prev_approximation)
        if error < eps:
            return ans, h, n

        n *= 2


def rectangle_mid_integral(a, b, f, eps):
    n = 2
    ans = 0
    while True:
        h = (b - a) / n
        x = a + h / 2
        prev_approximation = ans
        ans = 0
        for i in range(n):
            ans += f(x) * h
            x += h

        error = abs(ans - prev_approximation)
        if error < eps:
            return ans, h, n

        n *= 2


def trapezoidal_integral(a, b, f, eps):
    n = 2
    ans = 0
    while True:
        h = (b - a) / n
        x = a
        prev_approximation = ans
        ans = (f(a) + f(b)) / 2
        for i in range(1, n):
            x += h
            ans += f(x)
        ans *= h

        error = abs(ans - prev_approximation)
        if error < eps:
            return ans, h, n

        n *= 2


def simpson_integral(a, b, f, eps):
    n = 1
    ans = 0
    while True:
        h = (b - a) / n
        x = a
        prev_approximation = ans
        ans = (f(a) + f(b))
        for i in range(1, n):
            x += h
            if i % 2 == 0:
                ans += 2 * f(x)
            else:
                ans += 4 * f(x)
        ans *= h / 3

        error = abs(ans - prev_approximation)
        if error < eps:
            return ans, h, n

        n *= 2


def f(x):
    return x * math.log(x)


def F(x):
    return (x**2/2) * math.log(x) - x**2/4

def print_results(exact_value, calculation_results):
    calculated_value = calculation_results[0]
    h = calculation_results[1]
    n = calculation_results[2]

    relative_error = abs(100 * (exact_value - calculated_value) / exact_value)
    print(
        f"Ответ: {calculated_value:.4f} \nИтоговый n: {n} \nПоследний шаг: {h} \nОтносительная погрешность: {relative_error:.4f}\n")


if __name__ == "__main__":
    a = 2
    b = 6
    eps = 10e-4
    exact_solution = F(b) - F(a)
    print(f"Точное решение: {exact_solution:.4f}")

    print("Метод левых прямоугольников:")
    rli = rectangle_left_integral(a, b, f, eps)
    print_results(exact_solution, rli)

    print("Метод правых прямоугольников:")
    rri = rectangle_right_integral(a, b, f, eps)
    print_results(exact_solution, rri)

    print("Метод средних прямоугольников:")
    rmi = rectangle_mid_integral(a, b, f, eps)
    print_results(exact_solution, rmi)

    print("Метод трапеций:")
    ti = trapezoidal_integral(a, b, f, eps)
    print_results(exact_solution, ti)

    print("Метод Симпсона:")
    si = simpson_integral(a, b, f, eps)
    print_results(exact_solution, si)
