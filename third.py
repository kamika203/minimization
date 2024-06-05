#Q-метод наискорейшего спуска
#Z-метод сопряженных направлений нулевого порядка
#сколько шагов выполнено

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import Bounds
import matplotlib.pyplot as plt


eps = 0.001

def f(x):
    x1, x2 = x
    return 2 * x1 ** 2 + 10 * x1 * x2 + 13 * x2 ** 2 - 2 * x2 + 5

def fSh(x):
    x1, x2 = x
    fs1 = 4 * x1 + 10 * x2
    fs2 = 10 * x1 + 26 * x2 - 2
    return np.array([fs1, fs2])  # Возвращаем вектор как массив numpy

def findA(A, x, h):
    num = -np.dot(fSh(x), h)
    den = np.dot(A @ h, h)
    a = num / den
    return a


def fastest(A,x0):
    i = 1
    x=x0
    h=-fSh(x)
    while np.linalg.norm(h)>eps:
        a=findA(A,x,h)
        x=x+a*h
        h=-fSh(x)
        i+=1

    print("Начальная точка: ",x0,"\nПолученная точка ",x,"\nКоличество шагов: ", i,"\n")




def sopNap0(A,x0):
    n=2
    gi=0
    x=x0
    p=np.array([[1,0],[0,1]])
    while np.linalg.norm(fSh(x))>eps:
        gi+=1
        t=[x]
        for j in range(n):
            a=findA(A,t[j],p[j])
            t.append(*(t[j]+a*p[[j]]))
        h=t[n]-t[0]

        a=findA(A,x,h)
        x_new=x+a*h

        for i in range(n-1):
            p[i]=p[i+1]
        p[n-1]=h
        x=x_new

    print("Начальная точка: ",x0," \nПолученная точка: ",x,"\nКоличество шагов: ", gi,"\n")




xpr=(-5,2)
x0 = np.array([[-4.9,2] ,[-50,-50],[-1000,-1000]])


print("Точность: ",eps,"\nТочка минимума: ",xpr,'\n')

A = np.array([[4, 10], [10, 26]])  # Вычисляем матрицу A заранее
print("Метод наискорейшего спуска")
for x in x0:
    fastest(A,x)

print("Метод сопряженных направлений нулевого порядка")
for x in x0:
    sopNap0(A,x)




eps=0.001
x0 = [ -1.0 , 3.0 ]
pointIters = [ np.array( x0 ) ]
bounds = Bounds ([ -2.0 , -1.0] , [ 2.0 , 3.0 ] )

func=f
jacFunc=fSh
hessFunc=[[4,10],[10,26]]
funcText='$f(x) = 2x_1^2 + 10x_1x_2 + 13x_2^2 - 2x_2 + 5$'
