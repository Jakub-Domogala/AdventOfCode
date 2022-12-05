from pprint import pprint

k = "klocek.txt"
m = "input_day3_1.txt"
input = k

def binToDec(tab):
    result = 0
    exp = 0
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == 1:
            result += (2**exp)
        exp += 1
    return result

oxyTab = []
coTab = []
l = 0
with open(input) as fp:
    for line in fp:
        l = len(line) -1
        break


with open(input) as fp:
    tab = [0]*l
    mind = 0
    for line in fp:
        for i in range(0,l):
            tab[i] = int(line[i])
        oxyTab.append([0] * l)

        for i in range(0,l):
            oxyTab[mind][i] = tab[i]
        mind += 1
    for i in oxyTab:
        coTab.append(i)


for pos in range(l):
    # OXYTAB part
    counter = 0
    for i in range(len(oxyTab)):
        counter += int(oxyTab[i][pos])
    if counter * 2 >= len(oxyTab):
        curr = 1
    else:
        curr = 0
    i = 0
    while i < len(oxyTab):
        if int(oxyTab[i][pos]) != curr:
            oxyTab.remove(oxyTab[i])
        else:
            i += 1
    if len(oxyTab) == 1:
        break
for pos in range(l):
    #COTAB part
    counter = 0
    for i in range(len(coTab)):
        counter += int(coTab[i][pos])
    if counter * 2 >= len(coTab):
        curr = 0
    else:
        curr = 1
    i = 0
    while i < len(coTab):
        if int(coTab[i][pos]) != curr:
            coTab.remove(coTab[i])
        else:
            i += 1
    if len(coTab) == 1:
        break
print(oxyTab)
print(coTab)

print(binToDec(oxyTab[0]) * binToDec(coTab[0]))




