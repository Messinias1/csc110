#
# myFile = open('three_movies.txt', 'r')
# myFile
#
# x = myFile.readline()
# print(x)
#
# y = myFile.readline()
# print(y)
#
# myFile.close()
# myFile

# myFile.readline()

def getSpeeds():
    speedList = []
    inFile = open('speeds.txt', 'r')
    line = inFile.readline()
    line = line.strip()

    while line != '':
        speed = float(line)
        speedList.append(speed)
        line = inFile.readline()
        line = line.strip()

    inFile.close()

    return speedList


def getSpeeds2():
    speedList = []
    inFile = open('speeds.txt', 'r')
    for line in inFile:
        line = line.strip()
        speed = float(line)
        speedList.append(speed)
    inFile.close()

    return speedList


def main():
    print(getSpeeds())
    print(getSpeeds2())


main()
