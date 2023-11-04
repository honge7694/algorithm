class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		self.root = None
		self.result = 0
		
	def make_tree_by(self, lst, index):
		parent = None
		
		if len(lst) > index:
			value = lst[index]
			
			parent = Node(value)
			parent.left = self.make_tree_by(lst, 2 * index + 1)
			parent.right = self.make_tree_by(lst, 2 * index + 2)
		
		if index == 0:
			self.root = parent
		
		return parent
	
	def rangeSumBST(self, root, low, high):
		def dfs(node):
			if not node:
				return 
			
			if node.val and low <= node.val and node.val <= high:
				self.result += node.val
				print(node.val)
			
			dfs(node.left)
			dfs(node.right)
			
			return 
		
		dfs(root)
		return self.result
			
			
lst = [10,5,15,3,7,None,18]
s1 = Solution()
s1.make_tree_by(lst, 0)
print(s1.rangeSumBST(s1.root, 7, 15))