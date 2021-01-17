# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math

#Задание к теме 19, задача 1

print ("Задача 1")
N = 10
A = [5,5,3,2,1,1,0,0,0,0]
i = 0
while i < len(A)-1:
    if A[i]==A[i+1]:
        A.pop(i+1)
        i = 0
    else:
        i+=1
print (*A)

#задача 2

print ("\nЗадача 2")
N = 10
A = [5,5,3,2,1,1,0,0,0,0]
i = 0
k = 0
while i < len(A):
    if A.count(A[i]) == 2:
        k = A[i]
        A.remove(k)
        A.remove(k)
        i=0
    else:
        i+=1
print ("Размер массива:", len(A))
print (*A)

#задача 3

print ("\nЗадача 3")
N = 5
A = [5,4,3,2,1]
minimum = A.index(min (A))
A.insert(minimum, 0)
A.reverse()
maximum = A.index(max (A))
A.insert(maximum, 0)
A.reverse()
print (*A)

#задача 4

print ("\nЗадача 4")
N = 5
A = [-5,4,-1,2,-6]
i = 0
A.reverse()
while i < len(A):
    if A[i]<0:
        A.insert(i,0)
        i+=2
    else:
        i+=1
A.reverse()
print (*A)

#задача 5

print ("\nЗадача 5")
N = 5
A = [-5,4,-1,2,-6]
i = 0
while i < len(A):
    if A[i]>0:
        A.insert(i,0)
        i+=2
    else:
        i+=1
print (*A)
