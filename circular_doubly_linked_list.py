# Doubly circular linked list insertion and traversal

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# class CircularDoublyLinkedList:
# 	def __init__(self):
# 		self.start = None

# 	def insertEnd(self,data):
# 		if self.start == None:
# 			new_node = Node(data)
# 			new_node.next = new_node.prev = new_node
# 			self.start = new_node
# 			return

# 		last = self.start.prev
# 		new_node = Node(data)
# 		new_node.next = self.start
# 		last.next = self.start.prev = new_node
# 		new_node.prev = last

# 	def insertBegin(self,data):
# 		new_node = Node(data)
# 		last = self.start.prev

# 		new_node.next = self.start
# 		self.start.prev = last.next = new_node
# 		new_node.prev = last
# 		self.start = new_node

# 	def insertAfter(self,data1,data2):
# 		new_node = Node(data2)
# 		temp = self.start
# 		while(temp.data != data1):
# 			temp = temp.next
# 		next = temp.next
# 		new_node.prev = temp
# 		new_node.next = next
# 		next.prev = temp.next = new_node

# 	def display(self):
# 		temp = self.start
# 		if temp is None:
# 			print("list is empty")
# 			return

# 		print("Traversal in forward direction.")
# 		while(temp.next != self.start):
# 			print(temp.data,end=' ')
# 			temp = temp.next
# 		print(temp.data)

# 		print("Traversal in backward direction.")
# 		last = self.start.prev
# 		temp = last
# 		if temp is None:
# 			print("list is empty")
# 			return

# 		while(temp.prev != last):
# 			print(temp.data,end=' ')
# 			temp = temp.prev
# 		print(temp.data)

# if __name__ == '__main__':
# 	llist = CircularDoublyLinkedList()

# 	llist.insertEnd(10)
# 	llist.insertEnd(20)
# 	llist.insertBegin(30)
# 	llist.insertBegin(40)
# 	llist.insertAfter(10,70)

# 	llist.display()

#######################################################################################################
# Deleting a node in doubly circular linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class CircularDoublyLinkedList:
	def __init__(self):
		self.start = None

	def insertEnd(self,data):
		if self.start == None:
			new_node = Node(data)
			new_node.next = new_node.prev = new_node
			self.start = new_node
			return

		last = self.start.prev
		new_node = Node(data)
		new_node.next = self.start
		last.next = self.start.prev = new_node
		new_node.prev = last

	def display(self):
		temp = self.start
		if temp is None:
			print("list is empty")
			return

		print("Traversal in forward direction.")
		while(temp.next != self.start):
			print(temp.data,end=' ')
			temp = temp.next
		print(temp.data)

		# print("Traversal in backward direction.")
		# last = self.start.prev
		# temp = last
		# if temp is None:
		# 	print("list is empty")
		# 	return

		# while(temp.prev != last):
		# 	print(temp.data,end=' ')
		# 	temp = temp.prev
		# print(temp.data)

	def deleteNode(self,key):
		# If list is empty
		if self.start is None:
			return

		# Find the required node
		# Declare two pointers and initialize them
		curr = self.start
		prev1 = None

		while(curr.data != key):
			# If node is not present in the list
			if curr.next == self.start:
				print("list does not have the node ",key)
			prev1 = curr
			curr = curr.next

		# Check if the node is the only node in the list
		if curr.next == self.start and prev1 == None:
			self.start = None
			return

		# If list has more than one node
		# Check if it is the first node
		if curr == self.start:
			prev1 = self.start.prev
			self.start = self.start.next
			self.start.prev = prev1
			prev1.next = self.start
		# Check if it is the last node
		elif curr.next == self.start:
			prev1.next = self.start
			self.start.prev = prev1
		else:
			# Create a new pointer
			# Points to next of curr node
			temp = curr.next

			prev1.next = temp
			temp.prev = prev1

if __name__ == '__main__':
	llist = CircularDoublyLinkedList()

	llist.insertEnd(10)
	llist.insertEnd(20)

	print("original list :")
	llist.display()

	print("After deletion :")
	llist.deleteNode(20)

	llist.display()