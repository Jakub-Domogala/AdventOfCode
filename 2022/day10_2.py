cycle = 1
X = 1
height = 6
width = 40
screen = [[0 for _ in range(width)] for _ in range(height)]
def draw():
    global screen
    for i in range(len(screen)):
        print()
        for j in range(len(screen[i])):
            if screen[i][j] == 0:
                print(".", end="")
            else:
                print("#", end="")
    print()

def isMod():
    global cycle
    if cycle % 40 == 20:
        return True
    return False

def get_pos():
    global cycle
    return cycle//40, cycle%40

def update():
    global screen, X, cycle
    y, x = get_pos()
    if  X + 1 >= x >= X - 1:
        screen[y][x] += 1
        

with open("input10.txt") as file:
    for line in file:
        line = line.replace("\n", "").split(sep=" ")
        if len(line) == 1:
            update()
            cycle += 1
        if len(line) == 2:
            update()
            cycle += 1
            X += int(line[1])
            update()
            cycle += 1
draw()