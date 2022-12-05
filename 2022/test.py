import re
a = "29-47,22-32"
b = re.findall(r'\d+', a)
print(b)
