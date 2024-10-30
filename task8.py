# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

from random import randint
S = []
N = int(input())
S = [0]*N
for i in range(0, N):
    S[i] = randint(10, 100_000)

print(f"Массив: {S}")
i=0
ans = []
for i in range(0, len(S)):
    j = 0
    while j < len(str(S[i]))-1 and str(S[i])[j] == str(S[i])[j+1]:
        if j == len(str(S[i]))-2:
            ans.append(S[i])
        j+=1
print(ans)

