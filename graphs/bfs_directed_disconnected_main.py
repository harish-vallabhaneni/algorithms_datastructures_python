#bfs for directed graph

from queue import Queue

class Vertex:
	def __init__(self, vtx):
		self.id = vtx
		self.connectedvertices = {}
		self.color = 'white'

	def addNeighbor(self, nbr, weight=0):
		self.connectedvertices[nbr] = weight

	def setcolor(self, color):
		self.color = color

	def getcolor(self):
		return self.color

	def getid(self):
		return self.id

	def getConnections(self):
		return self.connectedvertices.keys()

	def getWeight(self, vtx):
		return self.connectedvertices[vtx]

	def __str__(self):
		return str(self.id) + " - color:" + str(self.color) + ", connected vertices: " + str(self.connectedvertices)

class Graph:
	def __init__(self):
		self.vertices = {}
		self.verticessize = 0

	def addVertex(self, vtx):
		newvertex = Vertex(vtx)
		self.vertices[vtx] = newvertex
		self.verticessize += 1
		return newvertex

	def addEdge(self, frm, to, weight=0):
		if frm not in self.vertices:
			newfrmvertex = self.addVertex(frm)
		if to not in self.vertices:
			newtovertex = self.addVertex(to)
		self.vertices[frm].addNeighbor(self.vertices[to], weight)

	def getVertices(self):
		return list(self.vertices.keys())

	def getVertex(self, vtx):
		if vtx in self.vertices:
			return self.vertices[vtx]
		else:
			return None

	def __contains__(self, vtx):
		return vtx in slef.vertices

	def __iter__(self):
		return iter(self.vertices.values())

	def bfs(self, source):
		queue = Queue()
		vertices = self.getVertices()
		for vertex in vertices:
			if self.getVertex(vertex).getcolor() == 'white':
				queue.put(self.getVertex(vertex))
				while not queue.empty():
					vtx = queue.get()
					for nbr in vtx.getConnections():
						if nbr.getcolor() == 'white':
							nbr.setcolor('gray')
							queue.put(nbr)
					vtx.setcolor('black')
					print(vtx.getid(), vtx.getcolor())

h = Graph()
h.addEdge(0,4)
h.addEdge(1,2)
h.addEdge(1,3)
h.addEdge(1,4)
h.addEdge(2,3)
h.addEdge(3,4)

h.bfs(0)

