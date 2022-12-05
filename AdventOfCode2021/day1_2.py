with open('input_day1_1.txt') as fp:
    a1 = int(fp.readline())
    a2 = None
    a3 = None
    a4 = None
    counter = 0
    while a1:
        a4 = a3
        a3 = a2
        a2 = a1
        a1 = fp.readline()
        if a1:
            a1 = int(a1)
        else: break

        if a4 and a4 < a1:
            counter += 1
    print(counter)
