def bubblesort(itemlist):
	for num in range(len(itemlist)-1, 0, -1):
		for i in range(num):
			if itemlist[i] > itemlist[i+1]:
				temp = itemlist[i]
				itemlist[i] = itemlist[i+1]
				itemlist[i+1] = temp

	return itemlist

if __name__ == '__main__':
	print(bubblesort([1,5,6,7,8,3,2,4,9]))
