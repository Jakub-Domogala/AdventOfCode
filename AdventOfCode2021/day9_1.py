from math import inf
from pprint import pprint

def spreadBasin(matrix, basins, adja, x, y, ind):
    count = 0
    for i in range(4):
        nx = x + adja[i][0]
        ny = y + adja[i][1]

        if nx >= 0 and nx < len(basins) and ny >= 0 and ny < len(basins[0]):
            if not basins[nx][ny] and matrix[nx][ny] < 9:
                count += 1

                basins[nx][ny] = ind
                count += spreadBasin(matrix, basins, adja, nx, ny, ind)
                #print(count, "count--------")
    return count





def main():
    input = 'input_day9_1.txt'

    matrix = []
    # Read file
    with open(input) as fp:
        while True:
            line = fp.readline()
            if len(line) < 10:
                break
            tab = [line[i] for i in range(len(line) - 1 )]
            matrix.append(tab)
    # Matrix to int
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j])
    # Create basin marks table
    basins = [[None] * len(matrix[0]) for i in range(len(matrix))]
    result = 0

    # Table of possible moves
    adja = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    ind_basin = 1
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            is_low = True
            for k in range(4):
                x = i + adja[k][0]
                y = j + adja[k][1]
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                    if matrix[x][y] <= matrix[i][j]:
                        is_low = False
            if is_low:
                sizes.append(spreadBasin(matrix, basins, adja, i, j, ind_basin))
                ind_basin += 1
    print(sizes)
    sizes.sort()
    sizes.reverse()
    print(sizes)
    print(sizes[0] * sizes[1] * sizes[2])
if __name__ == "__main__":
    main()
