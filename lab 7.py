import math

#Задание к теме 7, задача 1

print ("Задача 1","\nВведите значение угла A в градусах: ")
A = float(input())
A = A * 180 / math.pi
print ("Значение угла A в радианах:", "{:.2f}".format (A))

#задача 2

print ("\nЗадача 2","\nВведите значение угла A в радианах: ")
A = float(input())
A = A / 180 * math.pi
print ("Значение угла A в градусах:", "{:.2f}".format (A))

#задача 3

print ("\nЗадача 3","\nВведите массу конфет (кг): ")
X = float (input())
print ("Введите цену в рублях за", "{:.2f}".format (X), "кг конфет: ")
A = float (input())
print ("Цену за сколько кг этих конфет Вы хотите узнать? ")
Y = float (input())
Price = A/X
print ("1 кг конфет в рублях стоит:", "{:.2f}".format (Price))
print ("Цена за", "{:.2f}".format (Y), "кг конфет в рублях: ", "{:.2f}".format (Y*Price))

#задача 4

print ("\nЗадача 4","\nВведите скорость первого автомобиля (км/ч): ")
V1 = float (input())
print ("Введите скорость второго автомобиля (км/ч): ")
V2 = float (input())
print ("Введите расстояние между автомобилями (ч): ")
S = float (input())
print ("Введите время: ")
T = float (input())
print ("Расстояние между автомобилями через ", "{:.2f}".format (T), "ч (км): ", "{:.2f}".format ((V1+V2)*T+S))

#задача 5

print ("\nЗадача 5","\nВведите значение A: ")
A = float (input())
print ("Введите значение B: ")
B = float (input())
print ("x =", "{:.2f}".format (-B/A))

#задача 6

print ("\nЗадача 6","\nВведите значение A1: ")
A1 = float (input())
print ("Введите значение B1: ")
B1 = float (input())
print ("Введите значение C1: ")
C1 = float (input())
print ("Введите значение A2: ")
A2 = float (input())
print ("Введите значение B2: ")
B2 = float (input())
print ("Введите значение C2: ")
C2 = float (input())
D = A1*B2 - A2*B1
print ("x = ","{:.2f}".format ((C1*B2 - C2*B1)/D))
print ("y = ","{:.2f}".format ((A1*C2 - A2*C1)/D))
