from math import inf

def main():
    input = "input_day8_1.txt"
    line = 0
    with open(input) as fp:
        count = 0
        while True:
            line = fp.readline()
            #print(line)
            if len(line) < 10:
                break
            line = line.split(' ')
            print(line)
            print(len(line[14]))
            line[14] = line[14].removesuffix('\n')
            print(len(line[14]))
            for i in range(11,15):
                d = len(line[i])
                if d == 2 or d == 3 or d == 4 or d == 7:
                    print(line[i])
                    count += 1
        print(count)










if __name__ == "__main__":
    main()
