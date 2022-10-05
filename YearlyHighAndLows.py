# Highest and Lowest Prices Per Year: For each year in the file, 
# determine the date and amount for the lowest price, and the highest price.
file = open('GasPrices.txt', 'r')   
contents = file.readlines()       
file.close()              

for years in range(1993, 2014, 1):
  priceList = []
  for i in range(len(contents)):
    if str(contents[i][6:10]) == str(years):
        priceList.append(float(contents[i][11:])) 

  print('\n'+ str(years) +'\tThe lowest price was: $' + format(float(min(priceList)), ',.3f') + '.')
  print('\tThe highest price was: $' + format(float(max(priceList)), ',.3f') + '.')
  print()