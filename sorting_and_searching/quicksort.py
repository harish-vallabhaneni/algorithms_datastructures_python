import time

def quicksort(itemlist):
	return quicksorthelper(itemlist, 0, len(itemlist)-1)

def quicksorthelper(itemlist, first, last):
	if first<last:
		splitpoint = partition(itemlist, first, last)
		quicksorthelper(itemlist, first, splitpoint-1)
		quicksorthelper(itemlist, splitpoint+1, last)
	return itemlist

def partition(itemlist, first, last):
	pivotindex = median_of_three(itemlist, first, last)
	pivotvalue = itemlist[pivotindex]
	leftmark = first
	rightmark = last
	done = False
	while not done:
		while leftmark<=rightmark and itemlist[leftmark]<pivotvalue:
			leftmark += 1
		while rightmark>=leftmark and itemlist[rightmark]>pivotvalue:
			rightmark -= 1
		if rightmark<=leftmark:
			done=True
		else:
			temp = itemlist[leftmark]
			itemlist[leftmark]=itemlist[rightmark]
			itemlist[rightmark]=temp

	return rightmark

def median_of_three(itemlist, first, last):
	midpoint = (first+last)//2
	if itemlist[first] < itemlist[midpoint]:
		return first if itemlist[last] < itemlist[first] else last if itemlist[last] < itemlist[midpoint] else midpoint
	else:
		return midpoint if itemlist[last] < itemlist[midpoint] else first if itemlist[last] > itemlist[first] else last

if __name__=='__main__':
	print(quicksort([1,9,7,6,5,2,3,4,8]))
