import re
from collections import defaultdict

tab = []
with open("input03.txt") as file:
    for line in file:
        tab.append(list(line.replace("\n", "")))
numbers = [[tab[i][j] for j in range(len(tab[0]))] for i in range(len(tab))]


def mark_part_numbers(tab):
    options = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    result = defaultdict(bool)
    is_num = False

    def match_sign(i, j):
        return re.match("^[^0-9.]", tab[i][j])

    def find_sign_around(i, j):
        for oi, oj in options:
            ni, nj = i + oi, j + oj
            if 0 <= ni < len(tab) and 0 <= nj < len(tab[0]):
                if match_sign(ni, nj):
                    return True
        return False

    def match_num(i, j):
        return re.match("[0-9]+", tab[i][j])

    indexing = 1
    curr_num_string = ""
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if not match_num(i, j) or j == 0:
                if is_num:
                    indexing += 1
                is_num = False
            if match_num(i, j):
                if find_sign_around(i, j):
                    result[str(indexing)] = result[str(indexing)] or True
                is_num = True

                tab[i][j] = str(indexing)
            # else:
            #     tab[i][j] = ""

    return result


def get_gears_ratios(numbers, ids, marks):
    gear = "*"
    result = 0

    options = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    def match_num(i, j):
        return re.match("[0-9]+", numbers[i][j])

    def get_gear_ratio(i, j):
        count_adj = 0
        found = {"siema"}
        tmp_nums = []
        result = 1
        for oi, oj in options:
            ni, nj = i + oi, j + oj
            if 0 <= ni < len(tab) and 0 <= nj < len(tab[0]):
                if (
                    match_num(ni, nj)
                    and marks[ids[ni][nj]]
                    and ids[ni][nj] not in found
                ):
                    found.add(ids[ni][nj])
                    tmp_nums.append(expand_get_number(ni, nj))
                    count_adj += 1
                    result *= expand_get_number(ni, nj)
        if count_adj == 2:
            print(tmp_nums)
            return result
        return 0

    def expand_get_number(i, j):
        result = numbers[i][j]
        for jexp in range(j - 1, -1, -1):
            if match_num(i, jexp):
                result = numbers[i][jexp] + result
            else:
                break
        for jexp in range(j + 1, len(numbers)):
            if match_num(i, jexp):
                result = result + numbers[i][jexp]
            else:
                break
        return int(result)

    for i in range(len(ids)):
        for j in range(len(ids[0])):
            if numbers[i][j] == gear:
                result += get_gear_ratio(i, j)
    return result


r = mark_part_numbers(tab)
# print(r)
for row in tab:
    for i in range(len(row)):
        if re.match("[0-9]+", row[i]):
            if r[row[i]]:
                print("X", end=" ")
            else:
                print("-", end=" ")
        else:
            print(row[i], end=" ")
    print()
print(get_gears_ratios(numbers, tab, r))
