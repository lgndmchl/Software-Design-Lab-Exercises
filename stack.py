
class Node:
	

	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
	
	def __init__(self):
		self.head = None
	

	def isempty(self):
		if self.head == None:
			return True
		else:
			return False
	

	def push(self,data):
		
		if self.head == None:
			self.head=Node(data)
			
		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode

	def pop(self):
		
		if self.isempty():
			return None
			
		else:

			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data
	

	def peek(self):
		
		if self.isempty():
			return None
			
		else:
			return self.head.data
	

	def display(self):
		
		iternode = self.head
		if self.isempty():
			print("Stack Underflow")
		
		else:
			
			while(iternode != None):
				
				print(iternode.data,"->",end = " ")
				iternode = iternode.next
			return
		

MyStack = Stack()

MyStack.push(28)
MyStack.push(56)
MyStack.push(89)
MyStack.push(472)

# Display  the stack elements
MyStack.display()

# Print the top element of stack
print("\nTop element is ",MyStack.peek())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display the stack elements
MyStack.display()

# Print the top element of stack
print("\nTop element is ", MyStack.peek())


