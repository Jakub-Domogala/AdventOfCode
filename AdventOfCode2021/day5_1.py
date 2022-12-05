from math import inf
from pprint import pprint

input = "input_day5_1.txt"

def mPrint(Map):
    for line in Map:
        print(line)



def main():
    Cords = []
    with open(input) as fp:
        i = 0
        while 1:
            line = fp.readline().split(',')
            if len(line) < 3:
                break
            singleCord = [int(line[0]), None, None, int(line[2])]
            singleCord[1], singleCord[2] = line[1].split('->')
            singleCord[1] = int(singleCord[1])
            singleCord[2] = int(singleCord[2])
            print(singleCord)
            Cords.append(singleCord)
    print(Cords)
    n = len(Cords)
    highX = -inf
    highY = -inf
    lowX = inf
    lowY = inf
    for i in range(n):
        for j in range(2):
            if highX < Cords[i][2*j]: highX = Cords[i][2 * j]
            if lowX > Cords[i][2*j]: lowX = Cords[i][2*j]
            if highY < Cords[i][2*j + 1]: highY = Cords[i][2*j + 1]
            if lowY > Cords[i][2*j + 1]: lowY = Cords[i][2*j + 1]
    print(highX - lowX, highY - lowY)
    print(highX, highY)


    Map = [[0]*(highY + 1) for _ in range(highX + 1)]
    for cNum in range(n):
        if Cords[cNum][0] != Cords[cNum][2] and Cords[cNum][1] != Cords[cNum][3]:
            continue
        if Cords[cNum][0] < Cords[cNum][2]:
            x = Cords[cNum][0]
            while True:
                Map[x][Cords[cNum][1]] += 1
                if x >= Cords[cNum][2]:
                    break
                x += 1
        elif Cords[cNum][0] > Cords[cNum][2]:
            x = Cords[cNum][2]
            while True:
                Map[x][Cords[cNum][1]] += 1
                if x >= Cords[cNum][0]:
                    break
                x += 1
        elif Cords[cNum][1] < Cords[cNum][3]:
            y = Cords[cNum][1]
            while True:
                # if y > Cords[cNum][2] or y < 0:
                #     print(Cords[cNum][1]   , y)
                Map[Cords[cNum][0]][y] += 1
                if y >= Cords[cNum][3]:
                    break
                y += 1
        elif Cords[cNum][1] > Cords[cNum][3]:
            y = Cords[cNum][3]
            while True:
                Map[Cords[cNum][0]][y] += 1
                if y >= Cords[cNum][1]:
                    break
                y += 1
        else:
            Map[Cords[cNum][0]][Cords[cNum][1]] += 1

    result = 0

    for i in range(highX + 1):
        for j in range(highY + 1):
            if Map[i][j] > 1:
                result += 1
    print(result)











if __name__ == "__main__":
    main()
