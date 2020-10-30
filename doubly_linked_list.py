# Insertion in Doubly Linked List

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	# Inserts a new_node at the front of the list
# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node
		
# 		self.head = new_node

# 	# Insert a new_node after a given previous node
# 	def insertAfter(self,prev,data):
# 		if prev is None:
# 			print("prev cannot be null")
# 			return

# 		new_node = Node(data)
# 		new_node.next = prev.next
# 		new_node.prev = prev
# 		prev.next = new_node

# 		if new_node.next is not None:
# 			new_node.next.prev = new_node

# 	# Insert a new_node at the end
# 	def append(self,data):
# 		new_node = Node(data)
# 		new_node.next = None

# 		if self.head is None:
# 			new_node.prev = None
# 			self.head = new_node
# 			return

# 		last = self.head
# 		while (last.next is not None):
# 			last = last.next

# 		last.next = new_node
# 		new_node.prev = last

# 		return


# 	def printList(self,node):
# 		print("Traversal in forward direction : ")
# 		while(node is not None):
# 			print(node.data)
# 			last = node
# 			node = node.next

# 		print("Traversal in reverse direction")
# 		while(last is not None):
# 			print(last.data)
# 			last = last.prev

# if __name__ == '__main__':
# 	llist = DoublyLinkedList()

# 	llist.append(6)
# 	llist.push(7)
# 	llist.push(1)
# 	llist.append(4)

# 	llist.insertAfter(llist.head.next,8)

# 	print("DLL created is : ")
# 	llist.printList(llist.head)

#########################################################################################################
# Deleting a node in doubly linked list
# 1. Deletion of head node
# 2. Deletion of middle node
# 3. Deletion of last node

# import gc

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def deleteNode(self,dele):
# 		# Base Case
# 		if self.head is None or dele is None:
# 			return

# 		# if node to be deleted is head node
# 		if self.head == dele:
# 			self.head = dele.next

# 		# change next only if node to be deleted is not the last node
# 		if dele.next is not None:
# 			dele.next.prev = dele.prev

# 		# change prev only if node to be deleted is not the first node
# 		if dele.prev is not None:
# 			dele.prev.next = dele.next

# 		# finally free the memory occupy by the dele ....call python garbaze collector
# 		gc.collect()


# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node

# 		self.head = new_node

# 	def printList(self,node):
# 		while node is not None:
# 			print(node.data)
# 			node = node.next

# if __name__ == '__main__':
# 	llist = DoublyLinkedList()

# 	llist.push(2)
# 	llist.push(4)
# 	llist.push(8)
# 	llist.push(10)

# 	print("Original doubly linked list")
# 	llist.printList(llist.head)	

# 	llist.deleteNode(llist.head)
# 	llist.deleteNode(llist.head.next)
# 	llist.deleteNode(llist.head.next)
# 	print("Modified doubly linked list")
# 	llist.printList(llist.head)


#########################################################################################################
# Deleting a doubly linked list node at a given position
# import gc

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def deleteNode(self,dele):
# 		if self.head is None or dele is None:
# 			return

# 		if self.head == dele:
# 			self.head = dele.next

# 		if dele.next is not None:
# 			dele.next.prev = dele.prev

# 		if dele.prev is not None:
# 			dele.prev.next = dele.next

# 		gc.collect()

# 	def deleteNodeAtGivenPos(self,position):
# 		if self.head is None or position <= 0:
# 			return

# 		current = self.head
# 		i = 1

# 		# Traverse upto the node at position from beginning
# 		while(current is not None and i < position):
# 			current = current.next
# 			i += 1

# 		# if position is greater than number of nodes
# 		if current == None:
# 			return

# 		# delete the node pointed by current
# 		self.deleteNode(current)

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node

# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp is not None):
# 			print(temp.data)
# 			last = temp
# 			temp = temp.next

# 		print("doubly linked list in reverse order : ")
# 		while(last is not None):
# 			print(last.data)
# 			last = last.prev

# if __name__ == '__main__':
# 	llist = DoublyLinkedList()

# 	llist.push(5)
# 	llist.push(2)
# 	llist.push(4)
# 	llist.push(8)
# 	llist.push(10)

# 	print("Doubly Linked list before deletion : ")
# 	llist.printList()

# 	llist.deleteNodeAtGivenPos(2)

# 	print("Doubly Linked list after deletion : ")
# 	llist.printList()

#########################################################################################################
# Remove duplicates from a sorted doubly linked list

# import gc

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def deleteNode(self,dele):
# 		if self.head is None or dele is None:
# 			return

# 		if self.head == dele:
# 			self.head = dele.next

# 		if dele.next is not None:
# 			dele.next.prev = dele.prev

# 		if dele.prev is not None:
# 			dele.prev.next = dele.next

# 		gc.collect()

# 	def removeDuplicates(self):
# 		if self.head is None:
# 			return

# 		current = self.head

# 		while current.next is not None:
# 			if current.data == current.next.data:
# 				self.deleteNode(current.next)
# 			else:
# 				current = current.next

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node

# 		self.head = new_node

# 	def printList(self):
# 		current = self.head
# 		while(current):
# 			print(current.data)
# 			current = current.next

# if __name__ == "__main__":
# 	llist = DoublyLinkedList()

# 	llist.push(12)
# 	llist.push(12)
# 	llist.push(10)
# 	llist.push(8)
# 	llist.push(8)
# 	llist.push(6)
# 	llist.push(4)
# 	llist.push(4)
# 	llist.push(4)
# 	llist.push(4)

# 	print("Original Doubly linked list : ")
# 	llist.printList()

# 	llist.removeDuplicates()

# 	print("Doubly linked list after removing duplicates : ")
# 	llist.printList()

#########################################################################################################
# Delete all occurances of a given key in a doubly linked list

# import gc

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def deleteNode(self,dele):
# 		if self.head is None or dele is None:
# 			return

# 		if self.head == dele:
# 			self.head = dele.next

# 		if dele.next is not None:
# 			dele.next.prev = dele.prev

# 		if dele.prev is not None:
# 			dele.prev.next = dele.next

# 		gc.collect()

# 	def removeDuplicates(self):
# 		if self.head is None:
# 			return

# 		current = self.head

# 		while current.next is not None:
# 			if current.data == current.next.data:
# 				self.deleteNode(current.next)
# 			else:
# 				current = current.next

# 	def deleteAllOccurOfKey(self,key):
# 		if self.head is None:
# 			return

# 		current = self.head

# 		while(current is not None):
# 			if current.data == key:
# 				next = current.next
# 				self.deleteNode(current)
# 				current = next
# 			else:
# 				current = current.next

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node

# 		self.head = new_node

# 	def printList(self):
# 		current = self.head
# 		while(current):
# 			print(current.data)
# 			current = current.next

# if __name__ == "__main__":
# 	llist = DoublyLinkedList()

# 	llist.push(12)
# 	llist.push(12)
# 	llist.push(10)
# 	llist.push(8)
# 	llist.push(8)
# 	llist.push(6)
# 	llist.push(4)
# 	llist.push(4)
# 	llist.push(4)
# 	llist.push(4)

# 	print("Original Doubly linked list : ")
# 	llist.printList()

# 	llist.deleteAllOccurOfKey(4)
# 	llist.deleteAllOccurOfKey(12)

# 	print("Doubly linked list after removing all occurances of 4 and 12: ")
# 	llist.printList()

#########################################################################################################
# Remove duplicates in unsorted doubly linked list

# import gc

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class DoublyLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def deleteNode(self,dele):
# 		if self.head is None or dele is None:
# 			return

# 		if self.head == dele:
# 			self.head = dele.next

# 		if dele.next is not None:
# 			dele.next.prev = dele.prev

# 		if dele.prev is not None:
# 			dele.prev.next = dele.next

# 		gc.collect()

# 	def removeDuplicates(self):
# 		if self.head is None or self.head.next is None:
# 			return

# 		ptr1 = self.head
# 		ptr2 = None

# 		while(ptr1 != None):
# 			ptr2 = ptr1.next

# 			while(ptr2 != None):
# 				if ptr1.data == ptr2.data:
# 					next = ptr2.next
# 					self.deleteNode(ptr2)
# 					ptr2 = next
# 				else:
# 					ptr2 = ptr2.next

# 			ptr1 = ptr1.next


# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head

# 		if self.head is not None:
# 			self.head.prev = new_node

# 		self.head = new_node

# 	def printList(self):
# 		current = self.head
# 		while(current):
# 			print(current.data)
# 			current = current.next

# if __name__ == "__main__":
# 	llist = DoublyLinkedList()

# 	llist.push(12)
# 	llist.push(12)
# 	llist.push(10)
# 	llist.push(4)
# 	llist.push(8)
# 	llist.push(4)
# 	llist.push(6)
# 	llist.push(4)
# 	llist.push(4)
# 	llist.push(8)

# 	print("Original Doubly linked list : ")
# 	llist.printList()

# 	llist.removeDuplicates()

# 	print("removing duplicates in unsorted Doubly linked list : ")
# 	llist.printList()

#########################################################################################################
# Reverse a doubly linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		temp = None
		current = self.head

		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev

		# before changing head, check for the cases like empty list and list with only one node
		if temp is not None:
			self.head = temp.prev

	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def printList(self):
		current = self.head
		while(current):
			print(current.data)
			current = current.next

if __name__ == '__main__':
	llist = DoublyLinkedList()

	llist.push(2)
	llist.push(4)
	llist.push(8)
	llist.push(10)

	print("Original DLL : ")
	llist.printList()

	llist.reverse()

	print("after reversing the DLL :")
	llist.printList()

#########################################################################################################