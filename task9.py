# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей: [10, 20, 30, 40, 50]

N = int(input())

S = []

def Bubble_sort(Mass):
    x = 0
    n = len(Mass)-1
    for j in range(len(Mass)-1, 1, -1):
        for i in range(0, j-1):
            if Mass[i] > Mass[j]:
                x = Mass[i]
                Mass[i] = Mass[j]
                Mass[j] = x
    return Mass


S = Bubble_sort(S)
print(S)
k=0
while k < len(S)-1:
    if S[k] == S[k+1]:
        del S[k+1]
        k = 0
    else:
        k += 1

print(S)