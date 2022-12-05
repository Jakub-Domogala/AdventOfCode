import re

# get stacks
amount_of_stacks = 9
stacks = [[] for _ in range(amount_of_stacks)]
with open("input5_1.txt") as file:
    overlap_sum = 0
    counter = 0
    for line in file:
        n = len(line)//4
        for i in range(0, n):
            if 65 <= ord(line[i*4 + 1]) <= 90:
                stacks[i].append(line[i*4 + 1])

for i in range(amount_of_stacks):
    stacks[i].reverse()

# perform operations
with open("input5_2.txt") as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        for i in range(3):
            numbers[i] = int(numbers[i])
        crates, fr, to = numbers
        fr -= 1
        to -= 1
        for _ in range(crates):
            stacks[to].append(stacks[fr].pop())
            
for i in range(amount_of_stacks):
    print(stacks[i].pop(), end="")

