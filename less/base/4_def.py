#Функции представляют блок кода, который выполняет определенную задачу и который можно повторно использовать в других частях программы.

""""
--------------------------------
def say_hello():
    print("Hello")

say_hello()
say_hello()
--------------------------------------------------------------
mass = [красивый, ленивый]
mass2 = [красивый, ленивый]
#  используем функцию с параметрами:
def say_hello(name, mass):

    print("Hello,",mass.random , name)

say_hello("Tom", mass)
say_hello("Bob")
--------------------------------------------------------------------
def say_hello(name="Tom"):
    print("Hello,", name)

say_hello()
say_hello("Bob")
---------------------------------------------------------------------
#Неопределенное количество параметров

def sum(*params):
    result = 0
    for n in params:
        result += n
    return result

sum_num1 = sum(1, 2, 3, 4, 5)  # 15
sumNum2 = sum(3, 4, 5, 6)  # 18
print(sumOfNumbers1)
print(sumOfNumbers2)
------------------------------------------------------------------------

#Возвращение результата

def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result
 
result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
-----------------------------------------------------------------------------------------
В программе может быть определено множество функций.
И чтобы всех их упорядочить, хорошей практикой считается добавление специальной функции main,
в которой потом уже вызываются другие функции:

def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")
 
 
def say_hello(name):
    print("Hello,", name)
     
     
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result
 
# Вызов функции main
main()
-----------------------------------------------------------------
# Видимость переменных
name = "Tom"
 
def say_hi():
    print("Hello", name)
 
def say_bye():
    name = "Bob"
    print("Good bye", name)
 
say_hi()  # Hello Tom
say_bye()  # Good bye Bob

-----------------------------------------------------------------------------
# модули

!!! account.py

def calculate_income(rate, money, month):
    if money <= 0:
        return 0
  
    for i in range(1, month+1):
        money = round(money + money * rate / 100 / 12, 2)
    return money
    
!!! hello.py

#! Программа Банковский счет
import account
 
rate = int(input("Введите процентную ставку: "))
money = int(input("Введите сумму: "))
period = int(input("Введите период ведения счета в месяцах: "))
  
result = account.calculate_income(rate, money, period)
print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
        "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)
        
!!! from account import calculate_income
-----------------------------------------------------------------

Модуль random
Модуль random управляет генерацией случайных чисел. Его основные функции:
random(): генерирует случайное число от 0.0 до 1.0
randint(): возвращает случайное число из определенного диапазона
randrange(): возвращает случайное число из определенного набора чисел
shuffle(): перемешивает список
choice(): возвращает случайный элемент списка

---------------------------------------------------------------------
import random
 
number = random.random()  # значение от 0.0 до 1.0
print(number)
number = random.random() * 100  # значение от 0.0 до 100.0
print(number)
----------------------------------------------------------------
import random
 
number = random.randint(20, 35)  # значение от 20 до 35
print(number)
---------------------------------------------------------------------
import random
 
number = random.randrange(10)  # значение от 0 до 10
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9, 10
print(number)
number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8, 10
print(number)
--------------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  
rand_num = random.choice(numbers)
print(random_number)

# Список

numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # 1
print(numbers[2])   # 3
print(numbers[-3])  # 3
 
numbers[0] = 125  # изменяем первый элемент списка
print(numbers[0])   # 125
-------------------------------------------------------------------------------------------------
numbers = [5] * 6  # [5, 5, 5, 5, 5, 5]
print(numbers)
--------------------------------------------------------------------------------------------
ОТПРАВИТЬ

numbers = list(range(10))
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)      # [10, 8, 6, 4]



------------------------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = list(range(1, 10))
---------------------------------------------------------------------------------------------------
Список необязательно должен содержать только однотипные объекты. 
Мы можем поместить в один и тот же список одновременно строки, числа, объекты других типов данных:
objects = [1, 2.6, "Hello", True]
-------------------------------------------------------------------------------------------------
companies = ["Microsoft", "Google", "Oracle", "Apple"]
for item in companies:
    print(item)

------------------------------------------------------------------------------------------


companies = ["Microsoft", "Google", "Oracle", "Apple"]
i = 0
while i < len(companies):
    print(companies[i])
    i += 1
-------------------------------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers2 = list(range(1,10))
if numbers == numbers2:
    print("numbers equal to numbers2")
else:
    print("numbers is not equal to numbers2")





                       <<<<-------------------------------------------------------------------------------------->>>>>

users = ["Tom", "Bob"]
 
# добавляем в конец списка
users.append("Alice")  # ["Tom", "Bob", "Alice"]

# добавляем на вторую позицию
users.insert(1, "Bill")          # ["Tom", "Bill", "Bob", "Alice"]

# получаем индекс элемента
i = users.index("Tom")

# удаляем по этому индексу
removed_item = users.pop(i)            # ["Bill", "Bob", "Alice"]
 
last_user = users[-1]
# удаляем последний элемент
users.remove(last_user)           # ["Bill", "Bob"]
 
print(users)
 
# удаляем все элементы
users.clear()
-------------------------------------------------------------------------------------------------
>> Проверка наличия элемента

companies = ["Microsoft", "Google", "Oracle", "Apple"]
item = "Oracle"  # элемент для удаления
if item in companies:
    companies.remove(item)
 
print(companies)
-----------------------------------------------------------------------------
>> Подсчет вхождений

users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
 
users_count = users.count("Tom")
print(users_count)      # 3
-----------------------------------------------------------------------------
>> Сортировка

users = ["Tom", "Bob", "Alice", "Sam", "Bill"]
 
users.sort()
print(users)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]
-----------------------------------------------------------------------------
>> Минимальное и максимальное значения
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21
------------------------------------------------------------------------------

users1 = ["Tom", "Bob", "Alice"]
users2 = users1
users2.append("Sam")
# users1 и users2 указывают на один и тот же список
print(users1)   # ["Tom", "Bob", "Alice", "Sam"]
print(users2)   # ["Tom", "Bob", "Alice", "Sam"]
------------------------------------------------------------------------------
>> Соединение списков

users1 = ["Tom", "Bob", "Alice"]
users2 = ["Tom", "Sam", "Tim", "Bill"]
users3 = users1 + users2
print(users3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]
-------------------------------------------------------------------------------

------------------------------------------------------------------------------
-------------------------------------------------------------------------------



"""