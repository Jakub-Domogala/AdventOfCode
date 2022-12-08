tree_heights = []


# Get all heights to the table
with open("input8.txt") as file:
    first = True
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        tree_heights.append([int(line[0])])
        for i in range(1, len(line)):
            tree_heights[j].append(int(line[i]))

# Operations on table

n = len(tree_heights)

def calc_scenic(x, y, h):
    global tree_heights
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    for i in range(x-1, -1, -1):
        c1 += 1
        if tree_heights[i][y] >= h:
            break
    for j in range(y-1, -1, -1):
        c2 += 1
        if tree_heights[x][j] >= h:
            break
    for i in range(x+1, len(tree_heights)):
        c3 += 1
        if tree_heights[i][y] >= h:
            break
    for j in range(y+1, len(tree_heights)):
        c4 += 1
        if tree_heights[x][j] >= h:
            break
    score = c1 * c2 * c3 * c4
    print(c1, c2, c3, c4)
    return score

def get_most_scenic_tree():
    global tree_heights
    best = 0
    for i in range(n):
        for j in range(n):
            best = max(calc_scenic(i, j, tree_heights[i][j]), best)
    return best


result = get_most_scenic_tree()
print(result)