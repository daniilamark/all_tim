# Дан файл вещественных чисел. Найти среднее арифметическое его элементов.
import random
import numpy


def EmptyFile(fname):
    open(fname, 'w').close()


def GenerateLine(fname):
    EmptyFile(f_source)
    N = random.randrange(1, 20)
    line = ""
    L = []
    for i in range(N):
        x = format(random.uniform(-10, 10), '.1f')
        L.append(x)
        line = "; ".join(L)
    try:
        f = open(fname, "w")
        try:
            f.write(line)
        finally:
            f.close()
    except IOError:
        print('Write error: ', fname)
    print(line)


f_source = "file14_source.txt"
GenerateLine(f_source)

try:
    with open(f_source, 'r') as f:
        lines = f.readlines()
        l_float = []
        print(lines)
        for line in reversed(lines):
            for i in line.split("; "):
                l_float.append(float(i))
        print(l_float)
        x = numpy.mean(l_float)
        print("Mean:", format(x, '.3f'))

except IOError:
    print('Open error: ', f_source)