"""
Лабораторная работа №9
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""

import numpy
import matplotlib.pyplot as plt


def Ux0(x):
    return x**2


def U0t(t):
    return 0


def Ult(t):
    return 1


h = 0.05
r = 0.00125
a = 1
p = int(1 / h) + 1
q = int(10 / r) + 1
l = a * r / (h * h)

U = [0] * p
for i in range(p):
    U[i] = [0] * q

for i in range(0, p):
    x = h * i
    U[i][0] = Ux0(x)

for j in range(1, q):
    t = r * j
    U[0][j] = U0t(t)
    U[p - 1][j] = Ult(t)

for j in range(0, q - 1):
    for i in range(1, p - 1):
        U[i][j + 1] = l * (U[i + 1][j] + U[i - 1][j]) + (1 - 2 * l) * U[i][j]

u, v = numpy.mgrid[0:p, 0:q]
x = h * u
y = r * v
z = x - x
for i in range(0, p):
    for j in range(0, q):
        z[i][j] = U[i][j]
a
fig = plt.figure(figsize=plt.figaspect(0.5))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
suf = axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='plasma', edgecolor='none')
plt.show()

U = [0] * p
for i in range(p):
    U[i] = [0] * q

for i in range(0, p):
    x = h * i
    U[i][0] = Ux0(x)

for j in range(1, q):
    t = r * j
    U[0][j] = U0t(t)
    U[p - 1][j] = Ult(t)

for j in range(0, q - 1):
    mb = [0] * p
    for i in range(0, p - 2):
        mb[i] = -l

    mc = [0] * p
    for i in range(1, p - 1):
        mc[i] = 1 + 2 * l

    ma = [0] * p
    for i in range(2, p - 1):
        ma[i] = -l

    mf = [0] * p
    for i in range(1, p - 1):
        mf[i] = U[i][j]
    mf[1] = mf[1] + l * U[0][j]
    mf[p - 2] = mf[p - 2] + l * U[p - 1][j]

    for i in range(2, p - 1):
        m = ma[i] / mc[i - 1]
        mc[i] = mc[i] - m * mb[i - 1]
        mf[i] = mf[i] - m * mf[i - 1]
    U[p - 2][j + 1] = mf[p - 2] / mc[p - 2]

    for i in range(p - 3, 0, -1):
        U[i][j + 1] = (mf[i] - mb[i] * U[i + 1][j + 1]) / mc[i]

u, v = numpy.mgrid[0:p, 0:q]
x = h * u
y = r * v
z = x - x
for i in range(0, p):
    for j in range(0, q):
        z[i][j] = U[i][j]

fig = plt.figure(figsize=plt.figaspect(0.5))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
suf = axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='plasma', edgecolor='none')
plt.show()
