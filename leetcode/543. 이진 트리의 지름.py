class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left =left
		self.right = right

class Solution:
	def __init__(self):
		self.longest = 0
		self.root = None
		
	def __str__(self):
		if self.root:
			return f"Solution (root={self.root.val})"
		else:
			return "Solution (no root)"
			
	def make_tree_by(self, lst, index):
		parent = None
		
		if len(lst) > index:
			value = lst[index]
			
			if value is None:
				return
			
			parent = Node(value)
			parent.left = self.make_tree_by(lst, 2 * index + 1)
			parent.right = self.make_tree_by(lst, 2 * index + 2)
			
		if index == 0:
			self.root = parent
		
		return parent
		
	
	def diameterOfBinaryTree(self, root):
		if not root:
			return
		
		def dfs(node):
			if not node:
				return -1
			
			left = dfs(node.left)
			right = dfs(node.right)
			
			self.longest = max(self.longest, left + right + 2)
			return max(left, right) + 1
		
		dfs(root)
		return self.longest



lst = [1, 2, 3, 4, 5]

s1 = Solution()
s1.make_tree_by(lst, 0)
print(s1)
result = s1.diameterOfBinaryTree(s1.root)
print("Diameter of the binary tree:", result)