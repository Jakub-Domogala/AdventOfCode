import re

sum = 0
with open("input1.txt") as file:
    for line in file:
        digits = ''.join(re.findall(r'\d', line))
        sum += 10*int(digits[0]) + int(digits[-1])

print(sum)