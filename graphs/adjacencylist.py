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

	def addedge(self, frm, to, weight=0):
		if frm not in self.vertices:
			newfrmvertex = self.addVertex(frm)
		if to not in self.vertices:
			newtovertex = self.addVertes(to)
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

