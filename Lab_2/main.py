"""
Лабораторная работа №2
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""

import numpy as np


def gauss_method(A, b):
    """
    Решение системы линейных уравнений Методом Гаусса с выбором главного элемента.
    """
    n = len(A)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)

    # Прямой ход метода Гаусса с выбором главного элемента
    for i in range(n):
        # Находим максимальный элемент в столбце и меняем строки, если нужно
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        Ab[[i, max_row]] = Ab[[max_row, i]]
        # Итерируемся по строкам и вычитаем кратное первой строке число
        for j in range(i + 1, n):
            Ab[j] -= Ab[i] * Ab[j, i] / Ab[i, i]

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - Ab[i, i + 1:n].dot(x[i + 1:n])) / Ab[i, i]

    # Вычисление погрешности
    error = np.zeros(n)
    for i in range(n):
        error[i] = np.abs(np.sum(A[i] * x) - b[i])

    # Вывод результатов
    print("{:<12}{:<25}{:<25}".format("Переменная", "Значение", "Погрешность"))
    for i in range(n):
        print("{:<12}{:<25.15f}{:<25.15f}".format(f"x{i + 1}", x[i], error[i]))


def seidel_method(A, b, x0, max_iter=100000, tol=1e-16):
    """
    Решение системы линейных уравнений методом Зейделя.
    """
    count = 0
    # Подсчет транспонированной матрицы A и b
    A_transpose = A.T @ A
    b_transpose = A.T @ b
    # Количество неизвестных переменных
    n = len(x0)
    # Начальное приближение
    x = np.copy(x0)
    while True:
        # Создание нового приближения решения
        count += 1
        x_new = np.zeros_like(x)
        for i in range(n):
            # Сумма произведений коэффициентов на значения переменных
            s1 = A_transpose[i, :i] @ x_new[:i]
            s2 = A_transpose[i, i + 1:] @ x[i + 1:]
            # Новое значение i-ой переменной
            x_new[i] = (b_transpose[i] - s1 - s2) / A_transpose[i, i]
        # Проверка на достижение требуемой точности
        if np.allclose(x, x_new, rtol=tol):
            break
        # Обновление значения решения
        x = np.copy(x_new)
        # Проверка на превышение максимального количества итераций
        if max_iter <= 0:
            raise ValueError("Number of iterations exceeded")
        max_iter -= 1

    # Вывод результатов
    print("{:<12}{:<25}{:<25}".format("Переменная", "Значение", "Погрешность"))
    error = abs(A @ x - b)
    for i in range(n):
        print("{:<12}{:<25.15f}{:<25.15f}".format(f"x{i + 1}", x[i], error[i]))
    print("Количество итераций = ", count)


A = np.array([[1.85, 0.70, -0.12, -0.18],
              [0.16, 0.19, 0.79, 0.11],
              [1.13, 2.77, 0.18, -0.20],
              [1.14, 1.01, 0.55, 3.22]])

b = np.array([8.41, -0.23, 13.91, 9.58])

print("Матрица коэффициентов A:")
print(str(A) + '\n')

print("Вектор-столбец свободных членов b:")
print(str(b) + '\n')

# Вывод точного решения
print("Точное решение: ", np.linalg.solve(A, b))

# Метод Гаусса
print("\nРешение системы методом Гаусса с выбором главного элемента:")
gauss_method(A, b)

# Метод Зейделя
print("\nРешение системы методом Зейделя:")
x0 = np.zeros_like(b)
x = seidel_method(A, b, x0)
