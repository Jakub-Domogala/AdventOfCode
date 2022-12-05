def prio(type):
    if 97 <= ord(type) <= 122:
        return ord(type) - 96
    return ord(type) - 38

def find_common_in_2(a, b):
    common = []
    for i in a:
        for j in b:
            if i == j and not i in common:
                common.append(i)
    return common

def find_common_in_3(group):
    a, b, c = group
    common = find_common_in_2(a, b)
    common = find_common_in_2(common, c)
    return common[0]

with open("input3.txt") as file:
    prio_sum = 0
    counter = 0
    group = [None] * 3
    for line in file:
        line = line.replace("\n", "")
        group[counter%3] = line
        if counter%3 == 2:
            prio_sum += prio(find_common_in_3(group))
        counter += 1
    print(prio_sum)

# print(ord("z")-96)
# print(ord("Z")-38)
# print(ord("a"), ord("z"), "a-z")
# print(ord("A"), ord("Z"), "A-Z")
