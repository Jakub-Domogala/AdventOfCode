
import copy


def main():
    input = "input_day12_1.txt"
    table = []
    # Read file
    print(input)
    with open(input) as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip().split("-")
            line2 = [line[1], line[0]]
            table.append(line)
            table.append(line2)
            # print(line)
    # for i in table:
    #     print(i)
    neiList = {}
    for i in table:
        neiList[i[0]] = []
    for i in table:
        neiList[i[0]].append(i[1])
    
    print(neiList)
    
    

    def recur(curr_node, had_small_cave = [], been_twice = False):
        had_small_cave.append(curr_node)
        if curr_node == "end":
            print("Path", had_small_cave)
            return 1
        counter = 0
        for dir in neiList[curr_node]:
            if dir == "start":
                continue
            check_twice = False
            if dir.lower() == dir and dir in had_small_cave:
                if been_twice:
                    continue
                else:
                    check_twice = True
            if not check_twice and been_twice:
                check_twice = True
            counter += recur(dir, copy.deepcopy(had_small_cave), check_twice)
        return counter
    print(recur("start"))


    

                    
        

    

if __name__ == "__main__":
    main()
    pass