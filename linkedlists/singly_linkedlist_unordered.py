from node import Node

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, nodedata):
		node = Node(nodedata)
		node.setNext(self.head)
		self.head = node

	def search(self, nodedata):
		current = self.head
		found = False
		index = 0
		while not current == None and not found:
			if current.data == nodedata:
				found = True
				break
			else:
				current = current.getNext()
				index = index + 1
		
		if found:
			return 'item found at index: {}'.format(str(index))
		elif current == None:
			return 'no items in the linkedlist'
		else:
			return 'item not found in the linkedlist'

	def size(self):
		current = self.head
		index = 0
		while not current == None:
			current = current.getNext()
			index += 1
		return index

	def remove(self, nodedata):
		current = self.head
		previous = None
		found = False
		index = 0
		while not current == None and not found:
			if current.data == nodedata:
				found = True
				break
			else:
				previous = current
				current = current.getNext()
				index = index + 1

		if previous == None:
			self.head = current.getNext()
			return 'item at index {} removed from the linkedlist'.format(str(index))
		elif found:
			current = current.getNext()
			previous.setNext(current)
			return 'item at index {} removed from the linkedlist'.format(str(index))
		elif current == None:
			return 'item not found. The linkedlist is empty'
		else:
			return 'provided item not found in the linkedlist'

	def append(self,item):
		current = self.head
		index = 0
		if current:
			while current.getNext() != None:
				current = current.getNext()
				index = index + 1
			current.setNext(Node(item))
			index = index + 1
			return 'item {} added at pos {}'.format(item, index)
		else:
			self.head = Node(item)
			return 'item {} added at pos {}'.format(item, index)

	def index(self, item):
		return self.search(item)
 
	def insert(self, pos, item):
		current = self.head
		index = 0
		node = Node(item)
		previous = None
		if current:
			while index <= pos:
				if index == pos:
					if not previous == None:
						previous.setNext(node)
						node.setNext(current)
					else:
						node.setNext(current)
						self.head = node
					break
				previous = current
				current = current.getNext()	
				index += 1
			return 'item {} inserted at index {}'.format(item, index)
		else:
			self.head = node
			return 'The linkedlist is empty. Inserting the item as the first item instead of inserting at {}'.format(str(pos))
				
	def pop(self, pos=None):
		current = self.head
		previous = None
		index = 0
		popped_item = None
		if not pos == None:
			pos = pos
		else:
			pos = self.size() - 1
		if current:
			if pos and pos > 0:
				while index <= pos:
					if index == pos:
						popped_item = current.data
						current = current.getNext()
						previous.setNext(current)
						break
					previous = current
					current = current.getNext()
					index += 1
			else:
				self.head = current.getNext()
			return 'item {} popped at position {}'.format(popped_item, index)
		else:
			return 'No items to pop. The linkedlist is empty'

if __name__ == '__main__':
	l = UnorderedList()
	print('adding items 1,2,3')
	l.add(1)
	l.add(2)
	l.add(3)
	print('size: '+str(l.size()))
	print('searching item 1: '+l.search(1))
	print('searching item 2: '+l.search(2))
	print('searching item 3: '+l.search(3))
	print('removing item 3: '+l.remove(3))
	print('size: '+str(l.size()))
	print('searching item 1: '+l.search(1))
	print('searching item 2: '+l.search(2))
	print('appending item 3: '+l.append(3))
	print('size: '+str(l.size()))
	print('searching item 3: '+l.search(3))
	print('index of item 1: '+l.index(1))
	print('index of item 3: '+l.index(3))
	print('inserting item 4 at pos 3: '+l.insert(3, 4))
	print('size: '+str(l.size()))
	print('searching item 4: '+l.search(4))
	print('popping item at pos 3: '+l.pop(3))
	print('size: '+str(l.size()))
	print('popping the last node: '+l.pop())
	print('size: '+str(l.size()))
