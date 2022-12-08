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
visible = [[False for _ in range( len(tree_heights))] for _ in range(len(tree_heights[0]))]

n = len(visible)

def mark_visible_trees(tree_heights):
    global visible
    for i in range(n):
        h = -1
        for j in range(n):
            if tree_heights[i][j] > h:
                visible[i][j] = True
                h = tree_heights[i][j]
    for i in range(n):
        h = -1
        for j in range(n):
            if tree_heights[n - 1 - i][n - 1 - j] > h:
                visible[n - 1 - i][n - 1 - j] = True
                h = tree_heights[n - 1 - i][n - 1 - j]
    for i in range(n):
        h = -1
        for j in range(n):
            if tree_heights[j][i] > h:
                visible[j][i] = True
                h = tree_heights[j][i]
    for i in range(n):
        h = -1
        for j in range(n):
            if tree_heights[n - 1 - j][n - 1 - i] > h:
                visible[n - 1 - j][n - 1 - i] = True
                h = tree_heights[n - 1 - j][n - 1 - i]

 
def count_visibility():
    ctr = 0
    for i in range(n):
        for j in range(n):
            if visible[i][j]:
                ctr += 1
    return ctr

mark_visible_trees(tree_heights)
result = count_visibility()
print(result)