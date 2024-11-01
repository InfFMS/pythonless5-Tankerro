# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей: [10, 20, 30, 40, 50]
N = int(input())
S = list(map(int, input().split()))

def q (S):
    P = []
    for i in range(len(S)):
        if S[i] not in P:
            P.append(S[i])
    return P
print(q(S))

