import random

N = random.randrange(100, 1000)
print("Число: ", N)

# 545
# ( 545 - 5 * 100 = 45 ) / 10


d2 = int(N / 100)
d1 = int((N - d2 * 100) / 10)
d0 = N % 10


print("Сотни: ", d2)
print("Десятки: ", d1)
print("Единицы: ", d0)

d2 != d1

ab = (d2 != d1)
bc = (d1 != d0)
ac = (d2 != d0)
x = ab and bc and ac
print("Все цифры данного числа различны: ", x)


