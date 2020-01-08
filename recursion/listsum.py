
def listsum(listnum):
	if len(listnum) == 1:
		return listnum[0]
	else:
		return listnum[0] + listsum(listnum[1:])


if __name__ == '__main__':
	print(listsum([1,2,3,4,5,6,7,8,9]))

