
def sequentialsearch(itemlist, item):
	if len(itemlist) == 0:
		return False
	found = False
	index = 0
	while index<len(itemlist) and not found:
		if itemlist[index] == item:
			found = True
		index = index + 1
	return found

def orderedsequentialsearch(itemlist, item):
	if len(itemlist) == 0:
		return False
	found = False
	index = 0
	stop = False

	while index<len(itemlist) and not found and not stop:
		if itemlist[index] == item:
			found = True
		elif itemlist[index] > item:
			stop = True
		else:
			index += 1
	return found

if __name__ == '__main__':
	print(sequentialsearch([1,2,3,4,5],5))
	print(orderedsequentialsearch([1,2,3,4,5],5))
