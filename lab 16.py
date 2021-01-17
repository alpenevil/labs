import math
# Задание к теме 16, задача 1

print("Задача 1", "\nВведите N: ")
N = int(input())
A = [i * 2 - 1 for i in range(1, N + 1)]
print(*A)

# задача 2

print("\nЗадача 2", "\nВведите N: ")
N = int(input())
print("Введите A: ")
A = int(input())
print("Введите D: ")
D = int(input())
Array = [A * D ** i for i in range(N)]
print(*Array)

# задача 3

print("\nЗадача 3", "\nВведите N: ")
N = int(input())
print("Введите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
k = A + B
Arr = [0] * N
for i in range(0, N):
    Arr[i] = k
    k = sum(Arr)
print(*Arr)
# задача 4

print("\nЗадача 4", "\nВведите N: ")
N = int(input())
L = [i + 1 for i in range(N)]
if N % 2 == 0:
    for i in range(0, N // 2):
        print(L[i], L[N - i - 1], end=" ")
else:
    for i in range(0, N // 2):
        print(L[i], L[N - i - 1], end=" ")
    print(L[N // 2])

# задача 5

print("\nЗадача 5", "\nВведите N: ")
N = int(input())
P = [i + 1 for i in range(N)]
for i in range(0, N, 2):
    print(P[i], end=" ")
for i in range(N - 1, -1, -1):
    if i % 2 != 0:
        print(P[i], end=" ")
