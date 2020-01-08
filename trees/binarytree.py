class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftchild = None
		self.rightchild = None

	def insertleft(self, newNode):
		if self.leftchild == None:
			self.leftchild = BinaryTree(newNode)
		else:
			newTree = BinaryTree(newNode)
			newTree.leftchild = self.leftchild
			self.leftchild = newTree

	def insertright(self, newNode):
		if self.rightchild == None:
			self.rightchild = BinaryTree(newNode)
		else:
			newTree = BinaryTree(newNode)
			newTree.leftchild = self.rightchild
			self.rightchild = newTree

	def getrightchild(self):
		return self.rightchild

	def getleftchild(self):
		return self.leftchild

	def getrootvalue(self):
		return self.key

	def setrootvalue(self, key):
		self.key = key

	def isleaf(self):
		return self.leftchild == None and self.rightchild == None

	def inorder(self):
		if self.leftchild:
			self.leftchild.inorder()
		print(self.key)
		if self.rightchild:
			self.rightchild.inorder()

	def preorder(self):
		print(self.key)
		if self.leftchild:
			self.leftchild.preorder()
		if self.rightchild:
			self.rightchild.preorder()

	def postorder(self):
		if self.leftchild:
			self.leftchild.postorder()
		if self.rightchild:
			self.rightchild.postorder()
		print(self.key)

def height(tree):
	if tree == None:
		return -1
	else:
		return 1 + max(height(tree.leftchild), height(tree.rightchild))

if __name__ == '__main__':
	bt = BinaryTree('T')
	bt.insertleft('l')
	bt.insertright('r')
	print(bt.getrootvalue())
	print(bt.getleftchild())
	print(bt.getrightchild())
	print(bt.getleftchild().getrootvalue())
	print(bt.getrightchild().getrootvalue())
	print('*** In-order traversal ***')
	bt.inorder()
	print('*** pre-order traversal ***')
	bt.preorder()
	print('*** pos-order traversal ***')
	bt.postorder()
	print('Height: '+str(height(bt)))
