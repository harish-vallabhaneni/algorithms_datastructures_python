#bfs for directed graph

from collections import defaultdict
from queue import Queue

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

	def bfs(self, source, total_vertices):
		visited = [False] * total_vertices
		print("adjacency list: "+str(self.graph))
		queue = Queue()
		for vertex in range(total_vertices):
			if visited[vertex] == False:
				queue.put(vertex)
				while not queue.empty():
					vtx = queue.get()
					print(vtx)
					for nbr in self.graph[vtx]:
						if visited[nbr] == False:
							queue.put(nbr)
							visited[nbr] = True

h = Graph()
Vertices = 5
h.addEdge(0,4)
h.addEdge(1,2)
h.addEdge(1,3)
h.addEdge(1,4)
h.addEdge(2,3)
h.addEdge(3,4)

#This program will fail if the following edges were added where the to vertex doesn't have a key created in self.graph defaultdict
#g.addEdge(5,6)
#g.addEdge(5,7)

h.bfs(0, 5)

