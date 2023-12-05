from functools import reduce

max_red = 12
max_green = 13
max_blue = 14
limits = {
    "red": max_red,
    "green": max_green,
    "blue": max_blue
}
sum = 0
with open("input02.txt") as file:
    for line in file:
        game, rounds = line.split(sep=":")
        rounds = rounds.split(sep=";")
        is_correct = True
        limits = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for r in rounds:
            for amount, color in [one_col.strip().split(sep=" ") for one_col in r.split(sep=",")]:
                limits[color] = max(limits[color], int(amount))
        sum += reduce(lambda x, y: x * y, [int(val) for key, val in limits.items()])
        
print(sum)

