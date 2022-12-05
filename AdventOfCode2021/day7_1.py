from math import inf

def main():
    input = "input_day7_1.txt"
    line = 0
    with open(input) as fp:
        line = [int(i) for i in fp.readline().split(',')]
    print(line)
    best = inf
    print(max(line), min(line), len(line))
    for i in range(min(line), max(line)+1):
        fuel = 0
        for j in line:
            if j != i:
                xd = abs(j - i)
                fuel += (1 + xd)/2*xd
        if fuel < best:
            best = fuel
    print(best)







if __name__ == "__main__":
    main()
