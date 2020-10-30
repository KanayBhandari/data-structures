# linked list (introduction)

# class Node:

# 	# Function to initialize node object
# 	def __init__(self,data):
# 		self.data = data	# Assign data
# 		self.next = None	# Initialize next as null


# # Linked list class contains a node object
# class LinkedList:

# 	# Funtion to initialize head
# 	def __init__(self):
# 		self.head = None

# 	# This function prints the content of linked list starting from head
# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next



# if __name__ == '__main__':

# 	# Start with the empty list
# 	llist = LinkedList()

# 	llist.head = Node(1)
# 	second = Node(2)
# 	third = Node(3)

# 	llist.head.next = second
# 	second.next = third

# 	llist.printList()


################################################################################################
# Liked list inserting a node
# 1. At the front of the list
# 2. After a given node
# 3. At the end of linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def insertAfter(self,prev_node,data):
		
# 		if prev_node is None:
# 			print("The given previous node must in linked list")
# 			return

# 		new_node = Node(data)
# 		new_node.next = prev_node.next
# 		prev_node.next = new_node

# 	def append(self,data):
# 		new_node = Node(data)
# 		if self.head is None:
# 			self.head = new_node
# 			return
		
# 		last = self.head
# 		while(last.next):
# 			last = last.next

# 		last.next = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.append(6)
# 	llist.push(3)
# 	llist.push(5)
# 	llist.insertAfter(llist.head.next,8)
# 	llist.append(9)

# 	llist.printList()

################################################################################################
# Deleting a node in linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def deleteNode(self,key):
# 		temp = self.head

# 		if temp is not None:
# 			if temp.data == key:
# 				self.head = temp.next
# 				temp = None
# 				return

# 		while temp is not None:
# 			if temp.data == key:
# 				break

# 			prev = temp
# 			temp = temp.next

# 		if temp == None:
# 			return

# 		prev.next = temp.next
# 		temp = None

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# if __name__ == '__main__':
# 	llist = LinkedList()
# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)

# 	llist.deleteNode(3)

# 	llist.printList()

################################################################################################
# Delete a linked list node at a given position

# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def deleteNode(self,position):
# 		if self.head is None:
# 			return

# 		temp = self.head

# 		if position == 0:
# 			self.head = temp.next
# 			temp = None
# 			return

# 		for i in range(position-1):
# 			temp = temp.next
# 			if temp is None:
# 				break

# 		if temp is None:
# 			return
# 		if temp.next is None:
# 			return

# 		next = temp.next.next
# 		temp.next = None
# 		temp.next = next

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)

# 	llist.deleteNode(0)

# 	llist.printList()


################################################################################################
# Write a function to delete a linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def deleteList(self):
# 		current = self.head

# 		while(current):
# 			prev = current.next
# 			del current.data
# 			current = prev

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)
# 	llist.push(4)
# 	llist.push(5)

# 	llist.printList()

# 	print("deleting linked list : ")
# 	llist.deleteList()
# 	print("\nlinked list deleted no data left in node object\n")

# 	llist.printList()


################################################################################################
# Find length of linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# 	def count(self):
# 		temp = self.head
# 		count = 0
# 		while(temp):
# 			count += 1
# 			temp = temp.next
# 		return count

# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)
# 	llist.push(4)
# 	llist.push(5)

# 	print("The elements in the linked list are : ")
# 	llist.printList()

# 	print("The number of nodes in the linked list are : ",llist.count())


################################################################################################
# Search an element in linked list (iterative and recursive)

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# 	def search(self,key):
# 		current = self.head

# 		while(current):
# 			if current.data == key:
# 				return True 	# data found
# 			current = current.next

# 		return False # data not found

# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)
# 	llist.push(4)

# 	print("The elements in the linked list are : ")
# 	llist.printList()

# 	print("Element 3 exist in linked list : ",llist.search(3))


################################################################################################
# Recursive Method to find a element in the linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# 	def search(self,li,key):
# 		if not li:
# 			return False

# 		while(li):
# 			if li.data == key:
# 				return True
# 			return self.search(li.next,key)


# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)
# 	llist.push(4)

# 	print("The elements in the linked list are : ")
# 	llist.printList()

# 	print("element 3 exits : ",llist.search(llist.head,3))


################################################################################################
# Function to get the nth node in the linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next

# 	def getNth(self,index):
# 		current = self.head
# 		count = 0

# 		while(current):
# 			if count == index:
# 				return current.data

# 			count += 1
# 			current = current.next


# if __name__ == '__main__':
# 	llist = LinkedList()

# 	llist.push(1)
# 	llist.push(2)
# 	llist.push(3)
# 	llist.push(4)

# 	print("The elements in the linked list are : ")
# 	llist.printList()

# 	print("element : ",llist.getNth(1))


################################################################################################
# Reverse a linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def reverse(self):
		prev = None
		current = self.head
		while(current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

if __name__ == '__main__':
	llist = LinkedList()

	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)

	llist.printList()

	print("Reversing the linked list : ")
	llist.reverse()

	llist.printList()
