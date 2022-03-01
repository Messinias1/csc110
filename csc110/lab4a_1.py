
def main():
    print(fact(4))


def fact(n):
    i = n
    f = 1
    while i > 0:
        f = f * i
        i = i - 1
    return f

main()