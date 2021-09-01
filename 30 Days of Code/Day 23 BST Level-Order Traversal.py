import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
	def insert(self,root,data):
		if root==None:
			return Node(data)
		else:
			if data<=root.data:
				cur=self.insert(root.left,data)
				root.left=cur
			else:
				cur=self.insert(root.right,data)
				root.right=cur
		return root

	def levelOrder(self,root):
		#Write your code here
		if root is None:
			return None

		qu = []
		qu.append(root)

		while len(qu) !=0:
			p = qu.pop(0)
			print(p.data, end=' ')
			if p.left is not None:
				qu.append(p.left)
			if p.right is not None:
				qu.append(p.right)

# T=int(input())
myTree=Solution()
root=None
# for i in range(T):
#     data=int(input())

root=myTree.insert(root,3)
root=myTree.insert(root,5)
root=myTree.insert(root,4)
root=myTree.insert(root,7)
root=myTree.insert(root,2)
root=myTree.insert(root,1)

myTree.levelOrder(root)
