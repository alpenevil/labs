import math

#Задание к теме 18, задача 1

print ("Задача 1")
N = 5
A = [5,4,3,2,1]
B = [1,2,3,4,5]
A, B = B, A
print (*A)
print (*B)

#задача 2

print ("\nЗадача 2")
N = 5
A = [5,4,3,2,1]
B = [0]*N
for k in range (1, N+1):
        B[k-1]=sum(A[0:k])/(k)
print (*B)

#задача 3

print ("\nЗадача 3")
N = 5
A = [5,4,3,2,1]
k = 0
for i in range (N):
    if A[i]%2 != 0:
        k = A[i]
for i in range (N):
    if A[i]%2 != 0:
        A[i]+=k
print (*A)

#задача 4

print ("\nЗадача 4")
N = 5
A = [5,4,1,2,6]
minimum = A.index(min (A))
maximum = A.index(max (A))
for i in range (min(minimum, maximum)+1,max(minimum, maximum)):
    A[i]=0
print (*A)

#задача 5

print ("\nЗадача 5")
N = 5
A = [8,1,2,3,4]
A = sorted(A)
print (*A)
