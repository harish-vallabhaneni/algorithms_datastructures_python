from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def addEdge(self, frm, to):
		self.graph[frm].append(to)
		self.graph[to].append(frm)

	def isCyclic(self):
		visited = [False] * self.vertices
		for vtx in range(self.vertices):
			if visited[vtx] == False:
				if self.isCyclicUtil(vtx, visited, -1) == True:
					return True
			else:
				return False

	def isCyclicUtil(self, vtx, visited, parent):
		visited[vtx] = True
		for nbr in self.graph[vtx]:
			if visited[nbr] == False:
				if self.isCyclicUtil(nbr, visited, vtx) == True:
					return True
			elif parent != nbr:
				return True
		return False



g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(5,2)
g.addEdge(5,6)
g.addEdge(5,7)

print(g.isCyclic())

