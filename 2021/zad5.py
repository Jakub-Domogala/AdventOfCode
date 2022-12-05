#zad5
N = input("Wpisz N: ")
k = input("Wpisz k: ")
N = int(N)
k = int(k)
table = [[0]*N for i in range(N)]
for i in range(N):
    table[i][i] = k
print(table)