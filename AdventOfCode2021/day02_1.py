with open('input_day2_1.txt') as fp:
    x = 0
    y = 0
    for line in fp:
        a, b = line.split()
        if a == "forward":
            x += int(b)
        if a == "up":
            y -= int(b)
        if a == "down":
            y += int(b)
    print(x, y)
    print(x*y)
