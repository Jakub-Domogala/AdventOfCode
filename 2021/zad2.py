#zad2
a = [1,0,3,4]

def multiplyList(tab):
    sum = 1
    for i in tab:
        sum *= i
        if i == 0:
            print("Mnożenie przez 0")
            return 0
    return sum


print(multiplyList(a))