# Дано имя файла целых чисел. Найти количество элементов, содержащихся в данном файле.
# Если файла с таким именем не существует, то вывести -1

# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod

N = 0
try:
    with open('integers.txt', 'r') as f:
        for line in f:
            N += 1
            # print(N, " => ", int(line))
except IOError:
    print("Файл не найден")
print("Количество элементов: ", N)