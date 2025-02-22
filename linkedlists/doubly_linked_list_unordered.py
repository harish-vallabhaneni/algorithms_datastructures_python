# A complete working Python program to demonstrate all 
# for Garbage collection 
import gc 
 
# A linked list node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
  
# Class to create a Doubly Linked List 
class DoublyLinkedList: 
  
    # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None
  
    # Given a reference to the head of a list and an 
    # integer, inserts a new node on the front of list 
    def push(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put the data in it 
        new_node = Node(new_data) 
  
        # 3. Make next of new node as head and 
        # previous as None (already None) 
        new_node.next = self.head 
  
        # 4. change prev of head node to new_node 
        if self.head is not None: 
            self.head.prev = new_node 
  
        # 5. move the head to point to the new node 
        self.head = new_node 
  
    # Given a node as prev_node, insert a new node after 
    # the given node 
    def insertAfter(self, prev_node, new_data): 
  
        # 1. Check if the given prev_node is None 
        if prev_node is None: 
            print "the given previous node cannot be NULL"
            return 
  
        # 2. allocate new node 
        # 3. put in the data 
        new_node = Node(new_data) 
  
        # 4. Make net of new node as next of prev node 
        new_node.next = prev_node.next
  
        # 5. Make prev_node as previous of new_node 
        prev_node.next = new_node 
  
        # 6. Make prev_node ass previous of new_node 
        new_node.prev = prev_node 
  
        # 7. Change previous of new_nodes's next node 
        if new_node.next is not None: 
            new_node.next.prev = new_node 
  
    # Given a reference to the head of DLL and integer, 
    # appends a new node at the end 
    def append(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put in the data 
        new_node = Node(new_data) 
  
        # 3. This new node is going to be the last node, 
        # so make next of it as None 
        new_node.next = None
  
        # 4. If the Linked List is empty, then make the 
        # new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
  
        # 5. Else traverse till the last node 
        last = self.head 
        while(last.next is not None): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next = new_node 
  
        # 7. Make last node as previous of new node 
        new_node.prev = last 
  
        return
  
    # This function prints contents of linked list 
    # starting from the given node 
    def printList(self, node): 
  
        print "\nTraversal in forward direction"
        while(node is not None): 
            print " % d" %(node.data), 
            last = node 
            node = node.next
  
        print "\nTraversal in reverse direction"
        while(last is not None): 
            print " % d" %(last.data), 
            last = last.prev 

   # Function to delete a node in a Doubly Linked List. 
   # head_ref --> pointer to head node pointer. 
   # dele --> pointer to node to be deleted 
  
    def deleteNode(self, dele): 
          
        # Base Case 
        if self.head is None or dele is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == dele: 
            self.head = dele.next
  
        # Change next only if node to be deleted is NOT 
        # the last node 
        if dele.next is not None: 
            dele.next.prev = dele.prev 
      
        # Change prev only if node to be deleted is NOT  
        # the first node 
        if dele.prev is not None: 
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele 
        # Call python garbage collector 
        gc.collect()

    # Function reverse a Doubly Linked List 
    def reverse(self): 
        temp = None
        current = self.head 
          
        # Swap next and prev for all nodes of  
        # doubly linked list 
        while current is not None: 
            temp = current.prev  
            current.prev = current.next
            current.next = temp 
            current = current.prev 
  
        # Before changing head, check for the cases like  
        # empty list and list with only one node 
        if temp is not None: 
            self.head = temp.prev 
 
# Driver program to test above functions 
  
# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
llist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 
  
print "Created DLL is: ", 
llist.printList(llist.head) 

# Start with empty list 
dll = DoublyLinkedList() 
  
# Let us create the doubly linked list 10<->8<->4<->2 
dll.push(2); 
dll.push(4); 
dll.push(8); 
dll.push(10); 
  
print "\n Original Linked List", 
dll.printList(dll.head) 

# Reverse doubly linked list
dll.reverse()

print "\n Reversed Linked List"
dll.printList(dll.head)
  
# delete nodes from doubly linked list 
dll.deleteNode(dll.head) 
dll.deleteNode(dll.head.next) 
dll.deleteNode(dll.head.next) 
# Modified linked list will be NULL<-8->NULL 
print "\n Modified Linked List", 
dll.printList(dll.head)

print "\nOriginal Linked List"
dll.printList(dll.head) 
