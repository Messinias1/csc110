
def main():
    print(sumOfMultiples(1000,3,5))

def sumOfMultiples(a,b,n):
    numList = []

    for i in range(a):
        if(i % b == 0 or i % n == 0):
            numList.append(i)

    total = sum(numList)
    return total

main()