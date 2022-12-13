from queue import PriorityQueue
from math import inf
import time

tab = []
xs, ys, xe, ye = 0, 0, 0, 0
count = 0
with open("input12.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        tab.append([])
        for i, x in enumerate(line):
            if x == "E":
                tab[len(tab)-1].append(ord("z"))
                xe = i
                ye = count
            elif x == "S":
                tab[len(tab)-1].append(ord("a"))
                xs = i
                ys = count
            else:
                tab[len(tab)-1].append(ord(x))
        
        count += 1

que = PriorityQueue()
print(xs, ys, xe, ye)
def sort_of_dijkstra(tab, start, end):
    def is_in_range(x, y): # is in table range
        nonlocal tab
        if 0 <= y < len(tab) and 0 <= x < len(tab[0]):
            return True
    

    # Available moves to make: up, down, left, right,
    moves = (
        (1,0),
        (0,1),
        (-1,0),
        (0,-1)
    )

    que = PriorityQueue()

    ys, xs = start
    ye, xe = end

    visited = [[False for _ in range(len(tab[0]))] for _ in range(len(tab))]
    distance = [[inf for _ in range(len(tab[0]))] for _ in range(len(tab))]

    visited[ys][xs] = True
    distance[ys][xs] = 0

    que.put((0, ys, xs)) # steps ys xs
    cnt = 0
    while not que.empty():
        cost, y, x = que.get()

        for m in moves:
            newx = x + m[0]
            newy = y + m[1]
            if is_in_range(newx, newy) and tab[newy][newx] <= tab[y][x] + 1 and distance[newy][newx] > cost + 1:
                distance[newy][newx] = cost + 1
                que.put((cost + 1, newy, newx))
                # print(newx, newy)

        # for row in distance:
        #     for i in row:
        #         if i == inf:
        #             print(".", end=" ")
        #         else:
        #             print(i, end=" ")
        #     print()
        # print()

        # time.sleep(0.1)


    return distance[ye][xe]

result = inf
# Could use modification of Belman ford but its similiar complexity in this case so we use dijkstra for each "a"
for i in range(len(tab)): 
    for j in range(len(tab[0])):
        if tab[i][j] == ord("a"):
            result = min(result, sort_of_dijkstra(tab, (i, j), (ye, xe)))

print(result)

