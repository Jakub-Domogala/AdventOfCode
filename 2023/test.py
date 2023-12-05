import re

input_string = "abac"

# Extract numeric digits and digits written as words
digits = re.findall(r'.*(ab|ba).*$', input_string, re.IGNORECASE)
print(digits)
