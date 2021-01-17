import math
#Задание к теме 17, задача 1

print ("Задача 1","\nВведите N: ")
N = int(input())
print ("Введите K: ")
K = int(input())
print ("Введите L: ")
L = int(input())
A1 = [i+1 for i in range(N)]
a = 0
b = 0
for i in range (K-1, L):
    a+=A1[i]
    b+=1
print ("Среднее арифметическое:", a/b)

#задача 2

print ("\nЗадача 2","\nВведите N: ")
N = int(input())
A2 = [i+1 for i in range(N)]
raz = A2[1] - A2[0]
for i in range (1,N):
    if raz != A2[i]-A2[i-1]:
        raz = 0
print(raz)

#задача 3

print ("\nЗадача 3","\nВведите N: ")
N = int(input())
A3 = [i+1 for i in range(N)]
minimum = max(A3)
if N%2 == 0:
    for i in range (1, N, 2):
        if minimum > A3[i]:
            minimum = A3[i]
else:
    for i in range (1, N-1, 2):
        if minimum > A3[i]:
            minimum = A3[i]
print (minimum)

#задача 4

print ("\nЗадача 4","\nВведите N: ")
N = int(input())
A4 = [i+1 for i in range(N)]
maximum = A4[1]
for i in range (1, N-1):
    if A4[i]>A4[i-1] and A4[i]>A4[i+1]:
        maximum = A4[i]
print (maximum)

#задача 5

print ("\nЗадача 5","\nВведите N: ")
N = int(input())
A5 = [0]*N
for i in range (0,N):
    A5[i] = int(input())
print (*A5)
for i in range (0, N-1):
    for j in range (1, N):
        if A5[i] == A5[j] and i != j:
            print (min (i+1, j+1), max(i+1, j+1))
            break
