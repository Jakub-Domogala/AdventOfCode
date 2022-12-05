from rpy2 import robjects as ro





def confInterNorm(m_x, sigma, n, p): # przedział ufności dla mi gdy znamy sigme
    res = ro.r(f'''
        alpha <- 1 - {p}
        z <- {sigma}/sqrt({n})
        res <- c(qnorm(alpha/2)*z+{m_x}, qnorm(1-alpha/2)*z+{m_x})
        print(qnorm(alpha/2))
        print(qnorm(1-alpha/2))
        return(res)
    ''')
    return res

def confInterT(m_x, S, n, p): #przedzial ufności dla mi gdy nie znamy sigmy
    res = ro.r(f'''
        alpha <- 1 - {p}
        z <- {S}/sqrt({n})
        res <- c(qt(1-alpha/2, {n}-1)*z+{m_x}, qt(alpha/2, {n}-1)*z+{m_x})
        print(qt(1-alpha/2, {n}-1))
        print(qt(alpha/2, {n}-1))
        return(res)
    ''')
    return res

def confInterChiSqrVar(S, n, p): # przedział ufności dla var = sigma^2
    res = ro.r(f'''
        alpha <- 1 - {p}
        z <- {S}^2*{n-1}
        res <- c(z/qchisq(1-alpha/2, {n}-1), z/qchisq(alpha/2, {n}-1))
        print(qchisq(1-alpha/2, {n}-1))
        print(qchisq(alpha/2, {n}-1))
        return(res)
    ''')
    return res

def confInterChiSqrSd(S, n, p):
    res = ro.r(f'''
           alpha <- 1 - {p}
           z <- {S}^2*{n-1}
           res <- c(z/qchisq(1-alpha/2, {n}-1), z/qchisq(alpha/2, {n}-1))
           print(qchisq(1-alpha/2, {n}-1))
           print(qchisq(alpha/2, {n}-1))
           return(sqrt(res))
       ''')
    return res

print(confInterNorm(50, 20, 100, 0.95))
print(confInterT(37.3, (13.5)**(1/2), 25, 0.96))
print(confInterChiSqrVar(2, 20, 0.9))




def main():
    pass
    # print("Wybierz co chcesz obliczyć")
    # print("Przedziały ufności T studenta: [T]")
    # print("Przedziały ufności hi^2: [X]")
    # print("Przedziały ufności rozkładu Normalnego: [N]")
    # c = input(">>>")
    # if c == "t" or c == "T":
    #     print("Wpisz [m_x, S, n, p]")
    #     m_x = input("m_x")
    #     S = input("S^2")
    #     n = input("n")
    #     p = input("p")
    #
    # elif c == "n" or c == "N":
    #     print("Wpisz [m_x, sigma, n, p]")
    #     m_x = input("m_x")
    #     sigma = input("sigma")
    #     n = input("n")
    #     p = input("p")
    # elif c == "x" or c == "X":
    #     print("Wpisz [S, n, p]")
    #     S = (input("S^2"))**(1/2)
    # elif c == "xsqrt" or c == "XSQRT":
    #     print("Wpisz [S, n, p]")
if __name__ == "__main__":
    main()


