def binarysearch(itemlist, item):
	if len(itemlist) == 0:
		return False
	found = False
	index = 0
	last = len(itemlist)-1
	while index<=last and not found:
		midpoint = int((index+last)/2)
		if itemlist[midpoint] == item:
			found = True
		elif itemlist[midpoint] > item:
			last = itemlist[midpoint-1]
		else:
			index = itemlist[midpoint+1]

	return found

def binarysearchwithrecursion(itemlist, item):
	if len(itemlist) == 0:
		return False
	else:
		midpoint = len(itemlist)//2
		if itemlist[midpoint] == item:
			return True
		elif itemlist[midpoint] > item:
			return binarysearchwithrecursion(itemlist[:midpoint], item)
		else:
			return binarysearchwithrecursion(itemlist[midpoint+1:], item)

if __name__ == '__main__':
	print(binarysearch([1,2,3,4,5,6,7,8], 7))
	print(binarysearch([1,2,3,4,5,6,7,8,9], 7))
	print(binarysearchwithrecursion([1,2,3,4,5,6,7,8], 7))
	print(binarysearchwithrecursion([1,2,3,4,5,6,7,8,9], 7))
