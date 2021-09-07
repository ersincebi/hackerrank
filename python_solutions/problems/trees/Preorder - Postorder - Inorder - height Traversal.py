class Node:
	def __init__(self, info): 
		self.info = info  
		self.left = None  
		self.right = None 
		self.level = None 

	def __str__(self):
		return str(self.info) 

class BinarySearchTree:
	def __init__(self): 
		self.root = None

	def create(self, val):  
		if self.root == None:
			self.root = Node(val)
		else:
			current = self.root
		
			while True:
				if val < current.info:
					if current.left:
						current = current.left
					else:
						current.left = Node(val)
						break
				elif val > current.info:
					if current.right:
						current = current.right
					else:
						current.right = Node(val)
						break
				else:
					break

def preOrder(root):
	#Write your code here
	if root is None:
		return
	print(root.info, end=" ")
	preOrder(root.left)
	preOrder(root.right)
	
def postOrder(root):
	#Write your code here
	if root is None:
		return
	
	postOrder(root.left)
	postOrder(root.right)
	print(root.info, end=" ")

def inOrder(root):
	#Write your code here
	if root is None:
		return
	
	inOrder(root.left)
	print(root.info, end=" ")
	inOrder(root.right)

def height(root):
	if root is None:
		return -1

	left = height(root.left)
	right = height(root.right)

	return max(left, right) + 1

def topView(root):
	if root is None:
		return
	

tree = BinarySearchTree()
t = 6

arr = list(map(int, '1 2 5 3 4 6'.split()))

for i in range(t):
	tree.create(arr[i])

preOrder(tree.root) # expected: 1 2 5 3 4 6
print()
postOrder(tree.root) # expected: 4 3 6 5 2 1
print()
inOrder(tree.root) # expected: 1 2 3 4 5 6
print()
print(height(tree.root)) # expected: 4
topView(tree.root) # expected: 1 2 5 6