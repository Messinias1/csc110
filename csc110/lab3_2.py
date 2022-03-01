
stocks = ['IBM', 'AAPL', 'GOOG', 'FB', 'SMSN', 'INTC', 'MCD', 'TWTR']
stockPrices = [23.4, 24.5, 25.3, 56.7, 89.4, 45.3, 43.6, 67.4]
counter = 0
yes = True

stockName = input("Enter the name of the stock: ")
perIncrease = float(input("Enter the percentage increase: "))


i = 0
while i < len(stocks) and yes == True:
    if (stockName == stocks[i]):
        # print(stockName)
        yes = False

    counter += 1
    i += 1

stockPrices[counter - 1] = round(stockPrices[counter - 1] * ((perIncrease /100)+1), 3)

# print(stockPrices[counter - 1])
# print(counter)
if yes == False:
    print("Updated Price List: ")
    print(stockPrices)
else:
    print("Stock not found")


