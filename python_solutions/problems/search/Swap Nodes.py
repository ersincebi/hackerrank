
global root

class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.right = None
		self.left = None

def inorder(node):
	if node is None:
		return
	
	inorder(node.left)
	print(node.data, end=" ")
	inorder(node.right)

def insertNodes(data):
	global root
	node = Node(data)
	if root is None:
		root = node
	else:
		tmp = root
		parent = root
	
		while tmp is not None:
			parent = tmp;
			if data < tmp.data:
				tmp = tmp.left;
			elif data > tmp.data:
				tmp = tmp.right
		
		if data < parent.data:
			parent.left = node
		else:
			parent.right = node
		

def swapEveryKLevelUtil(root, level, k):
	if (root is None or (root.left is None and
						root.right is None ) ):
		return

	if (level+1)%k == 0:
		root.left, root.right = root.right, root.left

	swapEveryKLevelUtil(root.left, level+1, k)
	swapEveryKLevelUtil(root.right, level+1, k)

def swapEveryKLevel(root, k):
	swapEveryKLevelUtil(root, 1, k)

def swapNodes(indexes, queries):
	global root
	root = Node(1)

	for a, b in indexes:
		if a != -1:
			insertNodes(a)
		if b != -1:
			insertNodes(b)
	
	inorder(root)
	for k in queries:
		swapEveryKLevel(root, k)
	print()
	inorder(root)

if __name__ == '__main__':
	indexes = [[2, 3],[-1, -1],[-1, -1]]

	indexes = [
		[2, 3],
		[-1, 4],
		[-1, 5],
		[-1, -1],
		[-1, -1]
		]
	queries = [1, 1]


	'''
	expected:
		3 1 2
		2 1 3
	'''
	swapNodes(indexes, queries)