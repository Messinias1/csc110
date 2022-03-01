
arr = []
reversedArr = []

size = int(input("Enter the size of the list: "))

num = int(input("Enter a number: "))
arr.append(num)

j = 1
while j < size:
    num = int(input("Enter a number: "))
    arr.append(num)

    j += 1

i = len(arr) - 1

while i >= 0:
    # print(arr[i])
    reversedArr.append(arr[i])
    i -= 1

print("The original list is: ")
print(arr)
print("The reversed list is: ")
print(reversedArr)