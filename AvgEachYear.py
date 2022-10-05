# Get average gas price for each year (1993 and 2013).
# Char spots 6 through 9 for YYYY.
file = open('GasPrices.txt', 'r')   
contents = file.readlines()       
file.close()                        

priceList = [0]
avgPrice = float(0)
for n in range(1993, 2014, 1):
    for i in range(len(contents)):
        if contents[i][6:10] == str(n):
            priceList.append(float(contents[i][11:]))
    for i in range(len(priceList)):
        avgPrice += priceList[i]
    avgPrice = avgPrice / len(priceList)
    print('The average price of \'' +  str(n) + ' is $' + format(avgPrice, ',.3f'))
