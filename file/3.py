# Дан файл вещественных чисел. Создать два новых файла, первый из которых содержит
# элементы исходного файла с нечетными номерами (1, 3, ...), а второй — с четными (2, 4, ...).

import random

def Write2File(fname,line):
    try:
        f = open(fname, "a")
        try:
            f.write(line)
        finally:
            f.close()
    except IOError:
        print('Write error: ', fname)

f_source = "file_start_source.txt"
f_odd = "file_odd.txt"
f_even = "file_even.txt" # четный
line = ""
k = 1
try:
    with open(f_source, 'r') as f:
        for line in f:
            l = int(line)
            if l % 2 == 0:
                Write2File(f_even, line)
            else:
                Write2File(f_odd, line)
    print("program exit")
except IOError:
    print('Open error: ', f_source)

