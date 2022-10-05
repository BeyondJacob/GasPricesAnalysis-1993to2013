# List of Prices, Lowest to Highest: Generate a text file that
# lists the dates and prices, sorted from the lowest price to the
# highest.
file = open('GasPrices.txt', 'r')   
contents = file.readlines()       
file.close()


priceList = []
sortedLowToHigh = []
lowestToHighest = open('q4write.txt', 'w')

for i in range(len(contents)):
  new = contents[i].split(':')
  priceList.append(new)
for i in range(len(priceList)):
  sortedLowToHigh.append(priceList[i][1] + ' was the price from: ' + priceList[i][0])

sortedLowToHigh = sorted(sortedLowToHigh)

for i in range(len(sortedLowToHigh)):
  lowestToHighest.write(str(sortedLowToHigh[i]) + '\n')

lowestToHighest.close()