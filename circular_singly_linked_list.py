# Circular singly linked list insertion

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CircularLinkedList:
# 	def __init__(self):
# 		self.last = None

# 	def addToEmpty(self,data):
# 		if self.last != None:
# 			return 

# 		temp = Node(data)
# 		self.last = temp

# 		self.last.next = self.last

# 	def addBegin(self,data):
# 		if self.last is None:
# 			return self.addToEmpty(data)

# 		temp = Node(data)
# 		temp.next = self.last.next
# 		self.last.next = temp

# 	def addEnd(self,data):
# 		if self.last is None:
# 			return self.addToEmpty(data)

# 		temp = Node(data)
# 		temp.next = self.last.next
# 		self.last.next = temp
# 		self.last = temp

# 	def addAfter(self,data,item):
# 		if self.last is None:
# 			return None

# 		temp = Node(data)
# 		p = self.last.next

# 		while(p):
# 			if p.data == item:
# 				temp.next = p.next
# 				p.next = temp

# 				if p == self.last:
# 					self.last = temp
# 					return
# 				else:
# 					return

# 			p = p.next
# 			if p == self.last.next:
# 				print(item,"not present in the list")
# 				break

# 	def traverse(self):
# 		if self.last is None:
# 			print("Circular linked list is empty")
# 			return
# 		temp = self.last.next
# 		while(temp):
# 			print(temp.data,end=' ')
# 			temp = temp.next

# 			if temp == self.last.next:
# 				break

# if __name__ == '__main__':
# 	llist = CircularLinkedList()
# 	llist.addToEmpty(6)
# 	llist.addBegin(4)
# 	llist.addBegin(2)
# 	llist.addEnd(8)
# 	llist.addEnd(12)
# 	llist.addAfter(10,8)

# 	llist.traverse()

#######################################################################################################
# circular linked list traversal

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CircularLinkedList:
# 	def __init__(self):
# 		self.last = None

# 	def push(self,data):
# 		if self.last is None:
# 			temp = Node(data)
# 			self.last = temp
# 			temp.next = self.last.next
# 			self.last.next = temp
# 			return

# 		temp = Node(data)
# 		temp.next = self.last.next
# 		self.last.next = temp

# 	def printList(self):
# 		if self.last is None:
# 			print("list is empty")
# 			return

# 		temp = self.last.next
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next
# 			if temp == self.last.next:
# 				break

# if __name__ == '__main__':
# 	llist = CircularLinkedList()

# 	llist.push(10)
# 	llist.push(20)

# 	llist.printList()

#######################################################################################################
# circular linked list using head node

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CircularLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		temp = self.head
# 		new_node.next = self.head

# 		if self.head is not None:
# 			while (temp.next != self.head):
# 				temp = temp.next
# 			temp.next = new_node
# 		else:
# 			new_node.next = new_node
# 		self.head = new_node

# 	def printList(self):
# 		temp = self.head
# 		if self.head is None:
# 			print("list is empty")
# 			return
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next
# 			if temp == self.head:
# 				break

# if __name__ == '__main__':
# 	llist = CircularLinkedList()

# 	llist.push(100)
# 	llist.push(200)

# 	llist.printList()

#######################################################################################################
# Sorted insert for circular linked list

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CircularLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def push(self,data):
# 		new_node = Node(data)
# 		temp = self.head
# 		new_node.next = self.head

# 		if self.head is not None:
# 			while (temp.next != self.head):
# 				temp = temp.next
# 			temp.next = new_node
# 		else:
# 			new_node.next = new_node
# 		self.head = new_node

# 	def sortedInsert(self,data):
# 		new_node = Node(data)

# 		current = self.head

# 		if current is None:
# 			new_node.next = new_node
# 			self.head = new_node

# 		elif current.data >= new_node.data:
# 			while current.next != self.head:
# 				current = current.next
# 			current.next = new_node
# 			new_node.next = self.head
# 			self.head = new_node
# 		else:
# 			while current.next != self.head and current.next.data < new_node.data:
# 				current = current.next
# 			new_node.next = current.next
# 			current.next = new_node

# 	def printList(self):
# 		current = self.head
# 		if current is None:
# 			print("list is empty")
# 			return

# 		while(current):
# 			print(current.data)
# 			current = current.next
# 			if current == self.head:
# 				break

# if __name__ == '__main__':
# 	llist = CircularLinkedList()

# 	llist.sortedInsert(10)
# 	llist.sortedInsert(2)
# 	llist.sortedInsert(20)
# 	llist.sortedInsert(6)
# 	llist.sortedInsert(30)
# 	llist.sortedInsert(10)

# 	llist.printList()

#######################################################################################################
# check if a linked list is circular

# class Node:
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None

# class CircularLinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def circular(self):
# 		current = self.head

# 		if current is None:
# 			return True

# 		node = self.head.next

# 		while node != None and node != self.head:
# 			node = node.next

# 		if node == self.head:
# 			return True
# 		else:
# 			return False

# if __name__ == '__main__':
# 	llist = CircularLinkedList()

# 	llist.head = Node(10)
# 	second = Node(2)
# 	third = Node(3)

# 	llist.head.next = second
# 	second.next = third
# 	third.next = llist.head

# 	if (llist.circular()):
# 		print("circular linked list")
# 	else:
# 		print("not a circular linked list")

#######################################################################################################
# Deletion from circular linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None

	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head

		temp = self.head

		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = new_node
		else:
			new_node.next = new_node

		self.head = new_node

	def deleteNode(self,head,key):
		if head is None:
			return

		if head.data == key and head.next == head:
			head = None

		last = head
		d = None

		if head.data == key:
			while last.next != head:
				last = last.next
			last.next = head.next
			head = last.next

		while last.next != head and last.next.data != key:
			last = last.next

		if last.next.data == key:
			d = last.next
			last.next = d.next
		else:
			print("no key found")

	# def printList(self):
	# 	if self.head is None:
	# 		print("list is empty")
	# 		return
	# 	head = self.head
	# 	temp = head
	# 	while(temp):
	# 		print(temp.data)
	# 		temp = temp.next
	# 		if temp == self.head:
	# 			break

	def printList(self):
		current = self.head
		if current is None:
			print("list is empty")
			return

		while(current):
			print(current.data)
			current = current.next
			if current == self.head:
				break

if __name__ == '__main__':
	llist = CircularLinkedList()

	llist.push(10)
	llist.push(20)

	print("original list")
	llist.printList()

	llist.deleteNode(llist.head,20)

	print("after deletion")
	llist.printList()