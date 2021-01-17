import math


#Задание к теме 13, задача 1

print ("Задача 1","\nВведите цену кг конфет: ")
a = float(input())
for i in range (1, 11):
    print("Стоимость за", "{:.1f}".format (0.1*i), " кг конфет равна", "{:.2f}".format (a*i*0.1))

#задача 2

print ("\nЗадача 2","\nВведите число: ")
a = int(input())
k = 1
b = 1.1
for i in range (a):
        k*=b
        b+=0.1
print ("Произведение", a, "чисел","{:.4f}".format (k))

#задача 3

print ("\nЗадача 3","\nВведите число: ")
a = int(input())
k = 0
for i in range (1,a+1):
    k += i*2-1
    print ("Значение суммы:", k)

#задача 4

print ("\nЗадача 4","\nВведите вещественное число: ")
A = float(input())
print ("Введите целое число:")
N = int(input())
k = 1
for i in range (N+1):
    k += A**i
print ("Сумма равна:", "{:.2f}".format (k))

#задача 3

print ("\nЗадача 5","\nВведите вещественное число: ")
A = float(input())
print ("Введите целое число:")
N = int(input())
k = 1
b = 1
for i in range (1, N+1):
    b = b*A*(-1)
    k += b
print ("Сумма равна:", "{:.2f}".format (k))
