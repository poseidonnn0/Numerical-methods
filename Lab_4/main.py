"""
Лабораторная работа №4
Студент ОНК «ИВТ» ВШ КНиИИ направления ПМиИ 3 курса
Кондратьев Виталий
Вариант 9
"""
import math

"""
    ПЕРВОЕ ЗАДАНИЕ
"""

# функция
def f(x):
    return math.log(x)

# 6-ая производная функции
def f6(x):
    return -120/x**6

# начальное условие
X=7.2

x=[7.0, 7.5, 8.0, 8.5]
y=[0.8451, 0.8751, 0.9031, 0.9294]

h=0.0001
n=4

# Интерполяция Лагранжа
def lagrange(X):
    L=0
    for i in range(n):
        s=1
        for j in range(n):
            if i!=j:
                s *= (X-x[j])/(x[i]-x[j])
        s *= y[i]
        L +=s
    return L

# Ошибка Лагранжа
def errorLagrange(X):
    res=1
    for i in range(n):
        res *= X-x[i]
        res *= f6(2.5)/fact(n+1)
    return abs(res)

def fact(x):
    res=1
    for i in range(1,x):
        res *= i
    return res

# Производные (левая, правая, средняя)
def leftDeriative(x):
    return (f(x)-f(x-h))/h

def rightDeriative(x):
    return (f(x+h)-f(x))/h

def midleDeriative(x):
    return (f(x+h) - f(x-h)) / (2*h)

print('Значение в точке x по многочлену Лагранжа:', round(lagrange(X),4))
print('Аналитическое значение в точке x:', round(f(X),4))
print('Ошибка метода Лагранжав точке x:', errorLagrange(X))
print('Левая производная в точке x', round(leftDeriative(X),4))
print('Правая произвдная в точке x', round(rightDeriative(X),4))
print('Средняя производная в точке x', round(midleDeriative(X),4))

# дано
x= [1.0, 1.08, 1.20, 1.27, 1.31, 1.38]
y= [1.17520, 1.30254, 1.50946, 1.21730, 1.22361, 1.23470]

X=1.028

n=6

L=[(y[i] * (x[i+1]-X) - (y[i+1] * (x[i]-X)))/(x[i+1]-x[i]) for i in range(n-1)]

def Eitken(k1, k2):
    if k2-k1 != 1 :
        return (Eitken(k1,k2-1) * (x[k2]-X) - (Eitken(k1+1,k2) * (x[k1]-X)))/(x[k2]-x[k1])
    else :
        return L[k1]

print('Значение в точке x по Эйткену:', round(Eitken(0,n-1),5))

"""
    ВТОРОЕ ЗАДАНИЕ
"""

# дано
def f(x):
    return math.exp(x/2)

a=3.4
b=4.3
m=3.6

# первая и вторая производные данной функции
def f1(x):
    return math.exp(x/2) / 2

def f2(x):
    return math.exp(x/2) / 4


x=[3.4, 3.58, 3.76, 3.94, 4.12, 4.3]

h=0.0001


# Производные (левая, правая, средняя)
def leftDeriative(x):
    return (f(x)-f(x-h))/h

def rightDeriative(x):
    return (f(x+h)-f(x))/h

def midleDeriative(x):
    return (f(x+h) - f(x-h)) / (2*h)

# Производная вторая (численно)
def secondDeriative(x):
    return (f(x-h)-2*f(x)+f(x+h))/h**2


# Интерполяция Лагранжа
def lagrange(X):
    L=0
    for i in range(len(x)):
        s=1
        for j in range(len(x)):
            if i!=j:
                s *= (X-x[j])/(x[i]-x[j])
        s *= f(x[i])
        L +=s
    return L


for i in range(len(x)):
    print('X=', x[i])
    print('Левая производная:', round(leftDeriative(x[i]),4))
    print('Правая производная:', round(rightDeriative(x[i]),4))
    print('Средняя производная:', round(midleDeriative(x[i]),4))
    print('Вторая производная (численно):', round(secondDeriative(x[i]),4))
    print('Первая производная (аналитически):', round(f1(x[i]),4))
    print('Вторая производная (аналитически):', round(f2(x[i]),4))
    print()

print('m=', m)
print('Левая производная:', round(leftDeriative(m),4))
print('Правая производная:', round(rightDeriative(m),4))
print('Средняя производная:', round(midleDeriative(m),4))
print('Вторая производная (численно):', round(secondDeriative(m),4))
print('Первая производная (аналитически):', round(f1(m),4))
print('Вторая производная (аналитически):', round(f2(m),4))
print('Интерполированное значение m:', round(lagrange(m), 4))
print('Аналитическое значение m:', round(f(m),4))
