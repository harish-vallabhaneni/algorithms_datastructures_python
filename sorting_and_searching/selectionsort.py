def selectionsort(itemlist):
	for num in range(len(itemlist)-1,0,-1):
		maxvaluepos = 0
		for i in range(1, num+1):
			if itemlist[maxvaluepos] < itemlist[i]:
				maxvaluepos = i
		temp = itemlist[num]
		itemlist[num] = itemlist[maxvaluepos]
		itemlist[maxvaluepos] = temp
	return itemlist

if __name__ == '__main__':
	print(selectionsort([1,4,6,3,2,5,9,8,7]))
