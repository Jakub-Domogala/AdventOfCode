from itertools import count
from math import *

input1 = "input_day13_1_1.txt"
input2 = "input_day13_1_2.txt"
cords = {}
folds = []



def fold_on_x(table, fold_x):
    nx = len(table[0])
    ny = len(table)
    for x in range(fold_x+1, nx):
        for y in range(ny):
            if table[y][x]:
                table[y][2*fold_x - x] = True
                table[y][x] = False

def fold_on_y(table, fold_y):
    nx = len(table[0])
    ny = len(table)
    for x in range(nx):
        for y in range(fold_y, ny):
            if table[y][x]:
                table[2*fold_y - y][x] = True
                table[y][x] = False

            
big_x = 0
big_y = 0

with open(input1) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip().split(",")
        line = (int(line[0]), int(line[1]))
        big_x = max(big_x, line[0])
        big_y = max(big_y, line[1])
        cords[line] = True

big_x = ceil(big_x/2) * 2
big_y = ceil(big_y/2) * 2
print(big_x, big_y)
table = [[(i, j) in cords for i in range(big_x+1)] for j in range(big_y+1)]



def counter(table):
    cnt = 0
    for i in table:
        for j in i:
            if j:
                cnt += 1
    print(cnt)

counter(table)

fold_on_x(table, 655)
counter(table)

fold_on_y(table, 447)
counter(table)

fold_on_x(table, 327)
counter(table)

fold_on_y(table, 223)
counter(table)

fold_on_x(table, 163)
counter(table)

fold_on_y(table, 111)
counter(table)

fold_on_x(table, 81)
counter(table)

fold_on_y(table, 55)
counter(table)

fold_on_x(table, 40)
counter(table)

fold_on_y(table, 27)
counter(table)

fold_on_y(table, 13)
counter(table)

fold_on_y(table, 6)
counter(table)

for j in range(7):
    for i in range(41):
        print("#" if table[j][i] == True else "_" , end="")
    print()
