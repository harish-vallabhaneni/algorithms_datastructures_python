def insertionsort(itemlist):
	for i in range(1, len(itemlist)):
		currentvalue = itemlist[i]
		position = i
		while position > 0 and itemlist[position-1] > currentvalue:
			itemlist[position] = itemlist[position-1]
			position = position - 1
		itemlist[position] = currentvalue
	return itemlist

if __name__ == '__main__':
	print(insertionsort([1,5,3,7,6,9,8,2,4]))
