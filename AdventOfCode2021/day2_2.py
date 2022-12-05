with open('input_day2_1.txt') as fp:
    x = 0
    y = 0
    aim = 0
    for line in fp:
        a, b = line.split()
        if a == "forward":
            x += int(b)
            y += int(b) * aim
        if a == "up":
            aim -= int(b)
        if a == "down":
            aim += int(b)
    print(x, y)
    print(x*y)