"""
choice = "Y"

while choice.lower() == "y":
    print("Привет")
    choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
print("Работа программы завешена")

"""

"""
#! Программа по вычислению факториала
 
num = int(input("Введите число: "))
i = 1
fact = 1

while i <= number:
    factorial *= i
    i += 1
print("Факториал числа", number, "равен", factorial)
"""

"""
#! Программа по вычислению факториала
 
number = int(input("Введите число: "))
fac = 1
for i in range(1, number+1):
    factorial *= i
print("Факториал числа", number, "равен", factorial)
"""

"""
range(stop): возвращает все целые числа от 0 до stop
range(start, stop): возвращает все целые числа в промежутке от start (включая) до stop (не включая).
range(start, stop, step): возвращает целые числа в промежутке от start (включая) до stop (не включая), которые увеличиваются на значение step

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(5, 0, -1)     # 5, 4, 3, 2, 1
"""

"""
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")
"""

"""
#! Программа Обменный пункт
 
print("Для выхода нажмите Y")
 
while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    cache = round(money / 74,17)
    print("К выдаче", cache, "долларов")
 
print("Работа обменного пункта завершена")
"""

"""
#! Программа Обменный пункт
 
print("Для выхода нажмите Y")
 
while True:
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    if money < 0:
        print("Сумма должна быть положительной!")
        continue
    cache = round(money / )
    print("К выдаче", cache, "долларов")
 
print("Работа обменного пункта завершена")
"""

