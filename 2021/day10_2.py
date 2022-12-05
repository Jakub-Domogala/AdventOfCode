from math import inf

op = ['(', '[', '{', '<']
cl = [')', ']', '}', '>']
points = [1, 2, 3, 4]

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
                return 0
            else:
                stack.pop()
    print(stack)
    score = 0
    for i in range(len(stack)-1, -1, -1):
        score *= 5
        score += points[op.index(stack[i])]
    return score
    


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
    score = []
    for line in table:
        a = find_corruption(line)
        if a > 0:
            score.append(a)
    score.sort()
    print(len(score))
    print(score[len(score)//2])
        
    print(score)




if __name__ == "__main__":
    main()
    pass
