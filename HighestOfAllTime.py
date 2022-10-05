# List of Prices, Highest to lowest: Generate a text file that
# lists the dates and prices, sorted from the highest price to the
# lowest.
file = open('GasPrices.txt', 'r')   
contents = file.readlines()       
file.close()


priceList = []
sortedHighToLow = []
highestToLowest = open('q5write.txt', 'w')

for i in range(len(contents)):
  new = contents[i].split(':')
  priceList.append(new)
for i in range(len(priceList)):
  sortedHighToLow.append(priceList[i][1] + ' was the price from: ' + priceList[i][0])

sortedHighToLow = sorted(sortedHighToLow, reverse = True)

for i in range(len(sortedHighToLow)):
  highestToLowest.write(str(sortedHighToLow[i]) + '\n')

highestToLowest.close()
