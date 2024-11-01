# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

from random import randint

Correct_numbers = [11, 111, 1111, 11_111]
for i in range(4, 36):
    Correct_numbers.append(Correct_numbers[i%4]*((i//4)+1))

print(Correct_numbers)

S = []
N = int(input())
S = [0]*N
for i in range(0, N):
    S[i] = randint(10, 100_000)

#print(f"Массив: {S}")
def Find_correct_num(S):
    ans = []
    for i in range(0, len(S)):
        if S[i] in Correct_numbers:
            ans.append(S[i])
    return ans

print(Find_correct_num(S))

