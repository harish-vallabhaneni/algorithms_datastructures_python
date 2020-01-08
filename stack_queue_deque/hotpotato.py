from ds import Queue

def hotpotato(namelist, number):
	namequeue = Queue()
	
	for name in namelist:
		namequeue.enqueue(name)

	while int(namequeue.size()) > 1:
		for i in range(number):
			namequeue.enqueue(namequeue.dequeue())
		namequeue.dequeue()
	return namequeue.dequeue()

if __name__ == '__main__':
	print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
