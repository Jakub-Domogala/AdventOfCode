from math import inf

def main():
    input = "input_day8_1.txt"
    line = 0
    with open(input) as fp:
        count = 0
        sum = 0
        while True:
            line = fp.readline()
            #print(line)
            if len(line) < 10:
                break
            line = line.split(' ')
            line[14] = line[14].removesuffix('\n')
            print(line)
                #   seg[ a    b    c    d    e    f    g ]
            segments = [['a', 'b', 'c', 'd', 'e', 'f', 'g'] for i in range(7)]

            print(segments)
            for i in range(10): #find 1
                if len(line[i]) == 2:
                    segments[2] = [line[i][0], line[i][1]]
                    segments[5] = segments[2]
                    for j in range(7):
                        if j != 2 and j != 5:
                            segments[j].remove(line[i][0])
                            segments[j].remove(line[i][1])
                    break
            print(segments)

            for i in range(10): #find 7
                if len(line[i]) == 3:
                    for j in range(3):
                        if line[i][j] not in segments[2]:
                            segments[0] = [line[i][j]]
                            break
                    break
            for i in range(1,7):
                if segments[0][0] in segments[i]:
                    segments[i].remove(segments[0][0])
            print(segments, 'after 7')


            for i in range(10): #find 4
                if len(line[i]) == 4:
                    tab = []
                    for j in range(4):
                        if line[i][j] not in segments[2]:
                            tab.append(line[i][j])
                    segments[1] = segments[3] = tab
                    break
            for i in range(4,7,2):
                for j in range(2):
                    if segments[1][j] in segments[i]:
                        segments[i].remove(segments[1][j])
            print(segments)

            ind6 = None
            for i in range(10): #find 6
                if len(line[i]) == 6:
                    tab = []
                    for j in range(6):
                        tab.append(line[i][j])
                    if segments[2][0] not in tab or segments[2][1] not in tab:
                        if segments[2][0] not in tab:
                            segments[2] = [segments[2][0]]
                            segments[5].remove(segments[2][0])
                        else:
                            segments[2] = segments[2][1]
                            segments[5].remove(segments[2][0])
                        ind6 = i
                        break
            print(segments, 'after 6')
            ind9 = None
            for i in range(10): #find 9
                if len(line[i]) == 6 and i != ind6:
                    tab = []
                    for j in range(6):
                        tab.append(line[i][j])
                    for j in range(2):
                        if segments[4][j] not in tab:
                            segments[4] = [segments[4][j]]
                            break
                    ind9 = i
                if len(segments[4]) == 1: break
            print(segments, 'after 9')


            for i in range(10): #find 0
                if len(line[i]) == 6 and i != ind6 and i != ind9:
                    tab = []
                    for j in range(6):
                        tab.append(line[i][j])
                    for j in range(2):
                        if segments[3][j] not in tab:
                            segments[3] = [segments[3][j]]
                            break
                    break
            print(segments)
            segments[1].remove(segments[3][0])
            segments[6].remove(segments[4][0])
            print(segments)
            number = 0
            for i in range(11,15):
                number *= 10
                tab = []
                for j in range(len(line[i])):
                    tab.append(line[i][j])
                y = len(tab)
                if y == 2:
                    number += 1
                elif y == 5 and segments[4][0] in tab:
                    number += 2
                elif y == 5 and segments[2][0] in tab and segments[5][0] in tab:
                    number += 3
                elif y == 4:
                    number += 4
                elif y == 5 and segments[1][0] in tab:
                    number += 5
                elif y == 6 and segments[2][0] not in tab:
                    number += 6
                elif y == 3:
                    number += 7
                elif y == 7:
                    number += 8
                elif y == 6 and segments[4][0] not in tab:
                    number += 9

            print(number)
            sum += number


        print(sum)






if __name__ == "__main__":
    main()
