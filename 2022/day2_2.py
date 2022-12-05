# A rock        1
# B paper       2
# C scissors    3

# X lose
# Y draw
# Z win

options = {
    "A X" : 3 + 0,
    "A Y" : 1 + 3,
    "A Z" : 2 + 6,
    "B X" : 1 + 0,
    "B Y" : 2 + 3,
    "B Z" : 3 + 6,
    "C X" : 2 + 0,
    "C Y" : 3 + 3,
    "C Z" : 1 + 6
}
score = 0
with open("input2.txt") as file:
    for line in file:
        line = line[:3]
        if line in options:
            print(line, options[line])
            score += options[line]
print(score)