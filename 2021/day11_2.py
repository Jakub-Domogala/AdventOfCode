def main():
    input = "input_day11_1.txt"
    table = []
    # Read file
    print(input)
    with open(input) as fp:
        while True:
            tmp = fp.readline()
            if len(tmp) < 2:
                break
            tab = [int(tmp[i]) for i in range(len(tmp) - 1 )]
            table.append(tab)
        pass
    # for i in table:
    #     print(i)
    
    flashed = [[False for _ in range(len(table))] for _ in range(len(table))]

    options = [
        (-1,    -1), 
        (-1,     0),
        (-1,     1),
        ( 0,     1),
        ( 1,     1),
        ( 1,     0),
        ( 1,    -1),
        ( 0,    -1)
    ]

    counter = 0
    for step in range(1000):
        print("NEW STEP")
        # Increase all by 1
        for i in range(10):
            for j in range(10):
                table[i][j] += 1
        # for row in table:
        #     print(row)
        # print()
        # Flash octopus with energy above 9
        any_flash = True
        counter = 0
        while any_flash:
            any_flash = False
            for i in range(10):
                for j in range(10):
                    if table[i][j] > 9 and not flashed[i][j]:
                        any_flash = True
                        flashed[i][j] = True
                        counter += 1
                        for opt in options:
                            x = i + opt[0]
                            y = j + opt[1]
                            if x in range(10) and y in range(10):
                                table[x][y] += 1
        for i in range(10):
            for j in range(10):
                if flashed[i][j]:
                    table[i][j] = 0
                    flashed[i][j] = False
        if counter == 100:
            print(step)
            for row in table:
                print(row)
            return step
        
        # for row in table:
        #     print(row)
        # print()
    print(counter)
                            
                    
        

    




if __name__ == "__main__":
    main()
    pass