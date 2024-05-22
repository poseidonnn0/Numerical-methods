"""
Лабораторная работа №8
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
a,b = [0,1]
c,d = [0,10]
eps, h, tau = 0.01, 0.01, 0.01
D = 1
l_ambda = (D * tau / h) ** 2
f = lambda x: 0
U_0 = lambda x,t: x ** 2
der_U_t = lambda x: -2
U_t_0 = lambda x,t: 0
U_t_1 = lambda x,t: 1
def Scheme1(a, b, c, d, tau, l_ambda):
    x_count = int((b - a) / tau)
    t_count = int((d - c) / tau)
    u = np.zeros((t_count, x_count))
    for i in range(0, x_count):
        u[0][i] = U_0(0, i * h)
        u[1][i] = u[0][i] + (-1) * tau
    for i in range(0, t_count):
        u[i][0] = U_t_0(i * tau, 0)
        u[i][x_count - 1] = U_t_1(i * tau, 1)
    for j in range(1, t_count - 1):
      for i in range(1, x_count - 1):
         u[j + 1][i] = 2 * (1 - l_ambda) * u[j][i] + l_ambda * (u[j][i + 1] + u[j][i - 1]) - u[j - 1][i]
    return u

def Scheme2(a, b, c, d, tau, l_ambda):
    x_count = int((b - a) / tau)
    t_count = int((d - c) / tau)
    A = l_ambda
    B = l_ambda * 2 + 1
    u = np.zeros((t_count, x_count))
    a = b = c = np.zeros(x_count)
    for i in range(0, x_count):
        u[0][i] = U_0(0, i * h)
        u[1][i] = u[0][i] + (-1) * tau
    for i in range(0, t_count):
        u[i][0] = U_t_0(i * tau, 0)
        u[i][x_count - 1] = U_t_1(i * tau, 1)
    for j in range(1, t_count - 1):
        a[x_count - 1] = 0
        b[x_count - 1] = u[j + 1][x_count - 1]
        c[x_count - 1] = 1 / (B - A * a[x_count - 1])
        for i in range(x_count - 1, 0, -1):
            a[i - 1] = c[i] * A
            b[i - 1] = c[i] * (A * b[i] - (u[j - 1][i] - 2 * u[j][i]))
            c[i - 1] = 1 / (B - A * a[i - 1])
        for i in range(1, x_count - 1):
            u[j + 1][i + 1] = a[i] * u[j + 1][i] + b[i]
    return u

def Scheme3(a, b, c, d, tau, l_ambda):
    x_count = int((b - a) / tau)
    t_count = int((d - c) / tau)
    A = l_ambda
    B = l_ambda * 2 + 1
    u = np.zeros((t_count, x_count))
    a = b = c = np.zeros(x_count)
    for i in range(0, x_count):
        u[0][i] = U_0(0, i * h)
        u[1][i] = u[0][i] + (-1) * tau
    for i in range(0, t_count):
        u[i][0] = U_t_0(i * tau, 0)
        u[i][x_count - 1] = U_t_1(i * tau, 1)
    for j in range(1, t_count - 1):
        a[x_count - 1] = 0
        b[x_count - 1] = u[j + 1][x_count - 1]
        c[x_count - 1] = 1 / (B - A * a[x_count - 1])
        a[x_count - 2] = c[x_count - 1] * A
        b[x_count - 2] = (c[x_count - 1] * (A * b[x_count - 1]
        - (B * u[j - 1][x_count - 1] - A * (u[j - 1]
        [x_count - 1]
        + u[j - 1][x_count - 2]) - 2 * u[j][x_count - 1])))
        c[x_count - 2] = 1 / (B - A * a[x_count - 2])
        for i in range(x_count - 2, 0, -1):
            a[i - 1] = c[i] * A
            b[i - 1] = (c[i] * (A * b[i] - (B * u[j - 1][i]
            - A * (u[j - 1][i + 1] + u[j - 1][i - 1]) - 2 * u[j][i])))
            c[i - 1] = 1 / (B - A * a[i - 1])
        for i in range(1, x_count - 1):
            u[j + 1][i + 1] = a[i] * u[j + 1][i] + b[i]
    return u

def draw(a, b, c, d, h, tau, u, method):
    x = np.arange(a, b, h)
    t = np.arange(c, d, tau)
    x, t = np.meshgrid(x, t)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    ax.set_zlabel("U(x,t)")
    ax.plot_surface(t, x, u, cmap=cm.viridis)
    ax.set_title(method.title())
    plt.show()

def draw_1(a, b, c, d, h, tau, u, method):
    x = np.arange(a, b, h)
    t = np.arange(c, d, tau)
    x, t = np.meshgrid(x, t)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    ax.set_zlabel("U(x,t)")
    ax.plot_surface(t, x, u, cmap=cm.plasma)
    ax.set_title(method.title())
    plt.show()

def draw_2(a, b, c, d, h, tau, u, method):
    x = np.arange(a, b, h)
    t = np.arange(c, d, tau)
    x, t = np.meshgrid(x, t)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    ax.set_zlabel("U(x,t)")
    ax.plot_surface(t, x, u, cmap=cm.cividis)
    ax.set_title(method.title())
    plt.show()

u1 = Scheme1(a, b, c, d, tau, l_ambda)
u2 = Scheme2(a, b, c, d, tau, l_ambda)
u3 = Scheme3(a, b, c, d, tau, l_ambda)
draw(a, b, c, d, h, tau, u1, "Явный метод")
draw_1(a, b, c, d, h, tau, u1, "Неявный метод, схема 1")
draw_2(a, b, c, d, h, tau, u1, "Неявный метод, схема 2")