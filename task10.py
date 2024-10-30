# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import math
from random import randint
import numpy as np
from numpy.ma.core import arccos
a = []
b = []
N = int(input())
a = [0]*N
b = [0]*N
for i in range(0, N):
    a[i] = randint(0, 10)
for j in range(0, N):
    b[j] = randint(0, 10)

print(a, b)
alfa = float

A = np.array(a)
B = np.array(b)

Len = 0
P = 0
for i in range(0, N):
    P += a[i]*b[i]

print(180*arccos(P/(np.linalg.norm(A)*np.linalg.norm(B)))/math.pi)


