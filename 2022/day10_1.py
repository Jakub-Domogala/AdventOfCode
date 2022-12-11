cycle = 1
X = 1
sig_sum = 0
def isMod():
    global cycle
    if cycle % 40 == 20:
        return True
    return False

with open("input10.txt") as file:
    for line in file:
        print(X)
        line = line.replace("\n", "").split(sep=" ")
        if isMod():
            # print(sig_sum, X, cycle)
            sig_sum += X * cycle
        if len(line) == 1:
            cycle += 1
        if len(line) == 2:
            cycle += 1
            if isMod():
                sig_sum += X * cycle
            X += int(line[1])
            cycle += 1
print(sig_sum)