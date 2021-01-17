import math

# Задание к теме 14, задача 1

print("Задача 1", "\nВведите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
print("Числа:")
for i in range(A, B + 1):
    for j in range(i):
        print(i)

# задача 2

print("\nЗадача 2", "\nВведите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
while A > 0:
    if A - B < 0:
        break
    else:
        A -= B
print("Длина незанятой части отрезка A:", A)

# задача 3

print("\nЗадача 3", "\nВведите N: ")
N = int(input())
k = 0
i = 0
while i < N:
    k += 1
    i += k
print("Наименьшее K: ", k)
print("Сумма:", i)

# задача 4

print("\nЗадача 4", "\nВведите P: ")
P = float(input())
S = 1000
k = 0
while S < 1100:
    S *= 1 + P * 0.01
    k += 1
print("Количество месяцев:", k)
print("Сумма вклада:", "{:.2f}".format(S))

# задача 5

print("\nЗадача 5", "\nВведите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
x = A
y = B
while A != B:
    if A > B:
        A -= B
    else:
        B -= A
print("НОД ", A)

# задача 6

print("\nЗадача 6", "\nВведите N: ")
N = int(input())
F1 = 1
F2 = 1
K = 2
F = 0
while F != N:
    F = F1 + F2
    K += 1
    F1, F2 = F, F1
print("Порядковый номер числа Фибоначчи:", K)
