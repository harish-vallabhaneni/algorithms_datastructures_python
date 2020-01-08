form node import Node
class orderedList:
	def __init__(self):
		self.head = None

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while not current == None and not found and not stop:
			if current.getData() == item:
				found = True
			elif current.getData() > item:
				stop = True
			else:
				current = current.getNext()
		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		node = Node(item)
		while not current == None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			node.setNext(self.head)
			self.head = node
		else:
			node.setNext(current)
			previous.setNext(node)

#other methods like search,isEmpty,size are same for both ordered and unordered lists
