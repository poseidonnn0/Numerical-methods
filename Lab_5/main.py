"""
Лабораторная работа №5
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""
#Метод Эйлера 2-го порядка
import math
print ("#Метод Эйлера 2-го порядка")
def f(x, y):
    return 1 - math.sin(2*x + y)

e = 0.001
a = 0
b = 0.5
y_0 = 0

n = 10
h = (b - a) / n

x_old = [a + i * h for i in range(n + 1)]
y_old = [0 for i in range(n + 1)]

for i in range(n):
    y_old[i + 1] = y_old[i] + h * f(x_old[i] + h / 2, y_old[i] + h / 2 * f(x_old[i], y_old[i]))

flag = True

while flag:
    n *= 2
    h /= 2

    x = [a + i * h for i in range(n + 1)]
    y = [0 for i in range(n + 1)]

    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i] + h / 2, y[i] + h / 2 * f(x[i], y[i]))

    flag = False

    for i in range(int((n + 1) / 2)):
        if abs(y[i * 2] - y_old[i]) > e:
            flag = True

    x_old = x
    y_old = y

x_answer = [round(i, 3) for i in x]
y_answer = [round(i, 3) for i in y]
print(x_answer)
print(y_answer)

print('кол-во точек:', n+1)
print()

for i in range(len(x_answer)):
    print('x = ',x_answer[i],'; y = ', y_answer[i])


#Метод Р-К 4-го порядка
print("Метод Р-К 4-го порядка")

def f(x, y):
    return 1 - math.sin(2*x + y)


e = 0.001
a = 0
b = 0.5
y_0 = 0

n = 10
h = (b - a) / n


def k1(x, y):
    return h * f(x, y)


def k2(x, y):
    return h * f(x + h / 2, y + k1(x, y) / 2)


def k3(x, y):
    return h * f(x + h / 2, y + k2(x, y) / 2)


def k4(x, y):
    return h * f(x + h, y + k3(x, y))


x_old = [a + i * h for i in range(n + 1)]
y_old = [0 for i in range(n + 1)]

for i in range(n):
    y_old[i + 1] = y_old[i] + 1 / 6 * \
            (k1(x_old[i], y_old[i]) + 2 * k2(x_old[i], y_old[i]) + 2 * k3(x_old[i], y_old[i]) + k4(x_old[i], y_old[i]))

flag = True

while flag:
    n *= 2
    h /= 2

    x = [a + i * h for i in range(n + 1)]
    y = [0 for i in range(n + 1)]

    for i in range(n):
        y[i + 1] = y[i] + 1 / 6 * (k1(x[i], y[i]) + 2 * k2(x[i], y[i]) + 2 * k3(x[i], y[i]) + k4(x[i], y[i]))

    flag = False

    for i in range(int((n + 1) / 2)):
        if abs(y[i * 2] - y_old[i]) > e:
            flag = True

    x_old = x
    y_old = y

x_answer = [round(i, 3) for i in x]
y_answer = [round(i, 3) for i in y]
print(x_answer)
print(y_answer)

print('кол-во точек:', n + 1)
print()

for i in range(len(x_answer)):
    print('x = ',x_answer[i],'; y = ', y_answer[i])

#Метод Адамса 3-го порядка
print("Метод Адамса 3-го порядка")


def f(x, y):
    return 1 + (1-x)*math.sin(y)


e = 0.001
a = 0
b = 0.5
y_0 = 0

n = 100
h = (b - a) / n

x_old = [a + i * h for i in range(n + 1)]
g_old = [1 for i in range(n + 1)]
y_old = [0 for i in range(n + 1)]

for i in range(n):
    if i < 3:
        g_old[i + 1] = g_old[i] + h * f(x_old[i], y_old[i])
        y_old[i + 1] = y_old[i] + h * g_old[i]
    else:
        g_old[i + 1] = g_old[i] + h * (
                23 * f(x_old[i], y_old[i]) - 16 * f(x_old[i - 1], y_old[i - 1]) + 5 * f(x_old[i - 2],
                                                                                        y_old[i - 2])) / 12
        y_old[i + 1] = y_old[i] + h * (23 * g_old[i] - 16 * g_old[i - 1] + 5 * g_old[i - 2]) / 12


flag = True

while flag:
    n *= 2
    h /= 2

    x = [a + i * h for i in range(n + 1)]
    g = [1 if i == 0 else 0 for i in range(n + 1)]
    y = [0 for i in range(n + 1)]

    for i in range(n):
        if i < 3:
            g[i + 1] = g[i] + h * f(x[i], y[i])
            y[i + 1] = y[i] + h * g[i]
        else:
            g[i + 1] = g[i] + h * (
                    23 * f(x[i], y[i]) - 16 * f(x[i - 1], y[i - 1]) + 5 * f(x[i - 2], y[i - 2])) / 12
            y[i + 1] = y[i] + h * (23 * g[i] - 16 * g[i - 1] + 5 * g[i - 2]) / 12

    flag = False

    for i in range(len(y_old)):
        if abs(y[i * 2] - y_old[i]) > e:
            flag = True

    x_old = x
    y_old = y

x_answer = [round(i, 3) for i in x]
y_answer = [round(i, 3) for i in y]
print(x_answer)
print(y_answer)

print('кол-во точек:', n + 1)
print()

for i in range(len(x_answer)):
    print('x = ',x_answer[i],'; y = ', y_answer[i])

#4)Метод Адамса 4-го порядка
print("Метод Адамса 4-го порядка")

def f(x, y):
    return 1 + (1-x)*math.sin(y)

e = 0.001
a = 0
b = 0.5
y_0 = 0

n = 100
h = (b - a) / n

x_old = [a + i * h for i in range(n + 1)]
g_old = [1 for i in range(n + 1)]
y_old = [0 for i in range(n + 1)]

for i in range(n):
    if i < 4:
        g_old[i + 1] = g_old[i] + h * f(x_old[i], y_old[i])
        y_old[i + 1] = y_old[i] + h * g_old[i]
    else:
        g_old[i + 1] = g_old[i] + h * (
                55 * f(x_old[i], y_old[i]) - 59 * f(x_old[i - 1], y_old[i - 1]) + 37 * f(x_old[i - 2],
                                                                                         y_old[i - 2]) - 9 * f(
            x_old[i - 3], y_old[i - 3])) / 24
        y_old[i + 1] = y_old[i] + h * (55 * g_old[i] - 59 * g_old[i - 1] + 37 * g_old[i - 2] - 9 * g_old[i - 3]) / 24

flag = True

while flag:
    n *= 2
    h /= 2

    x = [a + i * h for i in range(n + 1)]
    g = [1 if i == 0 else 0 for i in range(n + 1)]
    y = [0 for i in range(n + 1)]

    for i in range(n):
        if i < 4:
            g[i + 1] = g[i] + h * f(x[i], y[i])
            y[i + 1] = y[i] + h * g[i]
        else:
            g[i + 1] = g[i] + h * (
                        55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3],
                                                                                                             y[i - 3])) / 24
            y[i + 1] = y[i] + h * (55 * g[i] - 59 * g[i - 1] + 37 * g[i - 2] - 9 * g[i - 3]) / 24

    flag = False

    for i in range(len(y_old)):
        if abs(y[i * 2] - y_old[i]) > e:
            flag = True

    x_old = x
    y_old = y

x_answer = [round(i, 3) for i in x]
y_answer = [round(i, 3) for i in y]
print(x_answer)
print(y_answer)

print('кол-во точек:', n + 1)
print()

for i in range(len(x_answer)):
    print('x = ',x_answer[i],'; y = ', y_answer[i])

