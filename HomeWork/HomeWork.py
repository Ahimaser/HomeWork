"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
import math
print("Задача 1\n")
seasonsList = ['winter', 'spring', 'summer', 'autumn']
seasonsDict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}
month = int(input("Введите номер месяца: "))
month = month + 1 if month < 12 else 1
seasonNumber = math.ceil(month / 3) - 1
print(seasonsList[seasonNumber])
print(seasonsDict[seasonNumber])

"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

def Divide(a, b):
    return a / b

print("Задача 2")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
try:
    print(Divide(a, b))
except ZeroDivisionError:
    print("Делить на 0 нельзя!")

"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
print("Задача 3")

def pers_func(name, surname, year, city, email, number):
    print(f"{name} {surname} {year} года рождения, проживает в городе\n {city}, email: {email}, телефон: {number}")


pers_func(name='Андрей', surname='Андреев', year=1987, city='Москва',
          email='ggg@gmail.com', number=1111111111)

"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
print("Задача 4")
def summVersion1(a, b, c):
    list_1 = [a, b, c]
    list_1.sort()
    return list_1[1] + list_1[2]


def summVersion2(a, b, c):
    list_1 = [a, b, c]
    for i in range(len(list_1) - 1):
        pos = i
        for j in range(i + 1, len(list_1)):
            if list_1[j] < list_1[pos]:
                pos = j
        temp = list_1[i]
        list_1[i] = list_1[pos]
        list_1[pos] = temp
    return list_1[1] + list_1[2]


print(summVersion1(1, 4, 2))
print(summVersion2(1, 4, 2))

