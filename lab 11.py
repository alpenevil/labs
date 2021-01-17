import math

# Задание к теме 11, задача 1

print("Задача 1", "\nВведите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
if A != B:
    A = max(A, B)
    B = max(A, B)
else:
    A = 0
    B = 0
print("A =", A, "\nB =", B)

# задача 2

print("\nЗадача 2", "\nВведите A: ")
A = int(input())
print("Введите B: ")
B = int(input())
print("Введите C: ")
C = int(input())
if A >= B >= C:
    print("Сумма двух наибольших из них: ", A + B)
elif B >= C >= A:
    print("Сумма двух наибольших из них: ", C + B)
elif A >= C >= B:
    print("Сумма двух наибольших из них: ", C + A)

# задача 3

print("\nЗадача 3", "\nВведите Ax: ")
Ax = int(input())
print("Введите Ay: ")
Ay = int(input())
print("Введите Bx: ")
Bx = int(input())
print("Введите By: ")
By = int(input())
print("Введите Cx: ")
Cx = int(input())
print("Введите Cy: ")
Cy = int(input())
AC = sqrt((Cx - Ax) ** 2 + (Cy - Ay) ** 2)
AB = sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
if AB > AC:
    print("Точка C расположена ближе к A, AC =", AC)
elif AB < AC:
    print("Точка B расположена ближе к A, AB =", AB)
else:
    print("Точки расположены на одинаковом расстоянии, AB = BC =", AB)

# задача 4

print("\nЗадача 4", "\nВведите x: ")
x = int(input())
print("Введите y: ")
y = int(input())
if x > 0 and y > 0:
    print("Точка расположена в I четверти")
elif x < 0 and y > 0:
    print("Точка расположена во II четверти")
elif x < 0 and y < 0:
    print("Точка расположена в III четверти")
elif x > 0 and y < 0:
    print("Точка расположена в IV четверти")
else:
    print("Точка находится на координатной оси")

# задача 5

print("\nЗадача 5", "\nВведите число: ")
A = int(input())
if A > 0 and A % 2 == 0:
    print("Положительное четное число")
elif A > 0 and A % 2 != 0:
    print("Положительное нечетное число")
elif A < 0 and A % 2 == 0:
    print("Отрицательное четное число")
elif A < 0 and A % 2 != 0:
    print("Отрицательное нечетное число")
else:
    print("Нулевое число")

# задача 6

print("\nЗадача 6", "\nВведите число: ")
A = int(input())
if A // 100 > 0 and A % 2 == 0:
    print("Трехзначное четное число")
elif A // 100 > 0 and A % 2 != 0:
    print("Трехзначное нечетное число")
elif A // 10 > 0 and A % 2 == 0:
    print("Двузначное четное число")
elif A < 0 and A % 2 != 0:
    print("Двузначное нечетное число")
elif A % 2 == 0:
    print("Однозначное четное число")
elif A % 2 != 0:
    print("Однозначное нечетное число")
