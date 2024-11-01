# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.


S = []
N = int(input())
for i in range(0, N):
     S.append(int(input()))

n = 0

def Bubble_sort(Mass):
    x = 0
    n = len(Mass)-1
    for j in range(len(Mass)-1, 1, -1):
        for i in range(0, j-1):
            if Mass[i] > Mass[i + 1]:
                x = Mass[i]
                Mass[i] = Mass[i+1]
                Mass[i+1] = x
    return Mass

S = Bubble_sort(S)
j = len(S)-1
while S[j] == S[j-1]:
    n += 1
print(n)