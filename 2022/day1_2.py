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
max_elf2 = 0
max_elf3 = 0
for x in tab:
    if max_elf < x:
        max_elf = x

for x in tab:
    if max_elf2 < x and x != max_elf:
        max_elf2 = x

for x in tab:
    if max_elf3 < x and x != max_elf and x != max_elf2:
        max_elf3 = x


print(max_elf, max_elf2, max_elf3)
print(max_elf + max_elf2 + max_elf3)
tab.sort()

print(tab)


p = 1