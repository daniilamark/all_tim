# Дан файл целых чисел. Создать новый файл, содержащий те же элементы, что и исходный файл, но в обратном порядке


import random

def CountF(fname):
    N = 0
    try:
        with open(fname, 'r') as f:
            for line in f:
                N += 1
                #print(N, ":", line)
    except IOError:
        return -1
    finally:
        return N

def GetLineN(fname, N):
    line = ""
    k = 0
    try:
        with open(fname, 'r') as f:
            for line in f:
                k += 1
                if k == N:
                    break
    except IOError:
        print('Open error: ', file1)
    return line.strip()


file1 = "file_1.txt"
file2 = "file_2.txt"
print("Input file: ", file1)
print("Output file: ", file2)
print()

N = CountF(file1)
print("Number of records:", N)
while N > 0:
    last_line = GetLineN(file1, N)
    try:
        f = open(file2, "a")
        try:
            f.write(last_line + "\n")
        finally:
            f.close()
    except IOError:
        print('Write error: ', file2)
    N -= 1