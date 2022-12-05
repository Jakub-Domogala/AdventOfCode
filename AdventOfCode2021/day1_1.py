with open('input_day1_1.txt') as fp:
    new = None
    old = None
    counter = 0
    for line in fp:
        if not old:
            old = new
            new = int(line)
        else:
            if old < new:
                counter += 1
            old = new
            new = int(line)
    if old < new:
        counter += 1
    print(counter)