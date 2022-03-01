def main():
    print(comb(5,2))


def fact(n):
    i = n
    f = 1
    while i > 0:
        f = f * i
        i = i - 1
    return f


def comb(n, r):
    n1 = fact(n)
    r1 = fact(r)
    nr1 = fact(n-r)
    choose = n1/(nr1 * r1)
    # print(nAndr, "N - R")
    if n < r:
        return (0)
    else:
        return(choose)

main()