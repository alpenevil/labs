import math

#Задание к теме 12, задача 1

print ("Задача 1","\nВведите день: ")
day = int(input())
days = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое", "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое", "тридцатое", "двадцать", "тридцать"]
print("Введите месяц: ")
month = int(input())
months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
if day == 20:
    print(days[19], months [month-1])
elif day == 30:
    print(days[20], months [month-1])
elif day < 20:
    print(days [day-1], months [month-1])
elif 30 > day > 20:
    print (days[21], days[day%10-1], months [month-1])
elif 30 < day:
    print (days[22], days[day%10-1], months [month-1])

#задача 2

print ("\nЗадача 2","\nВведите направление робота: ")
direction = input()
directions = ["C", "З", "Ю", "В"]
print("Введите команду: ")
task = int(input())
a = directions.index(direction)
print ("Направление робота:", directions[(a+task)%4])

#задача 3

print ("\nЗадача 3","\nВведите количество заданий: ")
task = int(input())
tasks = ["одно", "два", "три", "четыре", "пять", "шесть", "седьмь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
dec = ["двадцать", "тридцать", "сорок"]
if task > 19:
    if task%10 == 0:
        print(dec[(task//10)-2], "учебных заданий")
    elif task%10 == 1:
        print (dec[(task//10)-2], tasks[(task%10)-1], "учебное задание")
    elif task%10 < 5:
        print (dec[(task//10)-2], tasks[(task%10)-1], "учебных задания")
    elif task%10 > 4:
        print(dec[(task//10)-2], tasks[(task%10)-1], "учебных заданий")
else:
    if task > 4:
        print(tasks [task-1], "учебных заданий")
    elif task == 1:
        print (tasks [task-1], "учебное задание")
    elif task < 5:
        print (tasks[task-1], "учебных задания")
#задача 4

print ("\nЗадача 4","\nВведите число: ")
number = int(input())
a = ["один", "два", "три", "четыре", "пять", "шесть", "седьмь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
b = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдясят", "семьдесят", "восемьдесят", "девяносто"]
c = ["сто", "двести", "триста","четыреста","пятьсот", "шестьсот","семьсот","восемьсот","девятьсот"]
if number%100 == 0:
    print (c[number//100-1])
elif number%100//10 == 0:
    print (c[number//100-1], a[number%10-1])
elif number%10 == 0:
    print (c[number//100-1], b[number%100//10-1])
else:
    if number%100 < 20:
        print (c[number//100-1], a[number%100-1])
    else:
        print (c[number//100-1], b[number%100//10-1],a[number%10-1])
#задача 5

print ("\nЗадача 5","\nВведите год: ")
year = int(input())
colormale = ["белого", "черного", "зеленого", "красного", "желтого"]
colorfemale = [ "белой", "черной", "зеленой", "красной", "желтой"]
animal = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
if 1 < (year+8)%12 < 5:
    if year%10 == 0 or year%10 == 1:
        print ("год", colormale[0], animal [(year+8)%12])
    elif year%10 == 2 or year%10 == 3:
        print ("год", colormale[1], animal [(year+8)%12])
    elif year%10 == 4 or year%10 == 5:
        print ("год", colormale[2], animal [(year+8)%12])
    elif year%10 == 6 or year%10 == 7:
        print ("год", colormale[3], animal [(year+8)%12])
    elif year%10 == 8 or year%10 == 9:
        print ("год", colormale[4], animal [(year+8)%12])
else:
    if year%10 == 0 or year%10 == 1:
        print ("год", colorfemale[0], animal [(year+8)%12])
    elif year%10 == 2 or year%10 == 3:
        print ("год", colorfemale[1], animal [(year+8)%12])
    elif year%10 == 4 or year%10 == 5:
        print ("год", colorfemale[2], animal [(year+8)%12])
    elif year%10 == 6 or year%10 == 7:
        print ("год", colorfemale[3], animal [(year+8)%12])
    elif year%10 == 8 or year%10 == 9:
        print ("год", colorfemale[4], animal [(year+8)%12])
