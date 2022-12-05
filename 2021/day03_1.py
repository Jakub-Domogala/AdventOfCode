def binToDec(tab):
    result = 0
    exp = 0
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == 1:
            result += (2**exp)
        print(result, i)
        exp += 1
    return result

with open('input_day3_1.txt') as fp:
    l = 12
    tab = [0] * l
    countLines = 0
    for line in fp:
        for i in range(0,l):
            tab[i] += int(line[i])
        countLines += 1
    for i in range(0,l):
        if tab[i] < countLines / 2:
            tab[i] = 0
        else:
            tab[i] = 1

    gamma = binToDec(tab)
    print(tab)
    for i in range(0,l):
        tab[i] *= -1
        tab[i] += 1
    print(tab)
    epilsion = binToDec(tab)

    print(gamma, epilsion)

    print(gamma * epilsion)


