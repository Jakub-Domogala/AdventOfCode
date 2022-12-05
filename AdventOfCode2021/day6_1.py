


def main():
    input = "input_day6_1.txt"
    list = [0]*9
    with open(input) as fp:
        line = fp.readline()
        print(line)
        print(len(line))
        for i in range(0, len(line), 2):
            list[int(line[i])] += 1
    print(list)
    tmp1 = 0
    tmp2 = 0
    time  = 256
    for day in range(1,time+1):
        for i in range(8, -1, -1):
            if i == 0:

                list[6] += tmp1
            else:
                tmp2 = list[i-1]
                list[i-1] = tmp1
                tmp1 = tmp2

        print(day, list, tmp1)
    result = tmp1
    for i in range(8):
        result += list[i]
    print(result)

if __name__ == "__main__":
    main()
