def mergesort(itemlist):
	if len(itemlist) > 1:
		midpoint = len(itemlist)//2
		leftlist = itemlist[0:midpoint]
		rightlist = itemlist[midpoint:len(itemlist)]

		mergesort(leftlist)
		mergesort(rightlist)

		i=0
		j=0
		k=0
		while i<len(leftlist) and j<len(rightlist):
			if leftlist[i]<=rightlist[j]:
				itemlist[k]=leftlist[i]
				i=i+1
			else:
				itemlist[k]=rightlist[j]
				j=j+1
			k=k+1
		while i<len(leftlist):
			itemlist[k]=leftlist[i]
			i=i+1
			k=k+1
		while j<len(rightlist):
			itemlist[k]=rightlist[j]
			j=j+1
			k=k+1
	return itemlist

if __name__ == '__main__':
	print(mergesort([1,9,4,7,2,8,3,5,6]))
