
def main():
    print(fib(10))

def fib(num):
    a = 1
    b = 1
    sum = 1

    while(b <= num):
        if(b % 2 == 0):
            sum += b

        c = b
        b = a + b
        a = b

    return sum

main()