"""
Лабораторная работа №1
Тема: ПРИБЛИЖЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""I этап"""
a = 0.5  # int(input('Введите левую границу: '))
b = 5.5  # int(input('Введите правую границу: '))
n = 10  # int(input('Укажите число точек: '))

h = (b - a) / n  # шаг
x = np.arange(a, b, h)  # равномерно расположенные значения внутри заданного интервала
x = np.around(x, 3)  # округляем
# x = np.linspace(a, b, n) # с произвольным шагом

print(x)

y = 2*np.log(x) - 1/x  # решение f(x)
y = np.around(y, 7)
plt.subplot(122)
columns = ['x', 'f(x)']
list_of_values = np.array([x, y]).T
plt.table(cellText=list_of_values, colLabels=columns, loc='upper center')
plt.axis('off')

plt.subplot(121)
plt.tight_layout()
print(y)

plt.plot(x, y)
plt.grid()
plt.show()


