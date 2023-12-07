import re

tab = []
with open("input03.txt") as file:
    for line in file:
        tab.append(line.replace("\n", ""))


def check_and_sum_tab(tab):
    options = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    result = 0

    is_num = False
    is_good = False

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
        return re.match("[0-9]", tab[i][j])

    curr_num_string = ""
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if not match_num(i, j) or j == 0:
                # if is_num:
                #     print(result, curr_num_string, is_num, is_good)
                if is_num and is_good:
                    result += int(curr_num_string)
                is_num = False
                is_good = False
                curr_num_string = ""
            if match_num(i, j):
                curr_num_string += tab[i][j]
                if find_sign_around(i, j):
                    is_good = True
                is_num = True

            # print(result, curr_num_string, is_num, is_good)
    return result


r = check_and_sum_tab(tab)
print(r)
