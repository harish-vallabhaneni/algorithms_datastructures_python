import sys
import os
import unittest
from collections import defaultdict


class Graph:
	def __init__(self):
		self.vertices = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertices[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertices:
			return self.vertices[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertices

	def addEdge(self, f, t, cost=0):
		if f not in self.vertices:
			nv = self.addVertex(f)
		if t not in self.vertices:
			nv = self.addVertex(t)
		self.vertices[f].addNeighbor(self.vertices[t], cost)
		self.vertices[t].addNeighbor(self.vertices[f], cost)

	def getVertices(self):
		return list(self.vertices.keys())

	def __iter__(self):
		return iter(self.vertices.values())


class Vertex:
	def __init__(self, num):
		self.id = num
		self.connectedTo = {}
		self.color = 'white'
		self.dist = sys.maxsize
		self.pred = None
		self.disc = 0
		self.fin = 0

	# def __lt__(self,o):
	#     return self.id < o.id

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def setColor(self, color):
		self.color = color

	def setDistance(self, d):
		self.dist = d

	def setPred(self, p):
		self.pred = p

	def setDiscovery(self, dtime):
		self.disc = dtime

	def setFinish(self, ftime):
		self.fin = ftime

	def getFinish(self):
		return self.fin

	def getDiscovery(self):
		return self.disc

	def getPred(self):
		return self.pred

	def getDistance(self):
		return self.dist

	def getColor(self):
		return self.color

	def getConnections(self):
		return self.connectedTo.keys()

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def __str__(self):
		return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

	def getId(self):
		return self.id


class PriorityQueue:
	def __init__(self):
		self.heapArray = [(0, 0)]
		self.currentSize = 0

	def buildHeap(self, alist):
		self.currentSize = len(alist)
		self.heapArray = [(0, 0)]
		for i in alist:
			self.heapArray.append(i)
		i = len(alist) // 2
		while (i > 0):
			self.percDown(i)
			i = i - 1

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapArray[i][0] > self.heapArray[mc][0]:
				tmp = self.heapArray[i]
				self.heapArray[i] = self.heapArray[mc]
				self.heapArray[mc] = tmp
			i = mc

	def minChild(self, i):
		if i*2 > self.currentSize:
			return -1
		else:
			if i*2 + 1 > self.currentSize:
				return i*2
			else:
				if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
					return i*2
				else:
					return i*2+1

	def percUp(self, i):
		while i // 2 > 0:
			if self.heapArray[i][0] < self.heapArray[i//2][0]:
				tmp = self.heapArray[i//2]
				self.heapArray[i//2] = self.heapArray[i]
				self.heapArray[i] = tmp
			i = i//2

	def add(self, k):
		self.heapArray.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def delMin(self):
		retval = self.heapArray[1][1]
		self.heapArray[1] = self.heapArray[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapArray.pop()
		self.percDown(1)
		return retval

	def isEmpty(self):
		if self.currentSize == 0:
			return True
		else:
			return False

	def decreaseKey(self, val, amt):
		# this is a little wierd, but we need to find the heap thing to decrease by
		# looking at its value
		done = False
		i = 1
		myKey = 0
		while not done and i <= self.currentSize:
			if self.heapArray[i][1] == val:
				done = True
				myKey = i
			else:
				i = i + 1
		if myKey > 0:
			self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
			self.percUp(myKey)

	def __contains__(self, vtx):
		for pair in self.heapArray:
			if pair[1] == vtx:
				return True
		return False


def dijkstra(aGraph, start):
	pq = PriorityQueue()
	dist = dict()
	graph = aGraph
	start_vtx = graph.getVertex(start)
	start_vtx.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in aGraph])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		dist[currentVert.getId()] = currentVert.getDistance()
		for nextVert in currentVert.getConnections():
			newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
			if newDist < nextVert.getDistance():
				nextVert.setDistance(newDist)
				nextVert.setPred(currentVert)
				pq.decreaseKey(nextVert, newDist)

	print('Vertex\tDistance from Source')
	for vtx, distance in dist.items():
		print(str(vtx)+'\t'+str(distance))


def prim(G, start):
	pq = PriorityQueue()
	mst = []
	for v in G:
		v.setDistance(sys.maxsize)
		v.setPred(None)
	graph = G
	start_vtx = graph.getVertex(start)
	start_vtx.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in G])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		if not currentVert.getPred() == None:
			Pred = currentVert.getPred().getId()
			mst.append([Pred, currentVert.getId()])
		for nextVert in currentVert.getConnections():
			newCost = currentVert.getWeight(nextVert)
			if nextVert in pq and newCost < nextVert.getDistance():
				nextVert.setPred(currentVert)
				nextVert.setDistance(newCost)
				pq.decreaseKey(nextVert, newCost)

	print('Source Vertex\tDest Vertex\tDistance from Source')
	for i in mst:
		print(str(i[0])+'\t\t'+str(i[1]))


graph = Graph()
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
#dijkstra(graph, 0)
prim(graph, 0)
