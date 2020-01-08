import heapq

def heapsort(itemlist):
	heapq.heapify(itemlist)
	sorted_heap = []
	for _ in range(len(itemlist)):
		sorted_heap.append(heapq.heappop(itemlist))
	return sorted_heap

if __name__ == '__main__':
	print(heapsort([9,1,8,2,7,3,6,4,5]))
