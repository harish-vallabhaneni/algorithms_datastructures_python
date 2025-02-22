import unittest

# this heap takes key value pairs, we will assume that the keys are integers


class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		print(len(self.heapList), i)
		while (i > 0):
			print(self.heapList, i)
			self.percDown(i)
			i = i - 1
		print(self.heapList, i)

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def percUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
			   tmp = self.heapList[i // 2]
			   self.heapList[i // 2] = self.heapList[i]
			   self.heapList[i] = tmp
			i = i // 2

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def isEmpty(self):
		if currentSize == 0:
			return True
		else:
			return False

	def __str__(self):
		return str(self.heapList)

class FooThing:
	def __init__(self, x, y):
		self.key = x
		self.val = y

	def __lt__(self, other):
		if self.key < other.key:
			return True
		else:
			return False

	def __gt__(self, other):
		if self.key > other.key:
			return True
		else:
			return False

	def __hash__(self):
		return self.key


if __name__ == '__main__':
    heap = BinHeap()
    heap.insert(1)
    heap.insert(5)
    heap.insert(3)
    heap.insert(9)
    heap.insert(7)
    heap.insert(2)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)
    print(heap.currentSize)
    print(heap)
    print(heap.delMin())
    print(heap.currentSize)
    print(heap)
    newheap = BinHeap()
    newheap.buildHeap([1,5,3,9,7,2,4,6,8])
    print(newheap)
    print(newheap.currentSize)
