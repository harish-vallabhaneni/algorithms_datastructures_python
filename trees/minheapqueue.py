import heapq

data = [9,8,7,6,5,4,3,2]

print('Before heapifying: '+str(data))

heapq.heapify(data)

print('After heapifying: '+str(data))

heapq.heappush(data, 1)

print('Updated heap structure after pushing element "1": '+str(data))

heapq.heappop(data)

print('Updated heap structure after popping the smaller element is: '+str(data))

heapq.heappushpop(data, 13)

print('Updated heap structure after pushing element "13" and popping the smallest element is: '+str(data))

heapq.heapreplace(data, 19)

print('Updated heap structure after popping the smallest element and pushing the newest element "19" is: '+str(data))

smallest = heapq.nsmallest(3, data)

print('The 3 smallest elements of the heap structure are: '+str(smallest))

largest = heapq.nlargest(3, data)

print('The 3 largest elements of the heap structure are: '+str(largest))
