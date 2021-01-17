import math
#Задание к теме 5, задача 1
x1 = 3.1
x2 = 2.5
y1 = 5.5
y2 = -6.3
print ("Расстояние между двумя точками = ", sqrt((x2-x1)**2+(y2-y1)**2))
#Задача 2
A = 3
B = 14
C = -1
print ("AB = ", abs(max(A,B)-min(A,B)), "; AC = ", abs(max(A,C)-min(A,C)), "; BC = ", abs(max(C,B)-min(C,B)), "; sum = ",abs( max(A,B,C)-min(A,B,C)))

#Задача 3
A = 3
B = 14
C = 7
print ("AC*CB = ", max(A,C)-min(A,C)*max(C,B)-min(C,B) )

#Задача 4
x1 = 3
x2 = 0
y1 = 1
y2 = 0

print ("S прямоугольника = ", abs(max(x1,x2)-min(x1,x2))*abs(max(y1,y2)-min(y1,y2)), "; P прямоугольника = ", (abs(max(x1,x2)-min(x1,x2))+abs(max(y1,y2)-min(y1,y2))*2))

#Задача 5
a1 = -1
b1 = -17
c1 = -7
a2 = 14
b2 = 2
c2 = 4
AB = sqrt ((b1-a1)**2 + (b2-a2)**2)
BC = sqrt ((c1-b1)**2 + (c2-b2)**2)
CA = sqrt ((a1-c1)**2 + (a2-c2)**2)
P = AB+BC+CA
p = P/2
S = sqrt(p*(p - AB)*(p - BC)*(p - CA))
print ("P треугольника = ","{:.2f}".format (P) , "; S треугольнока = ", "{:.2f}".format (S) )
