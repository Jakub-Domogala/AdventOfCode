

from math import inf
from pprint import pprint


# def recur(open, close, line, ind, type):
#     if ind == len(line):
#         return None, None
#     ntype = None
#     for i in range(4):
#         if line[ind] == open[i]:
#             ntype = i
#             break
#     if ntype != None:
#         return recur(open, close, ind + 1, ntype)

#     for i in range(4):
#         if line[ind] == close[i]:
#             ntype = i
#             break
#     if ntype == type:
#         return True, ind
#     else:
#         return False, ntype
#     return True, True


# def findMistake(line):
#     open = ['(', '[', '{', '<']
#     close = [')', ']', '}', '>']
#     type = None
#     for i in range(4):
#         if line[0] == open[i]:
#             type = i
#             break
#     is_fine = None
#     while is_fine == None:
#         is_fine, itype = recur(open, close, line, 1, type)
#         if is_fine == False:
#             return itype
#         if is_fine == True:
#             if itype == True:
#                 return True
#             else:
#                 type = None

op = ['(', '[', '{', '<']
cl = [')', ']', '}', '>']
points = [3, 57, 1197, 25137]

def find_corruption(t):
    ind = 0
    stack = []
    for i in range(len(t)):
        # print(stack)
        if t[i] in op:
            stack.append(t[i])
        elif t[i] in cl:
            # print(cl.index(t[i]), )
            if cl.index(t[i]) != op.index(stack[-1]):
                return points[cl.index(t[i])]
            else:
                stack.pop()
    return 0
    


def main():
    input = "input_day10_1.txt"
    table = []
    # Read file
    print(input)
    with open(input) as fp:
        while True:
            tmp = fp.readline()
            if len(tmp) < 2:
                break
            tab = [tmp[i] for i in range(len(tmp) - 1 )]
            table.append(tab)
        pass
    # for i in list:
    #     print(i)
    score = 0
    for line in table:
        score += find_corruption(line)
        # break
    print(score)




if __name__ == "__main__":
    main()
    pass
