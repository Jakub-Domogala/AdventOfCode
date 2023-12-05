import re

sum = 0
digit_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
with open("input01.txt") as file:
    for line in file:        
        first = [int(digit_mapping.get(digit.lower(), digit)) if digit in digit_mapping else int(digit) for digit in 
                 re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, re.IGNORECASE)][0]
        last = [int(digit_mapping.get(digit.lower(), digit)) if digit in digit_mapping else int(digit) for digit in 
                re.findall(r'.*(\d|one|two|three|four|five|six|seven|eight|nine).*$', line, re.IGNORECASE)][-1]
        sum += 10*first + last

print(sum)