
def getData():
    authorList = []
    booksList = []

    authorNum = input("How many authors? ")

    for i in range(authorNum):
        author = input("Enter author: ")
        booksSold = int(input("Enter number of books sold: "))
        authorList.append(author)
        booksList.append(booksSold)
    return authorList, booksList


def getHighest(booksList):
    max = 0

    salesList = []
    for i in range(len(salesList)):
        if salesList[i] > max:
            max = salesList[i]
    return max

def getAverage(booksList):
    average = 0

    salesList = []

    for i in range(len(salesList)):
        average += salesList[i]
    average = average / len(salesList)

def main():
    authorList, bookList = getData()
    salesList = getHighest(bookList)
    average = getAverage(bookList)
    print("Best selling author is ", bookList)