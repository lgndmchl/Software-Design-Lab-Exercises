
class Node:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None


def PostPreInOrderInOneFlowRecursive(root, pre, post, In):

	if (root == None):
		return


	pre.append(root.data)

	PostPreInOrderInOneFlowRecursive(root.left, pre, post, In)

	In.append(root.data)

	
	PostPreInOrderInOneFlowRecursive(root.right, pre, post, In)


	post.append(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.right= Node(12)
root.left.right.left = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)


pre,post,In = [],[],[]


PostPreInOrderInOneFlowRecursive(root, pre, post, In)

print("Pre Order : ",end = "")
for i in pre:
	print(i,end = " ")

print()
print("Post Order : ",end = "")
for i in post:
	print(i,end = " ")
print()
print("In Order : ",end = "")
for i in In:
	print(i,end = " ")
