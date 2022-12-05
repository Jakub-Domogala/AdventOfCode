import re

def is_full_overlap(t):
    ax, bx, ay, by = t
    if ax <= ay and bx >= by or ax >= ay and bx <= by:
        return True
    return False

def is_overlap(t):
    if is_full_overlap(t):
        return True
    ax, bx, ay, by = t
    if ay <= ax <= by or ay <= bx <= by:
        return True
    return False

with open("input4.txt") as file:
    overlap_sum = 0
    counter = 0
    for line in file:
        line = line.replace("\n", "")
        trange = re.findall(r'\d+', line)
        for i in range(len(trange)):
            trange[i] = int(trange[i])
        # print(trange)
        if is_overlap(trange):
            # print("yes")
            overlap_sum += 1
        counter += 1
    print(overlap_sum)
    # print(counter)
