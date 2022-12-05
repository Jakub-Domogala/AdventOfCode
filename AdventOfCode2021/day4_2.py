from pprint import pprint
from math import inf

def isWinner(marks):
    for i in range(5):
        check = True
        for j in range(5):
            if not marks[j][i]:
                check = False
                break
        if check:
            return True

    for i in range(5):
        check = True
        for j in range(5):
            if not marks[i][j]:
                check = False
                break
        if check:
            return True

    return False

def markBoard(board, marks, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                marks[i][j] = True
                return True # zmienic jesli nie dziala

def addUnmarked(board, marks):
    result = 0
    for i in range(5):
        for j in range(5):
            if not marks[i][j]:
                result += board[i][j]
    return result


def main():
    wInd = None
    lowest = inf
    input = "input_day4_1.txt"
    Numbers = []
    Boards = []
    with open(input) as fp:
        line = fp.readline()
        check = False
        currNum = 0
        for i in range(len(line)):
            if ord(line[i]) >= 48 and ord(line[i]) <= 57:
                currNum *= 10
                currNum += int(line[i])
                check = True
            else:
                if check:
                    Numbers.append(currNum)
                    currNum = 0
                    check = False

        line = fp.readline() # empty line before boards list

        check = True

        while check:
            sBoard = []
            for i in range(5):
                bline = [] * 5
                line = fp.readline()
                if not line:
                    check = False
                    break
                bline = line.split()
                #print(bline)
                for ind in range(5):
                    bline[ind] = int(bline[ind])
                #print(bline, "LIne")
                sBoard.append(bline)
                #print(sBoard, "Board")
            xd = fp.readline()
            if not check: break
            Boards.append(sBoard) #List of Boards finished

    # Boards[i][y][x] board number 'i' row number 'y' and column 'x'

    n = len(Boards)
    Marks = [ [[False] * 5 for _ in range(5)] for i in range(n)]
    won = [False] * n

    for nInd in range(len(Numbers)):

        for bInd in range(n):

            markBoard(Boards[bInd], Marks[bInd], Numbers[nInd])

            win = isWinner(Marks[bInd])
            if win:
                won[bInd] = True
                countWinners = 0
                for i in range(n):
                    if won[i]:
                        countWinners += 1

                if countWinners == 99:
                    for i in range(100):
                        if not won[i]:
                            wInd = i
                            break
                if countWinners == 100:
                    sum = addUnmarked(Boards[wInd], Marks[wInd])
                    res = sum * Numbers[nInd]
                    print(res)
                    return 0


if __name__ == "__main__":
    main()






