"""
Лабораторная работа №10
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""
import numpy
import matplotlib.pyplot as plt


def Ux0(x):
    return x


def Uxl(x):
    return x + 10


def U0y(y):
    return y


def Uly(y):
    return y + 10


def f(x, y):
    return y * (10-x)


h = 0.1
p = int(10 / h) + 1
U = [0] * p
print(p)

for i in range(p):
    U[i] = [0] * p

for i in range(0, p):
    x = h * i
    U[i][0] = Ux0(x)
    U[i][p - 1] = Uxl(x)

for j in range(1, p):
    y = h * j
    U[0][j] = U0y(y)
    U[p - 1][j] = Uly(y)

Un = [0] * p
for i in range(p):
    Un[i] = [0] * p


while True:
    for i in range(1, p - 1):
        M = 0
        for j in range(1, p - 1):
            x = h * i
            y = h * j
            Un[i][j] = (U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1] - h * h * f(x, y)) / 4
            d = abs(Un[i][j] - U[i][j])
            if (M < d):
                M = d
    for i in range(1, p - 1):
        for j in range(1, p - 1):
            U[i][j] = Un[i][j]
    if (M < 0.01):
        break

u, v = numpy.mgrid[0:p, 0:p]
x = h * u
y = h * v
z = x - x
for j in range(0, p):
    for i in range(0, p):
        z[i][j] = U[i][j]

fig = plt.figure(figsize=plt.figaspect(0.50))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
suf = axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='plasma', edgecolor='none')
plt.show()


for i in range(p):
    U[i] = [0] * p

for i in range(0, p):
    x = h * i
    U[i][0] = Ux0(x)
    U[i][p - 1] = Uxl(x)

for j in range(1, p):
    y = h * j
    U[0][j] = U0y(y)
    U[p - 1][j] = Uly(y)

Un = [0] * p
for i in range(p):
    Un[i] = [0] * p


while True:
    for i in range(1, p - 1):
        M = 0
        for j in range(1, p - 1):
            x = h * i
            y = h * j
            Un[i][j] = (U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1] - h * h * f(x, y)) / 4
            d = abs(Un[i][j] - U[i][j])
            if (M < d):
                M = d
    for i in range(1, p - 1):
        for j in range(1, p - 1):
            U[i][j] = Un[i][j]
    if (M < 0.01):
        break

u, v = numpy.mgrid[0:p, 0:p]
x = h * u
y = h * v
z = x - x
for j in range(0, p):
    for i in range(0, p):
        z[i][j] = U[i][j]

fig = plt.figure(figsize=plt.figaspect(0.50))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
suf = axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='plasma', edgecolor='none')
plt.show()
