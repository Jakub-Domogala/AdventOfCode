def sign(a):
    if a == 0:
        return 0
    if a < 0:
        return -1
    return 1

countmax = [0] * 4 # U R D L
direction = [] # U R D L
stepsize = []
knots = []
k_amm = 10
# write down operations and count needed grid size
with open("input9.txt") as file:
    for line in file:
        line = line.replace("\n", "").split(sep=" ")
        line[1] = int(line[1])
        stepsize.append(line[1])
        if line[0] == "U":
            countmax[0] += line[1]
            direction.append(0)
        elif line[0] == "R":
            countmax[1] += line[1]
            direction.append(1)
        elif line[0] == "D":
            countmax[2] += line[1]
            direction.append(2)
        elif line[0] == "L":
            countmax[3] += line[1]
            direction.append(3)

middle = max(countmax)
n = middle * 2 + 1 # n is oversized but we don't care
tmp = middle
visited = [[False for _ in range(n)] for _ in range(n)]
visited[middle][middle] = True
# starting position for head and tail
xh, yh, xt, yt = tmp, tmp, tmp, tmp
# print("dir", direction)
for i in range(k_amm):
    knots.append([tmp, tmp])



def update_tail(xh, yh, xt, yt, visited, isLast):
    global k_amm
    if ((xh - xt)**2 + (yh - yt)**2)**0.5 > 1.5: # 1.5 is just something bigger than sqrt(2) and smaller than 2
        xt += sign(xh - xt)
        yt += sign(yh - yt)
    if isLast:
        visited[xt][yt] = True
    return [xt, yt]

def update_head(dir, knots):
    knots[0][0] += -1*(dir-2) if dir%2==1 else 0
    knots[0][1] += -1*(dir-1) if dir%2==0 else 0
    return knots[0]

def count_true():
    global visited
    cnt = 0
    for x in visited:
        for y in x:
            if y:
                cnt += 1
    return cnt
    

stop = 0
for i, x in enumerate(stepsize):
    for j in range(x):
        stop += 1
        knots[0] = update_head(direction[i], knots)
        print(knots)
        for k in range(1, k_amm):
            if k == k_amm - 1:
                knots[k] = update_tail(knots[k-1][0], knots[k-1][1], knots[k][0], knots[k][1], visited, True)
            else:
                knots[k] = update_tail(knots[k-1][0], knots[k-1][1], knots[k][0], knots[k][1], visited, False)

result = count_true()

print(result)

