#detect cycle in a directed graph using dfs

from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def addEdge(self, frm, to):
		self.graph[frm].append(to)

	def isCyclic(self):
		visited = [False] * len(self.graph)
		recursionstack = [False] * len(self.graph)
		for vtx in range(self.vertices):
			if self.isCyclicUtil(vtx, visited, recursionstack) == True:
				return True
			else:
				return False

	def isCyclicUtil(self, vtx, visited, recursionstack):
		visited[vtx] = True
		recursionstack[vtx] = True
		for nbr in self.graph[vtx]:
			if visited[nbr] == False:
				if self.isCyclicUtil(nbr, visited, recursionstack) == True:
					return True
			elif recursionstack[vtx] == True:
				return True
		recursionstack[vtx] = False
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

