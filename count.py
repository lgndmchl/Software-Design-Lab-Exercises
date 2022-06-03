
class node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def left_height(node):
	ht = 0
	while(node):
		ht += 1
		node = node.left
		

	return ht


def right_height(node):
	ht = 0
	while(node):
		ht += 1
		node = node.right
		
	return ht


def TotalNodes(root):


	if(root == None):
		return 0
	
	lh = left_height(root)
	rh = right_height(root)
	
	
	if(lh == rh):
		return (1 << lh) - 1
	
	
	return 1 + TotalNodes(root.left) + TotalNodes(root.right)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)

print(TotalNodes(root))


