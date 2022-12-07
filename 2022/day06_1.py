def is_all_diff(tab):
    for i in range(len(tab)-1):
        for j in range(i+1, len(tab)):
            if tab[i] is None or tab[i] == tab[j]:
                return False
    return True

def add_next(tab, elem):
    for i in range(1, len(tab)):
        tab[i-1] = tab[i]
    tab[len(tab) - 1] = elem
    return tab

index = 0
tab = [None] * 4
with open("input6.txt") as file:
    line = file.read()
    for i, x in enumerate(line):
        tab = add_next(tab, x)
        if is_all_diff(tab):
            print(i+1)
            break

        