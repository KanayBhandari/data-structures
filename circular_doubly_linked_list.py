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

	def insertBegin(self,data):
		new_node = Node(data)
		last = self.start.prev

		new_node.next = self.start
		self.start.prev = last.next = new_node
		new_node.prev = last
		self.start = new_node

	def insertAfter(self,data1,data2):
		new_node = Node(data2)
		temp = self.start
		while(temp.data != data1):
			temp = temp.next
		next = temp.next
		new_node.prev = temp
		new_node.next = next
		next.prev = temp.next = new_node

	def display(self):
		temp = self.start
		if temp is None:
			print("list is empty")
			return

		print("Traversal in forward direction.")
		while(temp.next != self.start):
			print(temp.data)
			temp = temp.next
		print(temp.data)

		print("Traversal in backward direction.")
		last = self.start.prev
		temp = last
		if temp is None:
			print("list is empty")
			return

		while(temp.prev != last):
			print(temp.data)
			temp = temp.prev
		print(temp.data)

if __name__ == '__main__':
	llist = CircularDoublyLinkedList()

	llist.insertEnd(10)
	llist.insertEnd(20)
	llist.insertBegin(30)
	llist.insertBegin(40)
	llist.insertAfter(10,70)

	llist.display()