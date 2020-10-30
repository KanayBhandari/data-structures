# Implementing stack using array

# from sys import maxsize

# def createStack():
# 	stack = []
# 	return stack

# def isEmpty(stack):
# 	return len(stack) == 0

# def push(stack, item):
# 	stack.append(item)
# 	print(item," pushed to stack")

# def pop(stack):
# 	if (isEmpty(stack)):
# 		return str(-maxsize-1)
# 	return stack.pop()

# def peek(stack):
# 	if (isEmpty(stack)):
# 		return str(-maxsize-1)
# 	return stack[len(stack)-1]


# stack = createStack()
# push(stack,10)
# push(stack,20)
# push(stack,30)
# print(pop(stack),"popped from stack")

#######################################################################################################
# Linked list implementation of stack

class StackNode:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self,data):
		new_node = StackNode(data)
		new_node.next = self.root
		self.root = new_node
		print(data," pushed to stack")

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		popped = temp.data
		self.root = self.root.next
		return popped

	def peek(self):
		if (self.isEmpty()):
			return float("-inf")
		return self.root.data

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek(),"top element of stack")
print(stack.pop(),"popped from stack")