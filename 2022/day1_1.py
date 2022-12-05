tab = []
tmp = 0
with open("input1.txt") as file:
    for line in file:
        if line == "\n":
            tab.append(tmp)
            tmp = 0
        else:
            tmp = tmp + int(line)

max_elf = 0

for x in tab:
    if max_elf < x:
        max_elf = x
print(max_elf)