def sign(a):
    if a == 0:
        return 0
    if a < 0:
        return -1
    return 1

countmax = [0] * 4 # U R D L
direction = [] # U R D L
stepsize = []

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
    # print(countmax)

middle = max(countmax)
n = middle * 2 + 1 # n is oversized but we don't care
tmp = middle
visited = [[False for _ in range(n)] for _ in range(n)]
visited[middle][middle] = True
# starting position for head and tail
xh, yh, xt, yt = tmp, tmp, tmp, tmp
# print("dir", direction)

def update_tail():
    global xh, yh, xt, yt, visited
    if ((xh - xt)**2 + (yh - yt)**2)**0.5 > 1.5: # 1.5 is just something bigger than sqrt(2) and smaller than 2
        xt += sign(xh - xt)
        yt += sign(yh - yt)
        
        visited[xt][yt] = True

def update_head(dir):
    global xh, yh
    # print(xt, yt, xh, yh)
    # print(-1*(dir-2) if dir%2==1 else 0, -1*(dir-1) if dir%2==0 else 0)
    xh += -1*(dir-2) if dir%2==1 else 0
    yh += -1*(dir-1) if dir%2==0 else 0

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
        update_head(direction[i])
        update_tail()
    # if stop > 50:
    #     break

result = count_true()

print(result)

