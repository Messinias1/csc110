
# purchasedItem = input("Enter name of purchased item: ")
# price = int(input("Enter price of item: "))
# taxRate = float(input("Enter tax rate: "))
#
# salesTax = price * taxRate
# print("The sales tax on the ", purchasedItem, " with tax rate of ", taxRate, " is: ", salesTax)

i = 0
sum = 0
while i < 10:
    num = int(input("Enter the grade for your exam: "))
    sum = sum + num
average = sum/10
print(average)