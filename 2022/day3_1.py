def prio(type):
    if 97 <= ord(type) <= 122:
        return ord(type) - 96
    return ord(type) - 38

def get_line_error_prio(line):
    for i in range(len(line)//2):
            for j in range(len(line)//2, len(line)):
                if line[i] == line[j]:
                    print(line[:len(line)//2], line[len(line)//2:], line[i])
                    return prio(line[i])

with open("input3.txt") as file:
    prio_sum = 0
    for line in file:
        line = line.replace("\n", "")
        prio_sum += get_line_error_prio(line)
    print(prio_sum)

# print(ord("z")-96)
# print(ord("Z")-38)
# print(ord("a"), ord("z"), "a-z")
# print(ord("A"), ord("Z"), "A-Z")
