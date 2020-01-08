#bfs for directed graph

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, frm, to):
		self.graph[frm].append(to)

	def bfs(self, source):
		visited = [False] * (len(self.graph))

		print("adjacency list: "+str(self.graph))
		
		queue = []

		queue.append(source)
		visited[source] = True

		while queue:
			vtx = queue.pop(0)
			print(vtx)
			for nbr in self.graph[vtx]:
				if visited[nbr] == False:
					queue.append(nbr)
					visited[nbr] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(5,2)

#This program will fail if the following edges were added where the to vertex doesn't have a key created in self.graph defaultdict
#g.addEdge(5,6)
#g.addEdge(5,7)

g.bfs(0)
