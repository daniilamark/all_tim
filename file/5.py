# Дан файл целых чисел. Найти количество содержащихся в нем серий (то есть наборов последовательно расположенных одинаковых элементов).
# Например, для файла с элементами 1, 5, 5, 5, 4, 4, 5 результат равен 4.

import random
import numpy

def GenerateLine(fname):
    N = random.randrange(1,20)
    line = ""
    L = []
    for i in range(N):
        x = str(random.randint(1,3))
        L.append(x)
        line = ", ".join(L)
    try:
        f = open(fname, "w")
        try:
            f.write(line)
        finally:
            f.close()
    except IOError:
        print('Write error: ',fname)
    print(line)

f_source = "file16_source.txt"
GenerateLine(f_source)

try:
    with open(f_source,'r') as f:
        lines = f.readlines()
        lst = []
        print(lines)
        for line in reversed(lines):
            for i in line.split(", "):
                lst.append(int(i))
        print(lst)
        k = 1
        i_prev = lst[0]
        for  i in lst[1::]:
            if i != i_prev:
                k += 1
            i_prev = i
        print("Number of series:",k)

except IOError:
    print('Open error: ',f_source)