from numpy import append, sort
# Get average gas price for each month.
file = open('GasPrices.txt', 'r')   
contents = file.readlines()       
file.close()         

priceList = []
averagePrice = float(0)
for n in range(1, 13, 1):
    for i in range(len(contents)):
      if(int(n) < 10):
        lower10 = '0' + str(n)
        if contents[i][:2] == str(lower10):
          priceList.append(float(contents[i][11:]))
      else:
        if contents[i][:2] == str(n):
          priceList.append(float(contents[i][11:]))
    for i in range(len(priceList)):
        averagePrice += priceList[i]
    averagePrice = averagePrice / len(priceList)
    print('The average price of month ' +  str(n) + ' is $' + format(averagePrice, ',.3f'))
